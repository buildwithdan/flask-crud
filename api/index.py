from flask import Flask, render_template, request, redirect, url_for
# from modelsV2 import selectTable2
# from config import connection2
from flask_sqlalchemy import SQLAlchemy
import configparser

app = Flask(__name__)

# Load configuration from 'config.ini'
config = configparser.ConfigParser()
config.read('configs.ini')

db_uri = f"postgresql://{config.get('database', 'user')}:{config.get('database', 'password')}@{config.get('database', 'host')}:{config.get('database', 'port')}/{config.get('database', 'dbname')}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class bounties3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bounty_target = db.Column(db.String(100))
    bounty_amount = db.Column(db.Integer)
    bounty_hunter = db.Column(db.String(100))
    published_date = db.Column(db.DateTime)
    
# this creates the table on first load of the page. 
# If the table already exits it wont add it again.
# @app.before_first_request
# def create_tables(): 
#     db.create_all()
#     print(">>>Table created in DB")

@app.route("/", methods=["POST","GET"])
def home():
     # persistent data 
    if request.method == "POST":
        # formData = postDataCheck()
        # print(formData)
        submit_data()
       
        # print("using Home()")
    data2 = bounties3.query.all()
    return render_template("base.html", data2=data2)


def postDataCheck():
    bounty_id = request.form["id"]
    bounty_target = request.form["bounty_target"]
    bounty_amount = request.form["bounty_amount"]
    bounty_hunter = request.form["bounty_hunter"]
    published_date = request.form["published_date"] 
    
    formData = (bounty_id, bounty_target, bounty_amount, bounty_hunter, published_date)
    print(formData)
    return formData

def submit_data():  
    if request.method == "POST":
        bounty_id = request.form["id"]
        bounty_target = request.form["bounty_target"]
        bounty_amount = request.form["bounty_amount"]
        bounty_hunter = request.form["bounty_hunter"]
        published_date = request.form["published_date"]

        bounty = bounties3.query.get(bounty_id)
        if bounty:
            bounty.bounty_target = bounty_target
            bounty.bounty_amount = int(bounty_amount)
            bounty.bounty_hunter = bounty_hunter
            bounty.published_date = published_date
        else:
            bounty = bounties3(
                id=bounty_id,
                bounty_target=bounty_target,
                bounty_amount=int(bounty_amount),
                bounty_hunter=bounty_hunter,
                published_date=published_date,
            )
        db.session.add(bounty)
        db.session.commit()
        # print(bounty)
        return redirect(url_for("home"))  
   