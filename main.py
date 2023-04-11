from flask import Flask, render_template
from models import createDB,insertData, readData,updateData
from modelsV2 import selectTable, selectTable2

app = Flask(__name__)

#models.py
# createDB()
# insertData()
# readData()
# updateData()


@app.route("/")
def base():
    data = selectTable()
    data2 = selectTable2()
    return render_template("baseLayout.html",data=data, data2=data2)


if __name__ == '__main__':
  app.run

