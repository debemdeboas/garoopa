from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FieldList
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
