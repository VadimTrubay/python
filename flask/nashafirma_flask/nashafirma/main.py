from connect_db import init_db, get_db, app
from flask import (render_template,
                   url_for,
                   request,
                   flash,
                   session,
                   redirect,
                   abort, make_response)

DEBUG = True

menu = [
    {"name": "Home", "url": "index.html"},
    {"name": "About", "url": "about.html"},
    {"name": "Products", "url": "products.html"},
    {"name": "Orders", "url": "orders.html"},
    {"name": "Contacts", "url": "contacts.html"},
]


@app.route("/")
@app.route("/index.html")
def index():
    return render_template(
        'index.html', title='Home', menu=menu)


@app.route("/contacts.html")
def contacts():
    return render_template(
        'contacts.html', title='Contacts', menu=menu)


@app.route("/products.html", methods=["POST", "GET"])
def products():
    conn = get_db()
    all_products = conn.execute('SELECT * FROM products_list').fetchall()
    return render_template(
        'products.html',
        title='Products', menu=menu,
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
    conn = get_db()
    all_orders = conn.execute('SELECT * FROM orders_list').fetchall()
    return render_template(
        'orders.html',
        title='Orders', menu=menu,
        orders_list=all_orders)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template(
        'page404.html', title='Page not fount', menu=menu), 404


@app.route("/login.html", methods=["POST", "GET"])
def login():
    if 'userLogger' in session:
        return redirect(url_for("profile", username=session['userLogger']))
    elif request.method == "POST" and request.form['username'] == 'admin' and request.form['psw'] == '1111':
        session['userLogger'] = request.form['username']
        return redirect(url_for("profile", username=session['userLogger']))
    return render_template('login.html', title='Authorization', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogger' not in session and session['userLogger'] != username:
        abort(401)
    return render_template('profile.html', title='Profile', menu=menu, username=username)


@app.route("/logout")
def logout():
    session.clear()
    session.pop('username', None)
    return redirect(url_for('index', title='Home', menu=menu))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
