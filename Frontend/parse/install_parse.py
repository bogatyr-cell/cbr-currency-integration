import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from Backend.database.install_DB import *
from Backend.loggers.loggers_init import install_log_system as Log

def install():
    resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(resp.content)
    date = root.get('Date')

    with sqlite3.connect(DB) as conn:
        for v in root.findall('Valute'):
            code = v.find('CharCode').text
            if code in ['USD', 'EUR', 'CNY']:
                rate = float(v.find('Value').text.replace(',', '.'))
                conn.execute('INSERT OR IGNORE INTO rates VALUES (?,?,?)', (code, rate, date))
    Log('good','Parse',f'Курсы обновлены: {date}')
