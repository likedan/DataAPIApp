from flask import Flask
from flask_pymongo import PyMongo

import os

app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)
from app import authentication
auth_manager = authentication.AuthenticationManager()
app.auth_manager = auth_manager

from app import index
from app import signup
from app import login
from app import email_confirmation
