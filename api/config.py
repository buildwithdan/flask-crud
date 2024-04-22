from dotenv import load_dotenv
import os

# # Load the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)


db_host = os.getenv('DB_HOST')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_schema = os.getenv('DB_SCHEMA')
db_port = os.getenv('DB_PORT')
