import base
from sqlalchemy.orm import sessionmaker
# Stworzenie nowej sesji
Session = sessionmaker(bind=base.engine)
session = Session()
# dodanie danych
for t in range(10):
    tr = base.Terminarz(t, '2020/05/06', 12)
    session.add(tr)
# zapis zmian w bazie danych
session.commit()