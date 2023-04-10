import sqlite3

connection = sqlite3.connect("starWars.db")
cursor = connection.cursor()
# this is to do operations

def createDB():
  command = "CREATE TABLE IF NOT EXISTS bounties3(name TEXT, value INTEGER, published_date TEXT)"
  cursor.execute(command)
  print("DB created")
  

def insertData():
  command = "INSERT INTO bounties3 VALUES ('Danie','999000', '2023-04-10')"
  cursor.execute(command)
  connection.commit()
  print("Data inserted into Table")
  
 
if __name__ == '__main__':
  createDB()
  insertData()
  
