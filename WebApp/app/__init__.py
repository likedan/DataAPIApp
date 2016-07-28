from flask import Flask
from flask_pymongo import PyMongo

import os

app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)
from flask_login import LoginManager

lm = LoginManager()
lm.init_app(app)
from user import User

@lm.user_loader
def load_user(email):
    return User(email)

from app import authentication
auth_manager = authentication.AuthenticationManager()
app.auth_manager = auth_manager

from app import index
from app import signup
from app import login
from app import email_confirmation
