from logging.handlers import RotatingFileHandler
from supabase import create_client, Client
import configparser, logging, datetime

config = configparser.ConfigParser()
config.read('config.ini')

URL = config['DATABASE']['URL']
API_KEY = config['DATABASE']['API_KEY']
LOG_PATH = config['DATABASE']['LOG_PATH']

supabase: Client = create_client(URL, API_KEY)

def log(message):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(LOG_PATH, maxBytes=1024, backupCount=3)
    logger.addHandler(handler)
    logger.info(f'[{str(datetime.datetime.now())}] {message}')

def insert(status, overview, alerted):
    data = [{"status":status, "overview":overview, "alerted":alerted}]
    supabase.table("status").insert(data).execute()
    log(f'INSERT: {status} into "status" table')