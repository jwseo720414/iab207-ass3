from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String)
    dob = db.Column(db.String)
    profileImg = db.Column(db.String(150))


class Events(db.Model):
    __tablename__ = 'events'
    eventId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, index=True)
    startDate = db.Column(db.String)
    endDate = db.Column(db.String)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String)
    # type = db.Column(db.String)
    status = db.Column(db.String)
    price = db.Column(db.Integer)
    ticketNum = db.Column(db.Integer)
    author = db.Column(db.Integer)
    image = db.Column(db.String(60), nullable=False) 
