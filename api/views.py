from flask import render_template, request, redirect, url_for, flash
from api.app import app, db
from api.models import Bounties
from sqlalchemy import desc

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET'])
def home():    
    # all_bounties = Bounties.query.all()
    
    sort_all_bounties = Bounties.query.order_by(desc(Bounties.bounty_amount)).all()
    
    for row in sort_all_bounties:
        row.formatted_bounty_amount = "{:,.0f}".format(row.bounty_amount)
      
    return render_template("base.html", data2=sort_all_bounties)

@app.route('/edit', methods=['POST'])
def edit_bounty():
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
    flash('Bounty edit saved')
    
    return redirect(url_for("home"))



@app.route('/add', methods=['POST'])
def add_bounty():
    # bounty_id = request.form["id"]
    bounty_target = request.form["bounty_target"]
    bounty_amount = request.form["bounty_amount"]
    bounty_hunter = request.form["bounty_hunter"]
    published_date = request.form["published_date"]
    
    bounty = Bounties(
            # id=bounty_id,
            bounty_target=bounty_target,
            bounty_amount=int(bounty_amount),
            bounty_hunter=bounty_hunter,
            published_date=published_date,
        )
    db.session.add(bounty)
    db.session.commit()
    flash('New Bounty added')
    return redirect(url_for("home"))


@app.route('/delete_bounty/<int:id>', methods=['POST'])
def delete_bounty(id):
    bounty = Bounties.query.get_or_404(id)
    db.session.delete(bounty)
    db.session.commit()
    flash('Bounty was deleted')
    return redirect(url_for('home'))
