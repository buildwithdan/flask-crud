from api.app import db
from datetime import datetime

class Bounties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bounty_target = db.Column(db.String(100))
    bounty_amount = db.Column(db.Integer)
    bounty_hunter = db.Column(db.String(100))
    published_date = db.Column(db.Date)
    
    
class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
