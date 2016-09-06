
from root import app
from flask import render_template

@app.route('/')
def hello_world():
    return 'Hello World! 321'

@app.route('/index')
def index():
    return render_template('/index.html')
