from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField


class Loginform(Flaskform):
    username = StringField(label='Username:')
    password_hash = PasswordField(label='Password')
    submi = SubmitField(label='submit')


class Registerform(Flaskform):
    username = StringField(label='Username:')
    password_hash = PasswordField(label='Password')
    submi = SubmitField(label='submit')
