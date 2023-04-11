from flask import Flask, render_template
from models import createDB,insertData, readData,updateData
from modelsV2 import selectTable

app = Flask(__name__)

#models.py
# createDB()
# insertData()
# readData()
# updateData()


@app.route("/")
def base():
    data = selectTable()
    return render_template("baseLayout.html",data=data)


if __name__ == '__main__':
  app.run

