from flask import render_template, url_for
from app import app, auth_manager
import config

@app.route('/')
@app.route('/index')

def index():
    title = "Trading Data"

    if auth_manager.is_authenticated():
        subtitles = ["", ""]
        return render_template("index.html", app_name=config.APP_NAME, title=title, has_user = True)
    else:
        subtitles = ["Stocks & Currencys data for developing trading algorithms.", '<a href="'+url_for("signup")+'">Sign Up</a> for FREE historical data and reatime API!']
        return render_template("index.html", app_name=config.APP_NAME, title=title, has_user = False)