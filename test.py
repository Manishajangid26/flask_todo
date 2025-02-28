from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/greet")
def Good():
    return "Good Morning Sir"

# @app.route("/profile/manisha")
# def manisha():
#     return "Hello,Manisha"    


# @app.route("/profile/vipin")
# def vipin():
#     return "Hello,vipin"            





@app.route("/profile/<path:a>")
def path(a):
    return "Hello"  



@app.route("/profile/<user>")
def user_name(user):
    return f"Hello,{user}"


    
  