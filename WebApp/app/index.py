from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')

def index():
    title = "Trading Data"
    subtitles = ["Stocks & Currencys data for developing trading algorithms.", "FREE historical data and reatime API available!"]

    if app.auth_manager.authenticated_user == None:
        return render_template("index.html", title=title, subtitles=subtitles, has_user = False)
    else:
        return render_template("index.html", title=title, subtitles=subtitles, has_user = True)