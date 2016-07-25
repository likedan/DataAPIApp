from flask import render_template, request, redirect
from app import app
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.security import generate_password_hash
from user import User


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/login', methods=['GET'])

def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route('/loginform', methods=['POST'])
def loginform():
    form = LoginForm(request.form)
    error_list = []
    if form.validate():
        user = User(form.email.data)
        if user.user_exists() and user.verify_password(form.password.data):
            return redirect("/index", code=302)
        else:
            error_list.append("Email and Passord doesn't match.")
    else:
        for key in form.errors.keys():
            error_list.append(key+": "+form.errors[key][0])
    #only displaying one error for now.                     
    return render_template("login.html", form=form, error=error_list[0])