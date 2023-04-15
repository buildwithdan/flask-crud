import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import load_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = load_config()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import views

# Create the tables if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()

# if __name__ == "__main__":
#     app.run()
