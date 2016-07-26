from app import app, mongo
from itsdangerous import URLSafeTimedSerializer

class AuthenticationManager:

    def __init__(self):
        self.authenticated_user = None

    def is_authenticated(self):
        return self.authenticated_user != None

    def authenticate_user_with_password(self, user, password):
        if user.verify_password(password):
            self.authenticated_user = user
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

