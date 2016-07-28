from flask import render_template, request, redirect, session
from app import app, auth_manager
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from user import User
import config
import datetime
expire_date = datetime.datetime.now()
expire_date = expire_date + datetime.timedelta(days=365)

class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/login', methods=['GET'])

def login():

    if auth_manager.is_authenticated() or auth_manager.authenticate_user_with_email_password(request.cookies.get('email'), request.cookies.get('password')):
        return redirect("/index", code=302)
    form = LoginForm()
    return render_template("login.html", form=form, app_name=config.APP_NAME)

@app.route('/loginform', methods=['POST'])

def loginform():

    if auth_manager.is_authenticated() or auth_manager.authenticate_user_with_email_password(request.cookies.get('email'), request.cookies.get('password')):
        return redirect("/index", code=302)

    form = LoginForm(request.form)
    error_list = []
    if form.validate():
        user = User(email=form.email.data)
        if user.exists() and user.verify_password(form.password.data):
            redirect_to_index = redirect('/index', code=302)
            response = app.make_response(redirect_to_index)  
            response.set_cookie('email', user.email, expires=expire_date)
            response.set_cookie('password', user.password_hash, expires=expire_date)
            session["user"] = vars(user)
            return response
        else:
            error_list.append("Email and Passord doesn't match.")
    else:
        for key in form.errors.keys():
            error_list.append(key+": "+form.errors[key][0])
    #only displaying one error for now.                     
    return render_template("login.html", form=form, error=error_list[0], app_name=config.APP_NAME)