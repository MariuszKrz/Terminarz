import base
from form import *
from datetime import date
from flask import Flask, render_template, url_for, redirect
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = "sikretkij"

@app.route('/')
def hello():
    form = TaskForm()
    Session = sessionmaker(bind=base.engine)
    session = Session()

    records = session.query(base.Terminarz).all()

    return render_template('organizer.html', form=form, records=records)

@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    form = TaskForm()
    Session = sessionmaker(bind=base.engine)
    session = Session()
    session.add(base.Terminarz(form.task_name.data, form.date.data, form.description.data))
    session.commit()
    records = session.query(base.Terminarz).all()


    if form.validate_on_submit():
        return redirect(url_for("hello"))

    return render_template('organizer.html', form=form, records = records)

if __name__ == '__main__':
    app.run(debug=True)
