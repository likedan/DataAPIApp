from flask import render_template, request
from app import app
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_pymongo import PyMongo

mongo = PyMongo(app)

class SignUpForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    full_name = StringField('full_name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/signup', methods=['GET'])

def signup():
    form = SignUpForm()
    return render_template("signup.html", form=form)

@app.route('/signupform', methods=['POST'])
def signupform():
    form = SignUpForm(request.form)
    print form.validate()
    error_list = []
    print form.errors
    if form.validate():
        if mongo.db.users.find_one({'email': form.email.data}):
            error_list.append("This email is associated with another account, please use a different one.")
        else:
            mongo.db.users.insert({"email": form.email.data, "full_name":form.full_name.data, "password": form.password.data})
            return render_template("index.html")
    else:
        for key in form.errors.keys():
            error_list.append(key+": "+form.errors[key][0])
    #only displaying one error for now.                     
    return render_template("signup.html", form=form, error=error_list[0])