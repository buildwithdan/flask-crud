import configparser
import psycopg2
from contextlib import closing

# Initialize the ConfigParser
config = configparser.ConfigParser()

# Read the config.ini file
config.read('config.ini')

# Get the connection details from the 'database' section
dbname = config.get('database', 'dbname')
user = config.get('database', 'user')
password = config.get('database', 'password')
host = config.get('database', 'host')
port = config.get('database', 'port')


def get_db_connection():
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = connection.cursor()
    
    return connection, cursor

