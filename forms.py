from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import URL, Optional, Length, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", [Length(min=1)])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", [Optional(), URL()])
    age = IntegerField("Age", [Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", [Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", [Optional(), URL()])
    notes = StringField("Notes", [Optional()])
    available = BooleanField("Available")
