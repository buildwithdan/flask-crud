from flask import render_template, request, redirect, url_for, flash
from faker import Faker
from api.models import Bounties
from sqlalchemy import desc
from api.app import app
from api.app import db_session

# from api.counter import increment_and_get_counter

@app.route('/', methods=['GET'])   
def home():    
    sorted_bounties = db_session.query(Bounties).order_by(desc(Bounties.bounty_amount)).all()

    total_bounties = db_session.query(Bounties).count()

    for bounty in sorted_bounties:
        bounty.formatted_bounty_amount = "{:,.0f}".format(bounty.bounty_amount)

    return render_template("base.html", tbl_Data=sorted_bounties, tbl_count=total_bounties)



@app.route('/edit', methods=['POST'])
def edit_bounty():
    # Retrieve and debug print form data
    # all the below from request, comes from the input fields NAMES and NOT ID names.
    bounty_id = request.form["id"]
    bounty_target = request.form["bounty_target"]
    bounty_amount = request.form["bounty_amount"]
    bounty_hunter = request.form["bounty_hunter"]
    published_date = request.form["published_date"]

    # Query for the existing bounty using the ID
    bounty = db_session.query(Bounties).filter(Bounties.id == bounty_id).first()

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

    db_session.close()  # Close the session

    return redirect(url_for("home"))


@app.route('/delete_bounty', methods=['POST'])
def delete_bounty():
    bounty_id = request.form["id"]
    print(bounty_id)

    # Query for the bounty using first() to retrieve the instance or None
    bounty = db_session.query(Bounties).filter(Bounties.id == bounty_id).first()

    if bounty is not None:  # Corrected the syntax here
        db_session.delete(bounty)  # Pass the bounty object, not its ID
        db_session.commit()
        flash('Bounty was deleted')
    else:
        print("Debug: Not able to delete")  # Improved debugging message
        flash('Not able to delete provided ID.')
    
    db_session.close()  # Close the session

    return redirect(url_for('home'))


@app.route('/add', methods=['POST'])
def add_bounty():
   
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
        db_session.add(bounty)
        db_session.commit()
        flash('New Bounty added')

    except Exception as e:
        db_session.rollback()
        flash('Failed to add bounty')
        logger.error("Error adding bounty", exc_info=True)
    finally:
        db_session.close()  # Close the session
    return redirect(url_for("home"))


@app.route('/add_fake_data', methods=['POST'])
def add_fake_data():
    fake = Faker()

    for i in range(5):
        fake_bounty = Bounties(
            bounty_target=fake.name(),
            bounty_amount=int(fake.random_number(digits=4)),  # to generate a random number
            bounty_hunter=fake.name(),
            published_date=fake.date_between(start_date='-1y', end_date='today')
        )
        db_session.add(fake_bounty)

    db_session.commit()

    flash('5 fake bounties added successfully')
    return redirect(url_for("home"))


@app.route('/delete_all', methods=['POST'])
def delete_all_bounties():

    try:
        # Execute a bulk delete operation
        num_deleted = db_session.query(Bounties).delete()
        db_session.commit()

        # Flash a message based on the operation success
        if num_deleted > 0:
            flash(f'All Bounties were deleted. Total: {num_deleted}')
        else:
            flash('No Bounties to delete')

    except Exception as e:
        # Log the exception and flash a failure message
        print(f"Exception occurred: {e}")  # Improved debugging message
        flash('Failed to delete Bounties')
        db_session.rollback()

    finally:
        # Always close the session
        db_session.close()

    # Redirect to the home page
    return redirect(url_for('home'))