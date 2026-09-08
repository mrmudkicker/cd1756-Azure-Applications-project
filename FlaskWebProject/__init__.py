"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
app.logger.setLevel(logging.INFO)
for handler in app.logger.handlers:
	handler.setFormatter(logging.Formatter(
		'%(asctime)s %(levelname)s %(name)s: %(message)s'
	))
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
