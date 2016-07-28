from app import app, mongo
from itsdangerous import URLSafeTimedSerializer
from user import User
from flask import session

class AuthenticationManager:

    def __init__(self):
        pass

    def is_authenticated(self):
        if "user" in session and User(session["user"]["email"], user_info=session["user"]).is_authenticated():
            return True
        else:
            return False

    def authenticate_user_with_email_password(self, email, password_hash):
        auth_user = User(email)
        if auth_user != None and auth_user.password_hash == password_hash:
            session_token = self.generate_user_session_token(email)
            self.authenticated_user[session_token] = auth_user
            return session_token
        else:
            return False

    def authenticate_user_with_session_token(self, session_token):
        return self.confirm_token(session_token, expiration=3600) != False

    def generate_user_session_token(self, email):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return serializer.dumps(email, salt=app.config['SECRET_KEY_USER_SESSION'])

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

