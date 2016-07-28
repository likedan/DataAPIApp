from flask import render_template, request, redirect
from app import app
from user import User
from flask_wtf import Form
import config

@app.route('/email_confirmation_form', methods=['GET'])

def email_confirmation_form():
    token = request.args.get('token')   
    verified_email = auth_manager.confirm_token(token)
    if verified_email == False :
        return redirect("/index")
    else:
        return render_template("email_confirmation.html", email=verified_email, app_name=config.APP_NAME)

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
