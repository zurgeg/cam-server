from datetime import datetime

from cam import db


class Orders(db.Model):
    order_id = db.Column(db.String(14), primary_key=True, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    email = db.Column(db.String(127))
    order_schema = db.Column(db.UnicodeText())
    filepath = db.Column(db.String())
    wiilink24_id = db.Column(db.Integer())
    
