from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

# Flask and Flask-SQLAlchemy initialization here


#Import for flask login
from flask_login import LoginManager
# Create flask app variable
app = Flask(__name__)
app.config.from_object(Config)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# admin.add_view(ModelView(User, db.session))

login = LoginManager(app)
login.login_view = 'login' # Specify what page to load for NON-authenticated Users


from venv import routes,models