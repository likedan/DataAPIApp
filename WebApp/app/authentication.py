from app import app
from itsdangerous import URLSafeTimedSerializer
from user import User
from flask import session

class AuthenticationManager:

    def __init__(self):
        pass

    def is_authenticated(self):
        if "user" in session and User(user_info=session["user"]).is_authenticated():
            return True
        else:
            return False

    def authenticate_user_with_email_password(self, email, password_hash):
        print "authenticate_user_with_email_password"
        auth_user = User(email=email)
        print email
        if auth_user.exists() and auth_user.password_hash == password_hash:
            session["user"] = vars(auth_user)
            return True
        else:
            return False

    def generate_confirmation_token(self, email):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return serializer.dumps(email, salt=app.config['SECRET_KEY_EMAIL_AUTHENTICATION'])

    def confirm_token(self, token, expiration=86400):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            email = serializer.loads(
                token,
                salt=app.config['SECRET_KEY_EMAIL_AUTHENTICATION'],
                max_age=expiration
            )
        except:
            return False
        return email

