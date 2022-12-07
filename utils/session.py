from utils.utils import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(engine)
session = Session()