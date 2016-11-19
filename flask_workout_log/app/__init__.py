from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

__status__ = "Alpha"
__description__ = "Simple workout track system using flask microframework"
__author__ = "Benjamin Babic"
__email__ = "kakosi69@gmail.com"

app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password_hash = db.Column(db.Unicode(50))
    units = db.Column(db.String(3))

class Workout(db.Model):
    int = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.Column(db.Text)

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    order = db.Column(db.Integer, unique = True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class Set(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    order = db.Column(db.Integer, unique = True)
    weight = db.Column(db.Numeric)
    reps = db.Column(db.Integer)

from app import views