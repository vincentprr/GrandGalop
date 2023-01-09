from flask import Flask
from os import urandom
from flask_login import LoginManager
from .constant import DATABASE_HOST, DATABASE_NAME, DATABASE_PASS, DATABASE_PROVIDER, DATABASE_USER, SESSION_KEY_LENGTH
from base64 import b64encode

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# APP CONFIG #
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Release only
app.config['SQLALCHEMY_DATABASE_URI'] = "%s://%s:%s@%s/%s" % (DATABASE_PROVIDER, DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_NAME)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.secret_key = urandom(SESSION_KEY_LENGTH)
login_manager = LoginManager(app)

from .views import *
from ..models.modeles import *