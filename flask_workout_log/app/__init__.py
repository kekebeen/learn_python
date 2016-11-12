from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

__status__ = "Alpha"
__description__ = "Simple workout track system using flask microframework"
__author__ = "Benjamin Babic"
__email__ = "kakosi69@gmail.com"

app = Flask(__name__)

from app import views, models
