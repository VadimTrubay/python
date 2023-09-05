import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from goit_web_hw13.conf.config import settings

# file_config = pathlib.Path(__file__).parent.parent.joinpath('config/config.ini')
# config = configparser.ConfigParser()
# config.read(file_config)

# username = config.get('DEV', 'USER')
# password = config.get('DEV', 'PASSWORD')
# domain = config.get('DEV', 'DOMAIN')
# port = config.get('DEV', 'PORT')
# db_name = config.get('DEV', 'DB_NAME')

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
