from flask import Flask, render_template, request, session, flash, redirect, url_for
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import datetime
import logging
import check
import os

SECRET_KEY = os.getenv('SECRET_KEY')
PASSCODE = os.getenv('PASSCODE')
LOG_PATH = os.getenv('LOG_PATH')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def log(msg):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(LOG_PATH, maxBytes=100000000, backupCount=5)

    logger.addHandler(handler)
    
    logger.info(f'{str(datetime.datetime.now())} {msg}\n')

def get_status():
    data = check.get_status()
    if len(data) > 0:
        return data
    else:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if session.get('authenticated') == None:
            passcode = request.form['passcode']
            if passcode == PASSCODE:
                session['authenticated'] = True
                data = get_status()
                return render_template('index.html', date=data[1], time=data[2], status=data[3].title(), msg=data[4], symbol=data[5])
            else:
                log(f'Failed login attempt: "{request.remote_addr}"')
                flash('Failed login attempt.')
                return render_template('index.html')
        else:
            return render_template('index.html')
    else:
        if session.get('authenticated'):
            data = get_status()

            return render_template('index.html', date=data[1], time=data[2], status=data[3].title(), msg=data[4], symbol=data[5])
        else:
            return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    check.init()
    app.run(debug=True)