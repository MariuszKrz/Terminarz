from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, FieldList
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task_name = StringField('Nazwa zadania: ')
    date = StringField('Data: ')
    description = StringField('Opis: ')
