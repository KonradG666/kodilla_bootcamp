from config import app, db
from datetime import datetime

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(15), nullable=True)
    message = db.Column(db.String(400),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, surname, message):
        self.name = name
        self.surname = surname
        self.message = message