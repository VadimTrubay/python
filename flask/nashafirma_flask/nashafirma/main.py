import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for, make_response
from DataBase import DataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin

DEBUG = True

DATABASE = 'products_list.db'
SECRET_KEY = 'bdr3t6567hb45e5urgs55trjh65h0ytg'
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config.update(DATABASE=os.path.join(app.root_path, 'products_list.db'))

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Log in to access restricted pages'
login_manager.login_message_category = 'success'

menu = [
    {"name": "Home", "url": "index.html"},
    {"name": "About", "url": "about.html"},
    {"name": "Products", "url": "products.html"},
    {"name": "Orders", "url": "orders.html"},
    {"name": "Contacts", "url": "contacts.html"},
]


@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(user_id, dbase)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None
@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = DataBase(db, menu)


@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
@app.route("/index.html")
def index():
    return render_template(
        'index.html', title='Home', menu=dbase.getMenu())


@app.route("/contacts.html")
def contacts():
    return render_template(
        'contacts.html', title='Contacts', menu=dbase.getMenu())


@app.route("/products.html", methods=["POST", "GET"])
@login_required
def all_products():
    products_list = dbase.allProducts()
    return render_template('products.html',
                           title='Products', menu=dbase.getMenu(),
                           products_list=products_list)


@app.route("/add_product.html", methods=["POST", "GET"])
@login_required
def add_product():
    if request.method == "POST":
        if len(request.form['product']) > 2:
            res = dbase.addProduct(request.form['product'], request.form['price'], request.form['note'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
                return redirect(url_for('all_products'))
        else:
            flash('Ошибка добавления статьи', category='error')

    else:
        return render_template('add_product.html',
                               title='Add product', menu=dbase.getMenu())


@app.route("/edit_product/<product>", methods=["POST", "GET"])
@login_required
def edit_product(product):
    if request.method == "POST":
        new_product = request.form.get('product')
        new_price = request.form.get('price')
        new_note = request.form.get('note')
        if len(new_product) > 2:
            res = dbase.editProduct(new_product, new_price, new_note, product)
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
                return redirect(url_for('all_products'))
        else:
            flash('Ошибка добавления статьи', category='error')
    else:
        product_data = dbase.getProduct(product)
        return render_template(
            'edit_product.html', title='Edit product', menu=dbase.getMenu(), product=product, product_data=product_data)


@app.route("/delete_product/<product>", methods=["POST", "GET"])
@login_required
def delete_product(product):
    if request.method == "POST":
        if request.form.get("confirmation") == "yes":
            res = dbase.delProduct(product)
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
                return redirect(url_for('all_products'))
        else:
            return redirect(url_for('all_products'))
    else:
        return render_template('delete_product.html', title='Delete Product', menu=menu, product=product)


@app.route("/orders.html", methods=["POST", "GET"])
@login_required
def all_orders():
    orders_list = dbase.allOrders()
    return render_template(
        'orders.html',
        title='Orders', menu=menu,
        orders_list=orders_list)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template(
        'page404.html', title='Page not fount', menu=menu), 404


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == "POST":
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            rm = True if request.form.get('remainme') else False
            login_user(userlogin, remember=rm)
            return redirect(request.args.get("next") or url_for("profile"))

        flash("Неверная пара логин/пароль", "error")

    return render_template("login.html", menu=dbase.getMenu(), title="Авторизация")



@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
            and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('login'))
            else:
                flash("Ошибка при добавлении в БД", "error")
        else:
            flash("Неверно заполнены поля", "error")

    return render_template("register.html", menu=dbase.getMenu(), title="Регистрация")



@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html", menu=dbase.getMenu(), title="Профиль")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))


@app.route('/userava')
@login_required
def userava():
    img = current_user.getAvatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h

@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verifyExt(file.filename):
            try:
                img = file.read()
                res = dbase.updateUserAvatar(img, current_user.get_id())
                if not res:
                    flash("Ошибка обновления аватара", "error")
                flash("Аватар обновлен", "success")
            except FileNotFoundError as e:
                flash("Ошибка чтения файла", "error")
        else:
            flash("Ошибка обновления аватара", "error")

    return redirect(url_for('profile'))


if __name__ == "__main__":
    app.run(debug=True)
