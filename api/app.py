
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.config import load_config

app = Flask(__name__)
app.secret_key = 'eym7UHZrRpJg2Naj46zXDxUQ9'

app.config['SQLALCHEMY_DATABASE_URI'] = load_config()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import api.views