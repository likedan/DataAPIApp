from flask import render_template, url_for, request
from app import app, auth_manager
import config

@app.route('/')
@app.route('/index')

def index():
    title = "Trading Data"
    print request.cookies.get('email')
    if auth_manager.is_authenticated() or auth_manager.authenticate_user_with_email_password(request.cookies.get('email'), request.cookies.get('password')):
        return render_template("index.html", app_name=config.APP_NAME, title=title, has_user = True)
    else:
        return render_template("index.html", app_name=config.APP_NAME, title=title, has_user = False)