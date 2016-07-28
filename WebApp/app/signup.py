from flask import render_template, request, redirect, session
from app import app, mongo, auth_manager
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.security import generate_password_hash
from user import User
import config
import message
from flask_login import login_user
from flask import session

class SignUpForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    full_name = StringField('full_name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/signup', methods=['GET'])

def signup():
    if auth_manager.is_authenticated():
        return redirect("/index", code=302)

    # user_email = request.cookies.get('email')
    # user_password = request.cookies.get('password_hash')
    # token = auth_manager.authenticate_user_with_email_password(user_email, user_password):

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
        if user.exists():
            error_list.append("This email is associated with another account, please use a different one.")
        else:
            user.password_hash = generate_password_hash(form.password.data)
            user.email = form.email.data
            user.full_name = form.full_name.data

            token = auth_manager.generate_confirmation_token(user.email)
            user.email_confirmation_token = token
            user.is_email_authenticated = False
            message.send_confirmation_email_for_user(user)
            user.save()
            login_user(user, remember=True)
            session["user"] = vars(user)
            return redirect("/index", code=302)
    else:
        for key in form.errors.keys():
            error_list.append(key+": "+form.errors[key][0])
    #only displaying one error for now.                     
    return render_template("signup.html", form=form, error=error_list[0], app_name=config.APP_NAME)