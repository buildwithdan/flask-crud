import sqlite3

#SQLite Setup
connection = sqlite3.connect("starWars.db")
cursor = connection.cursor()
# this is to do operations

#local db sqllite file 
def createDB():
  command = "CREATE TABLE IF NOT EXISTS bounties3(name TEXT, value INTEGER, published_date TEXT)"
  cursor.execute(command)
  print("DB created") 

def insertData():
  command = "INSERT INTO bounties3 VALUES ('Danie','999000', '2023-04-10')"
  cursor.execute(command)
  connection.commit()
  print("Data inserted into Table")
  

def readData():
  cursor.execute("SELECT * FROM bounties3")
  results = cursor.fetchall()
  print(results)
  
def updateData():
  cursor.execute("UPDATE bounties3 SET value = 895000")
  connection.commit()
  print("Data has been updated/modified")
 
if __name__ == '__main__':
  createDB()
  insertData()
  
