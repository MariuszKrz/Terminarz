import base
# import insert
import select
from datetime import date
from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


@app.route('/')
def hello():
    Session = sessionmaker(bind=base.engine)
    session = Session()

    records = session.query(base.Terminarz).all()

    return render_template('organizer.html', d = records)

if __name__ == '__main__':
    app.run(debug=True)
