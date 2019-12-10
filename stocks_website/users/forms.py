from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class LoginForm(FlaskForm):
    email = StringField('E-Mail')
    password = PasswordField('Password')
