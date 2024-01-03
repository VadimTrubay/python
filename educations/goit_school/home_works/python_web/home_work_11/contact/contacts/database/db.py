from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL = "postgresql+psycopg2://postgres:password@localhost/postgres"
engine = create_engine(URL, echo=True, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
