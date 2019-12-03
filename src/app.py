import datetime

from flask import Flask, redirect, render_template

from src.classes import *
from src.web_forms import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '91661dd23df8a7b72c3a'

clients = {}
drivers = {
    '69273238972': Driver('69273238972', 'Agnaldo de Freitas',
                          NormalCar('JAG0A90', 'Ford Focus', 'Black'), 'CREDIT', True)
}
number_of_trips = 0

neighborhoods_list = [Neighborhood("Moinhos de Vento", 15, 0, 0, 4, 4),
                      Neighborhood("Menino Deus", 10, 5, 5, 6, 6),
                      Neighborhood("Lami", 5, -5, 2, 0, 11),
                      Neighborhood("Tres Figueiras", 17, -15, 3, -5, 10),
                      Neighborhood("Jardim do Salso", 8, 0, 4, 4, 10),
                      Neighborhood("Cidade Baixa", 22, -6, -2, 0, 2),
                      ]

city_info = City("Nova Porto Alegre", neighborhoods_list)


@app.route("/")
@app.route("/home")
def root():
    return render_template('index.html')


@app.route("/user", methods=['POST', 'GET'])
def user():
    form = MemberRegistrationForm()
    if form.validate_on_submit():
        clients[form.cpf.data] = (Passenger(form.cpf.data, form.username.data))
        return redirect('/registered_user/' + form.cpf.data)
    return render_template('user.html', main_header='Registration Page', title='Register Client', form=form)


@app.route('/registered_user/<cpf>', methods=['POST', 'GET'])
def registered_user(cpf):
    form = TripForm()
    form.city = city_info
    form.payment_method.choices = [(v, v) for v in payment_methods]
    form.driver_ranks.choices = [(r, r) for r in ranks]
    form.from_where.choices = [(n.name, n.name) for n in city_info.neighborhoods]
    form.to_where.choices = [(n.name, n.name) for n in city_info.neighborhoods]

    if form.validate_on_submit():
        curr_driver = get_driver(form.driver_ranks.data, form.payment_method.data, clients[cpf], drivers)
        if not curr_driver:
            return '<h1>No driver was found.</h1><a href=\"/\">Home Page</a'
        global number_of_trips
        number_of_trips += 1
        route = Route(city_info, get_neighborhood(form.from_where.data, neighborhoods_list),
                      get_neighborhood(form.to_where, neighborhoods_list))
        trip = Trip(clients[cpf], curr_driver, number_of_trips, datetime.datetime.now(), route)
        driver.trips[cpf] = trip
        return f'<h1>Your trip has ended.</h1><h2>Invoice: {trip.trip_cost()}</h2>'
    return render_template('registered_user.html', main_header='Client - Main Menu',
                           user=clients[cpf], form=form)


@app.route("/driver", methods=['POST', 'GET'])
def driver():
    form = DriverRegistrationForm()
    return render_template('driver.html', form=form, main_header='Driver Registration Page', title='Register Driver')


@app.route('/registered_driver', methods=['POST', 'GET'])
def registered_driver():
    return render_template('registered_driver.html', main_header='Driver\'s Control Panel', title='Control Panel')


if __name__ == "__main__":
    Geometry()  # Initialize the geometry singleton class with default values
    app.run(debug=True)
