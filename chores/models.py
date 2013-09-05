from . import db
from flask.ext.security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

households_users = db.Table('households_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('household_id', db.Integer(), db.ForeignKey('household.id')))

# Create user model. For simplicity, it will store passwords in plain text.
# Obviously that's not right thing to do in real world application.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    household = db.relationship('Household', secondary=households_users,
                            backref=db.backref('users', lazy='dynamic'))


    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.email)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Household(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    magic_word = db.Column(db.String(255))