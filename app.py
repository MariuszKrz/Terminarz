import  base
import insert
from datetime import date
from  flask import Flask, render_template
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('organizer.html')

# @app.route('/organizer')
# def organizer():
#    return render_template('organizer.html')

if __name__ == '__main__':
   app.run(debug=True)
