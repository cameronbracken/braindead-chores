from . import db
from flask.ext.security import UserMixin, RoleMixin, current_user

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))

# Create user model. For simplicity, it will store passwords in plain text.
# Obviously that's not right thing to do in real world application.
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref='users')
    households = db.relationship('Household', backref='users')

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
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Household(db.Model):
    __tablename__ = 'households'
    __table_args__ = ( db.UniqueConstraint('name', 'magic_word'), )
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    magic_word = db.Column(db.String(255))
    creator_id = db.Column(db.Integer(), db.ForeignKey(User.id))

    def __init__(self):
        self.creator_id = current_user.id

class HouseholdMembers(db.Model):
    __tablename__ = 'household_members'
    __table_args__ = ( db.UniqueConstraint('user_id', 'household_id'), )
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    household_id = db.Column(db.Integer(), db.ForeignKey(Household.id))
    members = db.relationship('Household', backref='household_members')

    def __init__(self):
        self.user_id = current_user.id
