import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///zadania1.db', echo=False)
base = declarative_base()

class Terminarz(base):
   __tablename__ = 'zadania'

   id = Column(Integer, primary_key=True)
   name = Column(String)
   date = Column(String)
   description = Column(String)

   def __init__(self, name, date, description):
      self.name = name
      self.date = date
      self.description = description

base.metadata.create_all(engine)
