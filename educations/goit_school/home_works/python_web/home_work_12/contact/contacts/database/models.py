from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, func
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
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'),
                     default=None)
    user = relationship('User', backref="contacts")
    information = Column(String, nullable=True)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String, unique=True, index=True)
    password = Column(String(255), nullable=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)


Base.metadata.create_all(engine)
Base.metadata.bind = engine