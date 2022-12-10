import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

path = os.path.abspath('./')+'"\ \"'.replace(" ", "").replace('"', '')

exist_env = os.path.exists(path+'.env')
exist_migrations = os.path.exists(path+"migrations")

get_db_url = os.getenv("DATABASE_URL") if os.getenv("DATABASE_URL") != None else ""
get_db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else ""
get_secret_key = os.getenv("SECRET_KEY") if os.getenv("SECRET_KEY") != None else ""

db = SQLAlchemy()
migrate = Migrate()

try:
    engine = create_engine(get_db_url)
    Session = sessionmaker(engine)
    session = Session()
except:
    engine = None