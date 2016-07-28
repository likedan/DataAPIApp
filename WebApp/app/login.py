from flask import render_template, request, redirect
from app import app, auth_manager
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from user import User
import config

class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/login', methods=['GET'])

def login():
    form = LoginForm()
    if auth_manager.is_authenticated():
        return redirect("/index", code=302)
    else:
        return render_template("login.html", form=form, app_name=config.APP_NAME)

@app.route('/loginform', methods=['POST'])

def loginform():

    if auth_manager.is_authenticated():
        return redirect("/index", code=302)
    form = LoginForm(request.form)
    error_list = []
    if form.validate():
        user = User(form.email.data)
        if user.user_exists() and auth_manager.authenticate_user_with_password(user, form.password.data):
            return redirect("/index", code=302)
        else:
            error_list.append("Email and Passord doesn't match.")
    else:
        for key in form.errors.keys():
            error_list.append(key+": "+form.errors[key][0])
    #only displaying one error for now.                     
    return render_template("login.html", form=form, error=error_list[0], app_name=config.APP_NAME)