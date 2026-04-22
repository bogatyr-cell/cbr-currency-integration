import sqlite3

database_name = 'database.db'

def install():
    with sqlite3.connect(database_name) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS rates
            (id INTEGER PRIMARY KEY, currency TEXT, rate REAL, date TEXT,
             UNIQUE(currency, date))''')