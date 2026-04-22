import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from Frontend.database.install_DB import *

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
    print(f'✅ Курсы обновлены: {date}')

