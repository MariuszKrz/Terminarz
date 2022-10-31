import base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=base.engine)
session = Session()

records = session.query(base.Terminarz).all()
