from flask import Flask, request, send_file

from src.geometry import Geometry

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
    return send_file("index.html")


@app.route("/user")
def user():
    return send_file("user.html")


@app.route("/driver")
def driver():
    return send_file("driver.html")


def calc_trip(trip, current_driver):
    base_cost, number_of_neighborhoods = trip.trip_cost()
    if current_driver.rank == 'LUX':
        base_cost = base_cost * 1.1
        base_cost = base_cost * (1 + (0.02 * number_of_neighborhoods))
    elif current_driver.rank == 'SIMPLE':
        base_cost = base_cost * 1.1
    return base_cost


if __name__ == "__main__":
    Geometry(0, 0, 0, 0)
    app.run(debug=True)
