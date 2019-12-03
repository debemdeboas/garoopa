from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired


class MemberRegistrationForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    username = StringField('Full name', validators=[DataRequired()])

    submit = SubmitField('Register')


class DriverRegistrationForm(MemberRegistrationForm):
    car_type = SelectField('Car Type', choices=[], validators=[DataRequired()])
    lic_plate = StringField('License Plate', validators=[DataRequired()])
    make = StringField('Make and Model', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    answers = BooleanField('Answer lower-category trips?')
    big_trunk = BooleanField('Does your car have a big trunk?')
    payment_methods = SelectMultipleField('Accepted Payment Methods', validators=[DataRequired()], choices=[])


class TripForm(FlaskForm):
    driver_ranks = SelectField('Car Type', choices=[], validators=[DataRequired()])
    payment_method = SelectField('Payment Method', choices=[], validators=[DataRequired()])
    city = SelectField('City', choices=[], validators=[DataRequired()])
    big_trunk = BooleanField('Big Trunk')

    from_where = SelectField('From', choices=[], validators=[DataRequired()])
    to_where = SelectField('To', choices=[], validators=[DataRequired()])

    submit = SubmitField('Request trip')


class RateForm(FlaskForm):
    stars = SelectField('Stars', choices=[(v, v) for v in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    submit = SubmitField('Rate')


class RateDriverTripsForm(RateForm):
    selected_trip = SelectField('Trip ID', choices=[], validators=[DataRequired()])
