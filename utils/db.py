import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

engine = create_engine(os.getenv("DATABASE_URL"))

db = SQLAlchemy()

migrate = Migrate()