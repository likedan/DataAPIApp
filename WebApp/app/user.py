from werkzeug.security import check_password_hash
from app import app, mongo

class User:

    def __init__(self, email=None, user_info=None):
        if user_info != None:
            for key in user_info.keys():
                setattr(self, key, user_info[key])

        if email != None:
            user_info = mongo.db.users.find_one({'email': email})
            if user_info != None:
                print user_info
                for key in user_info.keys():
                    if key != "_id":
                        setattr(self, key, user_info[key])

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def exists(self):
        return hasattr(self, "email")

    def save(self):
        attributes = vars(self)
        print attributes
        mongo.db.users.update(attributes, attributes, upsert=True)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False