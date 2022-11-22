from flask import Flask
from os import urandom
from .constant import DATABASE_HOST, DATABASE_NAME, DATABASE_PASS, DATABASE_PROVIDER, DATABASE_USER, SESSION_KEY_LENGTH

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# APP CONFIG #
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Release only
app.config['SQLALCHEMY_DATABASE_URI'] = "%s://%s:%s@%s/%s" % (DATABASE_PROVIDER, DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_NAME)
app.secret_key = urandom(SESSION_KEY_LENGTH)

import core.views