from flask import render_template, request, redirect
from app import app, auth_manager
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.security import generate_password_hash
from user import User
import config
import message

class SignUpForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    full_name = StringField('full_name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/signup', methods=['GET'])

def signup():
    if auth_manager.is_authenticated():
        return redirect("/index", code=302)
    form = SignUpForm()
    return render_template("signup.html", form=form, app_name=config.APP_NAME)

@app.route('/signupform', methods=['POST'])
def signupform():

    if auth_manager.is_authenticated():
        return redirect("/index", code=302)
    form = SignUpForm(request.form)
    error_list = []
    if form.validate():
        user = User(form.email.data)
        if user.user_exists():
            error_list.append("This email is associated with another account, please use a different one.")
        else:
            user.set_password(form.password.data)
            user.email = form.email.data
            user.full_name = form.full_name.data
            auth_manager.authenticated_user = user

            token = auth_manager.generate_confirmation_token(user.email)
            user.email_confirmation_token = token
            user.is_email_authenticated = False
            message.send_confirmation_email_for_user(user)

            user.save()
            return redirect("/index", code=302)
    else:
        for key in form.errors.keys():
            error_list.append(key+": "+form.errors[key][0])
    #only displaying one error for now.                     
    return render_template("signup.html", form=form, error=error_list[0], app_name=config.APP_NAME)