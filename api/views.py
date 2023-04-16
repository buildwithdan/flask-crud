from flask import render_template, request, redirect, url_for
from app import app, db
from models import Bounties


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET','POST',])
def home():
    data2 = Bounties.query.all()
    
    if request.method == "POST":
        submit_data()
    
    return render_template("base.html", data2=data2)

def submit_data():
    bounty_id = request.form["id"]
    bounty_target = request.form["bounty_target"]
    bounty_amount = request.form["bounty_amount"]
    bounty_hunter = request.form["bounty_hunter"]
    published_date = request.form["published_date"]
    
    bounty = Bounties.query.get(bounty_id)
    if bounty:
        bounty.bounty_target = bounty_target
        bounty.bounty_amount = int(bounty_amount)
        bounty.bounty_hunter = bounty_hunter
        bounty.published_date = published_date
    else:
        bounty = Bounties(
            id=bounty_id,
            bounty_target=bounty_target,
            bounty_amount=int(bounty_amount),
            bounty_hunter=bounty_hunter,
            published_date=published_date,
        )
    db.session.add(bounty)
    db.session.commit()
    return redirect(url_for("home"))

