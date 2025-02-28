from flask import url_for, Flask

myapp = Flask(__name__)

@myapp.route("/")
def home():
    return url_for("home")+url_for("a")+url_for("b")+url_for("profile",user = 'neha')
    # return url_for("a")
    # return url_for("b")
    # return url_for("profile",user = 'neha')

@myapp.route("/abc")
def a():
    return "this is a abs"

@myapp.route("/xyz")
def b():
    return url_for("profile",user = 'manisha')

@myapp.route("/profile/<user>")
def profile(user):
    return f"hrllo {user}"