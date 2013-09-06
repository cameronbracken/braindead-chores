from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField
from wtforms.validators import required


# Define login and registration forms (for flask-login)
class CreateHousehold(Form):
    name = TextField(validators=[required('Need a household name.')])
    magic_word = TextField(validators=[required('Need to create a magic word.')])
    submit = SubmitField()

class JoinHousehold(Form):
    name = TextField(validators=[required('Need a household name.')])
    magic_word = TextField(validators=[required('You didn\'t say the magic word!')])
    submit = SubmitField()