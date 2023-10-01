from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{"name": "index", "url": "index"},
        {"name": "about", "url": "about"},
        {"name": "feedback", "url": "feedback"}]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html",
                           title="about",
                           menu=menu)


@app.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        print(request.form.get("user_name"))
    return render_template("feedback.html",
                           title="feedback",
                           menu=menu)

# @app.route("/profile/<user_name>")
# def profile(user_name):
#     return f"User: {user_name}"


# with app.test_request_context():
#     print(url_for('about'))

if __name__ == "__main__":
    app.run(debug=True)
