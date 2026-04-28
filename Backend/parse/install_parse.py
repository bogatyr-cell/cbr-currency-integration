import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from Backend.database.install_DB import *
#from Backend.loggers.loggers_init import install_log_system as Log

def install(database_name):
    resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(resp.content)
    date = root.get('Date')

    with sqlite3.connect(database_name) as conn:
        for v in root.findall('Valute'):
            code = v.find('CharCode').text
            if code in ['USD', 'EUR', 'CNY']:
                rate = float(v.find('Value').text.replace(',', '.'))
                conn.execute('''
    INSERT OR IGNORE INTO RATES_HISTORY 
    (currency, rate, rate_date) 
    VALUES (?, ?, ?)
''', (code, rate, date))
   # Log('good','Parse',f'Курсы обновлены: {date}')


def get_last_history(currency, days=365):
    with sqlite3.connect(database_name) as conn:
        data = conn.execute('''
            SELECT rate_date, rate FROM RATES_HISTORY 
            WHERE currency = ? 
            ORDER BY rate_date DESC LIMIT ?
        ''', (currency.upper(), days)).fetchall()
    #Log('good','Parse (get_last_history)','Получена история')
    return {
        'dates': [d[0] for d in reversed(data)],
        'rates': [d[1] for d in reversed(data)]
        
    }


def get_active_valute():
    with sqlite3.connect(database_name) as conn:
        return conn.execute('''
            SELECT currency_code, name_ru, nominal 
            FROM CONFIG  
            WHERE is_active = 1
        ''').fetchall()
   # Log('good','Parse (get_active_valute)','Получен активный список валют')
    
#six seven
def get_sync_status(limit=67):
    with sqlite3.connect(database_name) as conn:
        return conn.execute('''
            SELECT sync_started, sync_finished, status, records_count, error_message 
            FROM Logs  
            ORDER BY id DESC LIMIT ?
        ''', (limit,)).fetchall()
    #Log('good','Parse (get_sync_status)','Логи получены')
