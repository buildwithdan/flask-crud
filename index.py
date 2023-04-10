from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("baseLayout.html")


