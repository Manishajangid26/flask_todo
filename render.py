from flask import render_template,Flask

# @app.route('/hello/')
app = Flask(__name__)
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html')

@app.route('/world/<user>')
def world(user):
    return render_template('world.html', name = user)