import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from Frontend.database.install_DB import *

def install():
    resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(resp.content)
    date = root.get('Date')

    #with sqlite3.connect(database_name) as conn:
        # print(f'✓ Курсы обновлены: {date}')

