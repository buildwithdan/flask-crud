import configparser
import psycopg2
from contextlib import closing
from config import engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class Bounty(Base):
#     __tablename__ = 'bounty'
#     id = Column(Integer, primary_key=True)
#     bounty_target = Column(String)
#     bounty_amount = Column(Integer)
#     bounty_hunter = Column(String)
#     published_date = Column(DateTime)

# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()





def selectTable2():
    # Define query
    query = "SELECT * FROM public.bounties3 ORDER BY bounty_amount DESC"

    # Read the SQL query into a pandas DataFrame using the SQLAlchemy engine
    df = pd.read_sql_query(query, engine)

    # html_table = df.to_html(index=False, classes="my-table")
    
    # Return the DataFrame
    
    # Print the DataFrame
    # print(df)
    return df

def updateData():
    # Define query
    
    row = printUpdateDB.rowID
    print("updateData",row)
    # query = "SELECT * FROM public.bounties3 ORDER BY bounty_amount DESC"
    

    # # Read the SQL query into a pandas DataFrame using the SQLAlchemy engine
    # df = pd.read_sql_query(query, engine)

    # # html_table = df.to_html(index=False, classes="my-table")
    
    # # Return the DataFrame
    
    # # Print the DataFrame
    # # print(df)
    return row


if __name__ == '__main__':
    selectTable()




# # Initialize the ConfigParser
# config = configparser.ConfigParser()

# # Read the config.ini file
# config.read('config.ini')

# # Get the connection details from the 'database' section
# dbname = config.get('database', 'dbname')
# user = config.get('database', 'user')
# password = config.get('database', 'password')
# host = config.get('database', 'host')
# port = config.get('database', 'port')


# # def get_db_connection():
# #     connection = psycopg2.connect(
# #         dbname=dbname,
# #         user=user,
# #         password=password,
# #         host=host,
# #         port=port
# #     )
# #     cursor = connection.cursor()
    
# #     return connection, cursor
# #     # this is in a tuple 0 and 1
# #     # if you want to call these you can use 
# #     #


# # def selectTable2():
# #     with closing(get_db_connection()[0]) as connection:
# #         with connection.cursor() as cursor:
# #             # Define query
# #             query = "SELECT * FROM public.bounties3"

# #             # Execute query
# #             cursor.execute(query)

# #             # Fetch all rows from the result
# #             rows = cursor.fetchall()

# #             print(rows)

# #             # Return the fetched rows
# #             return rows

# def selectTable():
#     # Connect to the database using psycopg2
#     with closing(psycopg2.connect(
#         dbname=dbname,
#         user=user,
#         password=password,
#         host=host,
#         port=port
#     )) as connection:
#         with connection.cursor() as cursor:
#             # Define query
#             query = "SELECT * FROM public.bounties3"

#             # Execute query
#             cursor.execute(query)

#             # Fetch all rows from the result
#             rows = cursor.fetchall()

#             # print(rows)

#             # Return the fetched rows
#             return rows

