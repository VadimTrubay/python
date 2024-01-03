from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.before_request
def before_request():
    init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message.html', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        message = request.form.get('message')
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (user_name, message) VALUES (?, ?)', (user_name, message))
        conn.commit()
        conn.close()
        return render_template('/thanks.html', user_name=user_name)
    return render_template('/message.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/error.html')
def error():
    return render_template('error.html')


@app.route('/thanks.html')
def thanks(user_name):
    return render_template('thanks.html', user_name=user_name)


def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS posts '
                 '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'user_name TEXT NOT NULL, '
                 'message TEXT NOT NULL)')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def close_db_connection(conn):
    conn.close()


if __name__ == '__main__':
    app.run()
