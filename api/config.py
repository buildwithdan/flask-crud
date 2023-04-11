import configparser
from sqlalchemy import create_engine

# Read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the PostgreSQL settings from the config.ini file
pg_settings = config['database']
host = pg_settings['host']
port = pg_settings['port']
dbname = pg_settings['dbname']
user = pg_settings['user']
password = pg_settings['password']

# Create the connection string for the PostgreSQL database
# different backend can be found here = https://docs.sqlalchemy.org/en/20/core/engines.html
connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)