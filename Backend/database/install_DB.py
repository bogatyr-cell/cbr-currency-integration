import sqlite3
#from Backend.loggers.loggers_init import install_log_system as Log

import os
from dotenv import load_dotenv

load_dotenv()


database_name = os.getenv("database_name")


def init_db():
    with sqlite3.connect(database_name) as conn:
        # курсов валют
        conn.execute('''
            CREATE TABLE IF NOT EXISTS RATES_HISTORY (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                currency TEXT NOT NULL,
                rate REAL NOT NULL,
                rate_date DATE NOT NULL,
                source TEXT DEFAULT 'ЦБ РФ',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(currency, rate_date)
            )
        ''')
        
        # логи
        conn.execute('''
            CREATE TABLE IF NOT EXISTS Logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sync_started DATETIME,
                sync_finished DATETIME,
                status TEXT,
                records_count INTEGER DEFAULT 0,
                error_message TEXT
            )
        ''')
        
        # настройки 
        conn.execute('''
            CREATE TABLE IF NOT EXISTS CONFIG (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                currency_code TEXT UNIQUE NOT NULL,
                nominal INTEGER DEFAULT 1,
                name_ru TEXT,
                is_active BOOLEAN DEFAULT 1
            )
        ''')
        #conn.close()
       # Log('good','Database','БД создано')
