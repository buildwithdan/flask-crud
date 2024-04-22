from flask import render_template, request, redirect, url_for, flash
from app import app
from faker import Faker
from models import *
from sqlalchemy import desc
from app import db_session

# from api.counter import increment_and_get_counter

# @app.before_first_request
# def start_db():
#     setup_db()

@app.route('/', methods=['GET'])   
def home():    
    all_bounties = db_session.query(Bounties).all()
    
    sort_all_bounties = db_session.query(Bounties).order_by(desc(Bounties.bounty_amount)).all()
    
    for row in sort_all_bounties:
        row.formatted_bounty_amount = "{:,.0f}".format(row.bounty_amount)

    return render_template("base.html", data2=sort_all_bounties)



@app.route('/edit', methods=['POST'])
def edit_bounty():
    # Retrieve and debug print form data
    bounty_id = request.form["id"]
    bounty_target = request.form["bounty_target"]
    bounty_amount = request.form["bounty_amount"]
    bounty_hunter = request.form["bounty_hunter"]
    published_date = request.form["published_date"]

    print(f"Debug: ID - {bounty_id}, Target - {bounty_target}, Amount - {bounty_amount}, Hunter - {bounty_hunter}, Date - {published_date}")

    # Query for the existing bounty using the ID
    bounty = db_session.query(Bounties).filter(Bounties.id == bounty_id).first()
    print(bounty)

    if bounty:
        print("Debug: Bounty found, updating...")
        # Update the existing bounty
        bounty.bounty_target = bounty_target
        bounty.bounty_amount = bounty_amount
        bounty.bounty_hunter = bounty_hunter
        bounty.published_date = published_date
        db_session.commit()
        flash('Bounty edit saved')
    else:
        print("Debug: No bounty found with the ID.")
        flash('No existing bounty found with the provided ID.')

    return redirect(url_for("home"))




@app.route('/add', methods=['POST'])
def add_bounty():
    session = Session()  # Create a new session instance
    try:
        bounty_target = request.form["bounty_target"]
        bounty_amount = request.form["bounty_amount"]
        bounty_hunter = request.form["bounty_hunter"]
        published_date = request.form["published_date"]

        bounty = Bounties(
            bounty_target=bounty_target,
            bounty_amount=int(bounty_amount),
            bounty_hunter=bounty_hunter,
            published_date=published_date,
        )
        session.add(bounty)
        session.commit()
        flash('New Bounty added')
    except Exception as e:
        session.rollback()
        flash('Failed to add bounty')
        logger.error("Error adding bounty", exc_info=True)
    finally:
        session.close()  # Close the session
    return redirect(url_for("home"))


@app.route('/delete_bounty/<string:id>', methods=['POST'])
def delete_bounty(id):
    bounty = Bounties.query.get_or_404(id)
    db.session.delete(bounty)
    db.session.commit()
    flash('Bounty was deleted')
    return redirect(url_for('home'))

@app.route('/add_fake_data', methods=['POST'])
def add_fake_data():
    fake = Faker()

    for _ in range(5):
        fake_bounty = Bounties(
            bounty_target=fake.name(),
            bounty_amount=int(fake.random_number(digits=4)),  # to generate a random number
            bounty_hunter=fake.name(),
            published_date=fake.date_between(start_date='-1y', end_date='today')
        )
        db.session.add(fake_bounty)

    db.session.commit()

    flash('5 fake bounties added successfully')
    return redirect(url_for("home"))
