import os
from sqlalchemy import create_engine
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

engine = create_engine(os.getenv("DATABASE_URL"))

migrate = Migrate()