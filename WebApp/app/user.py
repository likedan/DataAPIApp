from werkzeug.security import generate_password_hash, check_password_hash
from app import app, mongo

class User:

    def __init__(self, email):
        user_info = mongo.db.users.find_one({'email': email})
        if user_info != None:
            print user_info
            self.password_hash = user_info["password_hash"]
            self.email = email
            self.full_name = user_info["full_name"]
            self.is_email_authenticated = user_info["is_email_authenticated"]
            if not self.is_email_authenticated:
                self.email_confirmation_token = user_info["email_confirmation_token"]

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def user_exists(self):
        return hasattr(self, "email")

    def save(self):
        attributes = vars(self)
        print attributes
        mongo.db.users.update(attributes, attributes, upsert=True)
