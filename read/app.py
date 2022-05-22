from supabase import create_client, Client
from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv('URL')
API_KEY = os.getenv('API_KEY')

supabase: Client = create_client(URL, API_KEY)

app = Flask(__name__)

def read_data():
    data = (supabase.table("status").select("*").limit(15).execute()).data
    return data[-10:]

@app.route('/')
def index():
    return render_template('index.html', data=read_data())

if __name__ == '__main__':
    app.run(debug=True)