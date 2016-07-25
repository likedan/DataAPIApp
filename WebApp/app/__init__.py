from flask import Flask
from flask_pymongo import PyMongo

import os

app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)
from app import index
from app import signup

