from flask import render_template, request, redirect
from app import app, auth_manager
from user import User
from flask_wtf import Form

@app.route('/email_confirmation_form', methods=['GET'])

def email_confirmation():
    print request
    print request.form["email"]
    print request.form["token"]
    error_list = []

    return redirect("/index")
    # if form.validate():
    #     user = User(form.email.data)
    #     if user.user_exists() and auth_manager.authenticate_user_with_password(user, form.password.data):
    #         return redirect("/index", code=302)
    #     else:
    #         error_list.append("Email and Passord doesn't match.")
    # else:
    #     for key in form.errors.keys():
    #         error_list.append(key+": "+form.errors[key][0])
    # #only displaying one error for now.                     
    # return render_template("login.html", form=form, error=error_list[0])