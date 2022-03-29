from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

DB_PATH = os.getenv('DB_PATH')

def check(date, time, status, msg):

    if status == 'open':
        symbol = 'fa-solid fa-circle-check'
    else:
        symbol = 'fa-solid fa-circle-xmark' 

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO History(date, time, status, msg, symbol) VALUES(?, ?, ?, ?, ?)', (date, time, status, msg, symbol))
    conn.commit()
    c.close()
    conn.close()

def get_status():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM History DESC LIMIT 1;')
    results = c.fetchone()
    if results:
        return results
    else:
        return []

def init():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS History(id INTEGER PRIMARY KEY, date TEXT, time TEXT, status TEXT, msg TEXT, symbol TEXT)')
    conn.commit()
    c.close()
    conn.close()