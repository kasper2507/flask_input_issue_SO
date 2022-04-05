from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UdlaanForm(FlaskForm):
    customerID = StringField('Kunde ID')
    submit = SubmitField('Register')