from flask import url_for, redirect, request, flash
#use mako instead of jinja2 (its less ugly)
from flask.ext.mako import MakoTemplates, render_template
from flask.ext import login
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms.validators import ValidationError
from flask.ext.mail import Mail
from flask.ext.security.decorators import login_required

from . import app, db, login_manager
from forms import * 
from models import *


# Create user loader function
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# Flask views
@app.route('/', methods=('GET', 'POST'))
@login_required
def index():
    return render_template('chores.html', user=login.current_user)

