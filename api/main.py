from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import createDB,insertData, readData,updateData
from modelsV2 import selectTable, selectTable2

app = Flask(__name__)

#models.py
# createDB()
# insertData()
# readData()
# updateData()


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        bountryTarget = request.form["inputBountyTarget"]
        rowId = request.form["rowID"]
        print(bountryTarget)
        
        
        return redirect(url_for("home"))
    else:
        data = selectTable()
        data2 = selectTable2()
    return render_template("base.html",data=data, data2=data2)

  
# Update route
@app.route('/update', methods=['POST'])
def update_user():
    row_id = request.form['id']
    new_name = request.form['name']
    new_email = request.form['email']

    # Update the user in the database
    user = User.query.get(row_id)
    if row_id:
        user.name = new_name
        user.email = new_email
        db.session.commit()
        return "User updated successfully"
    else:
        return redirect(url_for("base"))


if __name__ == '__main__':
  app.run

