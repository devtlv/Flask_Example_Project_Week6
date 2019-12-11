from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, validators


class LoginForm(FlaskForm):
    email = StringField('E-Mail')
    password = PasswordField('Password')


class RegisterForm(FlaskForm):
    email = StringField('E-Mail', [validators.required()])
    password = PasswordField('Password', [validators.required()])
    confirm_password = PasswordField('Confirm Password', [validators.required()])
    first_name = StringField('First Name', [validators.required()])
    last_name = StringField('Last Name', [validators.required()])
    country = StringField('Country', [validators.required()])
    sex = SelectField('Sex', [validators.required()],
                      choices=(('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other'))
                      )

    def validate(self):
        result = super().validate()
        return result and self.password.data == self.confirm_password.data
