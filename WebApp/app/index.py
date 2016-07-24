from flask import render_template
from app import app

@app.route('/')
@app.route('/index')


def index():
    title = "Trading Data"
    subtitles = ["Stocks & Currencys data for developing trading algorithms.", "FREE historical data and reatime API available!"]
    return render_template("index.html", title=title, subtitles=subtitles)