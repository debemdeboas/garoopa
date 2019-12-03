from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired


class MemberRegistrationForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    username = StringField('Full name', validators=[DataRequired()])

    submit = SubmitField('Register')


class DriverRegistrationForm(MemberRegistrationForm):
    lic_plate = StringField('License Plate', validators=[DataRequired()])
    make = StringField('Make and Model', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    answers = BooleanField('Answer lower-category trips?')


class TripForm(FlaskForm):
    driver_ranks = SelectField('Car Type', choices=[], validators=[DataRequired()])
    payment_method = SelectField('Payment Method', choices=[], validators=[DataRequired()])
    city = SelectField('City', choices=[], validators=[DataRequired()])
    big_trunk = BooleanField('Big Trunk')

    from_where = SelectField('From', choices=[], validators=[DataRequired()])
    to_where = SelectField('To', choices=[], validators=[DataRequired()])

    submit = SubmitField('Request trip')
