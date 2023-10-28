import sqlite3
import os
from flask import (Flask,
                   render_template,
                   url_for,
                   request,
                   flash,
                   session,
                   redirect,
                   abort,
                   g)

DATABASE = 'products_list.db'
SECRET_KEY = 'bdrt6567hb45ergstrjh65hytg'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'products_list.db'))


def init_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as fh:
        db.cursor().executescript(fh.read())
    db.commit()
    db.close()


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

