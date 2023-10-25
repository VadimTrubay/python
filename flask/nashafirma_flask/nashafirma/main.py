from flask import (Flask,
                   render_template,
                   url_for,
                   request, flash)


app = Flask(__name__)
app.config["SECRET_KEY"] = 'bdrt6567hb45ergstrjh65hytg'

menu = [
        {"name": "products", "url": "products.html"},
        {"name": "orders", "url": "orders.html"},
]

products_list =  [
             {"name": "lime", "price": 12, "note": "fresh"},
             {"name": "awokado", "price": 55, "note": "-"},
]

@app.route("/")
@app.route("/index.html")
def index():
    return render_template(
        'index.html', title='nasha-firma', menu=menu)

@app.route("/products.html", methods=["POST", "GET"])
def products():
    return render_template(
        'products.html', title='products', menu=menu, products_list=products_list)


@app.route("/add_product.html", methods=["POST", "GET"])
def add_product():
    if request.method == "POST":
        if len(request.form['product']) > 2:
            flash('product added')
        else:
            flash('error sent')
        print(request.form)
    return render_template(
        'add_product.html', title='add product', menu=menu)

@app.route("/orders.html", methods=["POST", "GET"])
def orders():
    if request.method == "POST":
        print(request.form["product"])

    return render_template(
        'orders.html', title='orders', menu=menu)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template(
        'page404.html', title='page not fount', menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
