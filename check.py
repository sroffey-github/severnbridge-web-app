import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import datetime
import logging
import sqlite3
import os

load_dotenv()

DB_PATH = os.getenv('DB_PATH')
LOG_PATH = os.getenv('LOG_PATH')

def log(msg):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(LOG_PATH, maxBytes=100000000, backupCount=5)

    logger.addHandler(handler)
    
    logger.info(f'{str(datetime.datetime.now())} {msg}\n')

def add(date, time, status, msg):

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
    c.execute('SELECT * FROM History ORDER BY id DESC LIMIT 1')
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