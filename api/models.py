from index import db

class Bounties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bounty_target = db.Column(db.String(100))
    bounty_amount = db.Column(db.Integer)
    bounty_hunter = db.Column(db.String(100))
    published_date = db.Column(db.Date)
