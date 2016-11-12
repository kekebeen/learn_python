from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    title = "test"
    return render_template("index.html")
