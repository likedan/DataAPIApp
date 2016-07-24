from flask import render_template
from app import app

@app.route('/signup', methods=['GET', 'POST'])

def signup():
    print "event"
    return render_template("signup.html")