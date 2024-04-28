from sqlalchemy import create_engine, Column, Integer, String, Date, func, text, exc, Engine
from sqlalchemy.orm import sessionmaker, declarative_base
from api.config import db_host, db_name, db_password, db_port, db_schema, db_username
from sqlalchemy.engine import URL
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Database models
Base = declarative_base()

class Bounties(Base):
    __tablename__ = 'bounties'
    __table_args__ = {'schema': db_schema}
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    bounty_target = Column(String(100))
    bounty_amount = Column(Integer)
    bounty_hunter = Column(String(100))
    published_date = Column(Date)
    last_updated = Column(Date, default=func.now())
    
class Counter(Base):
    __tablename__ = 'counter'
    __table_args__ = {'schema': db_schema}
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    count = Column(Integer, default=0)
    last_updated = Column(Date, default=func.now())

# def get_engine_db(bulk: bool=True) -> Engine:
#     con_str = URL.create(
#         "mssql+pyodbc",
#         username=db_username,
#         password=db_password,
#         host=db_host,
#         database=db_name,
#         port=db_port,
#         query={"driver": 'ODBC Driver 17 for SQL Server', "LongAsMax": "Yes"}
#     )
#     return create_engine(con_str, fast_executemany=bulk, echo=True)

def get_engine_db(bulk: bool=True) -> Engine:
    con_str = URL.create(
        "postgresql+psycopg2",  # Database dialect and driver
        username=db_username,    # Database username
        password=db_password,    # Database password
        host=db_host,              # Use the Docker service name as the host
        database=db_name,    # Database name
        port=db_port            # Default PostgreSQL port
    )
    return create_engine(con_str, echo=True)


engine = get_engine_db()



def create_schema(engine, db_schema):
    with engine.connect() as connection:
        # Begin a new transaction
        trans = connection.begin()
        try:
            # Execute the SQL command to create schema if it does not exist
            connection.execute(
                text(f"CREATE SCHEMA IF NOT EXISTS {db_schema};")
            )
            # Commit the transaction
            trans.commit()
        except Exception as e:
            # If an error occurs, rollback the transaction
            trans.rollback()
            logger.error(f"Error creating schema {db_schema}: {str(e)}")
            raise



def create_all_tables():
    try:
        Base.metadata.create_all(engine)
        logger.info("All tables created successfully.")
    except exc.SQLAlchemyError as e:
        logger.error("Failed to create tables", exc_info=True)
        raise


def setup_db():
    create_schema(engine, db_schema)
    create_all_tables()    # Create tables

if __name__ == "__main__":
    logger.info("Starting database setup.")
    try:
        setup_db()
    except Exception as e:
        logger.error("Database setup process failed", exc_info=True)
