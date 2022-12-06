import os
from flask import Flask
from routes.home import home
from flask_sqlalchemy import SQLAlchemy

from date import *

app = Flask(__name__)

db_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)


# app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(home)