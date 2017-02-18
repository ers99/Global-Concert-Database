import datetime
from app import db, models
db.create_all()

u = models.User(username='Test', email='test@my.fsu.edu')
db.session.add(u)
p = models.Post(body='doodoo', timestamp=datetime.datetime.utcnow(), author = u)
db.session.add(p)
db.session.commit()

