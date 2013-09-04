import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mako import MakoTemplates, render_template
from config import basedir
import flask.ext.security as sec 
from flask.ext.mail import Mail

sec.views.render_template = render_template
sec.utils.render_template = render_template


#setup app
app = Flask(__name__)
app.config.from_object('config')

# mako initilization
app.template_folder = "templates"
mako = MakoTemplates(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'

# mail setup 
mail = Mail(app)

from . import views, forms, models

# Setup Flask-Security
user_datastore = sec.SQLAlchemyUserDatastore(db, models.User, models.Role)
security = sec.Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    #user_datastore.create_user(email='cameron.bracken@gmail.com', password='password')
    db.session.commit()


#msg = Message(
#          'Hello',
#       sender='you@dgoogle.com',
#       recipients=
#           ['recipient@recipient_domain.com'])
#msg.body = "This is the email body"
#mail.send(msg)
#return "Sent"