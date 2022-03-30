from flask import Flask, render_template, request, session, flash, redirect, url_for
from dotenv import load_dotenv
import check
import os

SECRET_KEY = os.getenv('SECRET_KEY')
PASSCODE = os.getenv('PASSCODE')
LOG_PATH = os.getenv('LOG_PATH')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

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
                check.log(f'Failed login attempt: "{request.remote_addr}"')
                flash('Failed login attempt.')
                return render_template('index.html')
        else:
            data = get_status()
            return render_template('index.html', date=data[1], time=data[2], status=data[3].title(), msg=data[4], symbol=data[5])
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