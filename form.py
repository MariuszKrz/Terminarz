from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, FieldList, validators

class TaskForm(FlaskForm):
    task_name = StringField('Nazwa zadania: ')
    date = StringField('Data: ')
    description = StringField('Opis: ')
