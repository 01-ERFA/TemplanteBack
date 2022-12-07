from utils.db import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(engine)
session = Session()