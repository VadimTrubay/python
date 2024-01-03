from sqlalchemy import Column, Integer, String, DateTime, Date, func
from sqlalchemy.orm import relationship, declarative_base

from contacts.database.db import engine

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False, index=True)
    last_name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, nullable=False)
    birthday = Column(Date, nullable=False)
    information = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


Base.metadata.create_all(engine)
Base.metadata.bind = engine