from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from api.models import engine, setup_db

app = Flask(__name__)
app.secret_key = 'eym7UHZrRpJg2Naj46zXDxUQ9'

# # Configure session for use with Flask
db_session = scoped_session(sessionmaker(bind=engine))

# Setup DB
setup_db()

# {CRITICAL} delay import as the app first needs to be configured before doing the import. This was an annoying issue but works when here.
from api.views import *


@app.teardown_appcontext
def cleanup(resp_or_exc):
    db_session.remove()

  # Ensure your views are using db_session or db as needed

if __name__ == "__main__":
    app.run(debug=True)