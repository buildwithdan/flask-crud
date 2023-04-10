from flask import Flask, render_template
from models import createDB,insertData

app = Flask(__name__)

createDB()
insertData()


@app.route("/")
def base():
    return render_template("baseLayout.html")


if __name__ == '__main__':
  app.run

