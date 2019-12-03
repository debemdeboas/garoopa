from flask import Flask, redirect, render_template

from src.classes import *
from src.web_forms import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '91661dd23df8a7b72c3a'

clients = {}
drivers = {}


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
    return render_template('registered_user.html', main_header='Client - Main Menu',
                           ranks=ranks, p_methods=payment_methods, user=clients[cpf])


@app.route("/driver", methods=['POST', 'GET'])
def driver():
    form = DriverRegistrationForm()
    return render_template('driver.html', form=form, main_header='Driver Registration Page', title='Register Driver')


@app.route('/registered_driver', methods=['POST', 'GET'])
def registered_driver():
    return render_template('registered_driver.html', main_header='Driver\'s Control Panel', title='Control Panel')


if __name__ == "__main__":
    Geometry()
    app.run(debug=True)
