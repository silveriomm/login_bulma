import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__name__)) 

app.config['SECRET_KEY'] = 'a1c8d3c9fef78b458f2a5312b2ff4966'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.sqlite')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'is_warning'
app.app_context().push()

from flaskblog import routes
