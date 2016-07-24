from flask import Flask
import os

app = Flask(__name__)
from app import index
from app import signup

