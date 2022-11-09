from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField
from wtforms.validators import DataRequired

msg = "Nie podałeś nazwy zadania"

class TaskForm(FlaskForm):
    task_name = StringField('Nazwa zadania: ', [DataRequired()])
    date = DateTimeLocalField('Data: ', [DataRequired()])
    description = StringField('Opis: ', [DataRequired()])
