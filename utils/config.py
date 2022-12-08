import os
from flask import Flask
from routes.home import home
from utils.utils import db
from flask_cors import CORS

from utils.utils import migrate

app = Flask(__name__, template_folder="../templates")

db_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

CORS(app)

# app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(home)