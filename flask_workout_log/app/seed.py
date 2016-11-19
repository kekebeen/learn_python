from flask import Flask
from . import app, db

db.create_all()