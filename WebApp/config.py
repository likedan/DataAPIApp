import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# authentication
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SECRET_KEY_EMAIL_AUTHENTICATION = 'my_precious_two'

# email
MAIL_SERVER = 'smtp.gmail.com:587'
MAIL_USERNAME = 'likedan5@gmail.com'
MAIL_PASSWORD = '15889431247'

# names
APP_NAME = "TraData"
