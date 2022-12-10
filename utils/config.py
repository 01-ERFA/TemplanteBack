import os
from flask import Flask
from flask_cors import CORS
from routes.site import site
from utils.setup import db, migrate, get_db_url, get_secret_key

app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config['SECRET_KEY'] = get_secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

CORS(app)

app.register_blueprint(site)
# app.register_blueprint(api, url_prefix='/api')