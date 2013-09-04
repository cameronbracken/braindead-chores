from config import SQLALCHEMY_DATABASE_URI
from chores import db
db.create_all()