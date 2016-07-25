from flask import render_template, url_for
from app import app, auth_manager

@app.route('/')
@app.route('/index')

def index():
    title = "Trading Data"
    subtitles = ["Stocks & Currencys data for developing trading algorithms.", "FREE historical data and reatime API available!"]

    if auth_manager.is_authenticated():
        return render_template("index.html", title=title, subtitles=subtitles, has_user = True)
    else:
        return render_template("index.html", title=title, subtitles=subtitles, has_user = False)