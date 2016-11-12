from flask import Flask

app = Flask(__name__)
#load config csrf protection for wtf forms and secret key
app.config.from_object('config')

from app import views