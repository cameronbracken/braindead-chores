from flask.ext.wtf import Form, recaptcha
from wtforms.fields import TextField, PasswordField
from wtforms.validators import required, Email, ValidationError

from chores import db
from models import *


# Define login and registration forms (for flask-login)
class LoginForm(Form):
    email = TextField(validators=[required('Email required'), Email()])
    password = PasswordField(validators=[required('Password required')])

    def validate_login(self):
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')

        if user.password != self.password.data:
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()


class RegistrationForm(Form):
    email = TextField(validators=[required('Email required'), Email()])
    password = PasswordField(validators=[required('Password required')])
    recaptcha = recaptcha.RecaptchaField()

    def validate_login(self):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise ValidationError('Duplicate username')