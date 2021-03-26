"""
This module will initialize the application object.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config
app = Flask(__name__)
bootstrap = Bootstrap(app)
# Apply the configurations on the app object. 
app.config.from_object(Config)
# create the database object.
db = SQLAlchemy(app)
# apply migrations for the database in case of database change.
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# imports at the end to avoid circular dependencies.
from app import routes, models
