from flask import url_for, redirect, request, flash
#use mako instead of jinja2 (its less ugly)
from flask.ext.mako import render_template
from flask.ext import login
import flask.ext.security as security

from . import app, db, login_manager
from forms import * 
from models import *


# Create user loader function
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# Flask views
@app.route('/', methods=('GET', 'POST'))
def index():
    if security.current_user.is_authenticated(): 
        return render_template('chores.mako', security=security)
    else:
        return render_template('welcome.mako', security=security)


