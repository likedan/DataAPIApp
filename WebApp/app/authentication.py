from app import app, mongo

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

