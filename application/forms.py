from flask_security.forms import LoginForm
from wtforms import BooleanField


class ExtendedLoginForm(LoginForm):
    admin = BooleanField('Admin')
    sponsor = BooleanField('Sponsor')
    influencer = BooleanField('Influencer')
