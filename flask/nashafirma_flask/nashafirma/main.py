import os
import sqlite3
import time
from flask import (Flask,
                   render_template,
                   url_for,
                   request,
                   flash,
                   session,
                   redirect,
                   abort,
                   g)

DEBUG = True
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


menu = [
    {"name": "main", "url": "index.html"},
    {"name": "products", "url": "products.html"},
    {"name": "orders", "url": "orders.html"},
    {"name": "contacts", "url": "contacts.html"},
]


@app.route("/")
@app.route("/index.html")
def index():
    return render_template(
        'index.html', title='nasha-firma', menu=menu)


@app.route("/contacts.html")
def contacts():
    return render_template(
        'contacts.html', title='nasha-firma', menu=menu)


@app.route("/products.html", methods=["POST", "GET"])
def products():
    conn = get_db()
    all_products = conn.execute('SELECT * FROM products_list').fetchall()
    return render_template(
        'products.html',
        title='products', menu=menu,
        products_list=all_products)


@app.route("/add_product.html", methods=["POST", "GET"])
def add_product():
    if request.method == "POST":
        product = request.form.get('product')
        price = request.form.get('price')
        note = request.form.get('note')
        conn = get_db()
        cursor = conn.execute(
            'SELECT product FROM products_list WHERE product = ?', (product,))
        existing_product = cursor.fetchone()
        if existing_product:
            flash(f'Error: Product "{product}" already exists')
        elif len(product) <= 2:
            flash('Product name must be at least 3 characters long')
        else:
            conn.execute(
                'INSERT INTO products_list (product, price, note) VALUES (?, ?, ?)', (product, price, note))
            conn.commit()
            return redirect(url_for('products'))
    return render_template(
        'add_product.html', title='Add Product', menu=menu)


@app.route("/edit_product/<product>", methods=["POST", "GET"])
def edit_product(product):
    if request.method == "POST":
        new_product = request.form.get('product')
        new_price = request.form.get('price')
        new_note = request.form.get('note')
        if len(new_product) > 2:
            conn = get_db()
            conn.execute(
                'UPDATE products_list SET product = ?, price = ?, note = ? WHERE product = ?',
                (new_product, new_price, new_note, product))
            conn.commit()
            return redirect(url_for('products'))
        else:
            flash('Product name must be at least 3 characters long')
    else:
        conn = get_db()
        cursor = conn.execute(
            'SELECT product, price, note FROM products_list WHERE product = ?', (product,))
        product_data = cursor.fetchone()
        return render_template(
            'edit_product.html', title='Edit product', menu=menu, product=product, product_data=product_data)


@app.route("/delete_product/<product>", methods=["POST", "GET"])
def delete_product(product):
    if request.method == "POST":
        if request.form.get("confirmation") == "yes":
            conn = get_db()
            conn.execute(
                'DELETE FROM products_list WHERE product = ?', (product,))
            conn.commit()
            return redirect(url_for('products'))
        else:
            return redirect(url_for('products'))
    else:
        return render_template('delete_product.html', title='Delete Product', menu=menu, product=product)


@app.route("/orders.html", methods=["POST", "GET"])
def orders():
    if request.method == "POST":
        print(request.form["product"])
    return render_template(
        'orders.html', title='orders', menu=menu)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template(
        'page404.html', title='page not fount', menu=menu), 404


@app.route("/login.html", methods=["POST", "GET"])
def login():
    if 'userLogger' in session:
        return redirect(url_for("profile", username=session['userLogger']))
    elif request.method == "POST" and request.form['username'] == 'admin' and request.form['psw'] == '1111':
        session['userLogger'] = request.form['username']
        return redirect(url_for("profile", username=session['userLogger']))
    return render_template('login.html', title='authorization', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogger' not in session and session['userLogger'] != username:
        abort(401)
    return render_template('profile.html', title='profile', menu=menu, username=username)


@app.route("/logout")
def logout():
    session.clear()
    session.pop('username', None)
    return redirect(url_for('login', title='profile', menu=menu))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
