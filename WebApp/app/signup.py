from flask import render_template
from app import app
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(Form):
    email = StringField('email', validators=[DataRequired(), Email("invalid email address")])
    full_name = StringField('full_name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])

@app.route('/signup', methods=['GET'])

def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print "!!!!"
        # flash('Login requested for OpenID="%s", remember_me=%s' %
        #       (form.openid.data, str(form.remember_me.data)))
        return render_template("index.html")
    print "?????"
    return render_template("signup.html", form=form)