from flask import render_template,Flask
from data import data_dict

app = Flask(__name__)

@app.route("/id")
def id():
    return render_template("id.html",data = data_dict)

@app.route("/username")
def user():
    return render_template("user.html",data = data_dict)


@app.route("/email")
def email():
    return render_template("email.html",data = data_dict)


@app.route("/details")
def detail():
    return render_template("table.html",data = data_dict)    