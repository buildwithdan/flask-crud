import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import load_config

app = Flask(__name__)


# application = app #for the WSGI service
app.config['SQLALCHEMY_DATABASE_URI'] = load_config()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import views


# Create the tables if they don't exist




if __name__ == "__main__": 
    app.run()
# this has got nothing to do with the app.py name. its a way to tell python to only run this file first. It also means that if app.py was being imported into any other file, it wont start automatically.