from flask import Flask, request, render_template

from src.classes import *

app = Flask(__name__)


@app.route("/api", methods=["GET", "POST"])
def api_get():
    if request.method == "GET":
        return "oi eu sou o %s caralho" % request.form["name"]
    elif request.method == "POST":
        data = request.form
        return data


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/user")
def user():
    return render_template('user.html', ranks=ranks)


@app.route("/driver")
def driver():
    return render_template('driver.html')


if __name__ == "__main__":
    Geometry()
    app.run(debug=True)
