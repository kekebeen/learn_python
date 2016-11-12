from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#load config csrf protection for wtf forms and secret key
app.config.from_object('config.DevConfig')
#initialize db
db = SQLAlchemy(app)

from app import views, models
