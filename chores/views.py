from flask import url_for, redirect, request, flash
#use mako instead of jinja2 (its less ugly)
from flask.ext.mako import render_template
from flask.ext import login
from flask.ext.security import current_user
from flask.ext.security.decorators import login_required

from . import app, db, login
from forms import * 
from models import *


# Create user loader function
@login.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# Flask views
@app.route('/', methods=('GET', 'POST'))
def index():
    if current_user.is_authenticated(): 

        forms = {}
        forms['create_household'] = CreateHousehold(csrf_enabled=True)
        forms['join_household'] = CreateHousehold(csrf_enabled=True)

        households = Household.query.join(HouseholdMembers).filter_by(user_id=current_user.id).all()

        return render_template('authenticated.html', current_user=current_user, forms=forms,
                               households=households)
    else:
        return render_template('anonymous.html', current_user=current_user)


#@user_registered.connect_via(app)
#def user_registered_sighandler(app, user, confirm_token):
#    default_role = user_datastore.find_role("User")
#    user_datastore.add_role_to_user(user, default_role)
#    db.session.commit()

@app.route('/create_household', methods=('GET', 'POST'))
@login_required
def create_household():
    
    form = CreateHousehold(csrf_enabled=True)
    
    if form.validate_on_submit():
        try: 
            house_id = add_household(form)
        except:
            flash("The household %s with magic word %s already exists." % (form.name.data, form.magic_word.data))
            return redirect('/#households')

        add_current_user_to_household(house_id)
        flash('Added household %s.' % (form.name.data))
        return redirect('/#households')


@app.route('/join_household', methods=('GET', 'POST'))
@login_required
def join_household():
    
    form = JoinHousehold(csrf_enabled=True)
    
    if form.validate_on_submit():

        house_id = db.session.query(Household.id).\
                        filter_by(name=form.name.data, 
                                  magic_word=form.magic_word.data).scalar()

        if house_id is None:
            flash('The household %s with magic word %s doesn\'t exist.' % (form.name.data, form.magic_word.data))
            return redirect('/#households')
        else:
            try: 
                add_current_user_to_household(house_id)
                flash('You have been added to the household %s.' % (form.name.data))
            except:
                flash("You are already part of the household %s." % (form.name.data))
            return redirect('/#households')

def add_household(form):
    
    household = Household()
    form.populate_obj(household)

    db.session.add(household)
    db.session.commit()

    id = db.session.query(Household.id).\
                    filter_by(name=form.name.data, 
                        creator_id=current_user.id).scalar()
    return id


def add_current_user_to_household(house_id):

    household_members = HouseholdMembers()
    household_members.household_id = house_id

    db.session.add(household_members)
    db.session.commit()


