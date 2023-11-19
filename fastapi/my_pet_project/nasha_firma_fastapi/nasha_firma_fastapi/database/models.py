from sqlalchemy import (func, Column, Integer, String,
                      Float, Boolean, Enum)
import enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship

from nasha_firma_fastapi.database.db import engine

Base = declarative_base()

class Role(enum.Enum):
    admin: str = 'admin'
    user: str = 'user'


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    price = Column(Float(), default=0, nullable=False)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column('created_at', DateTime, default=func.now())
    done = Column(Boolean, default=False)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), default=None)
    products_id = Column(ForeignKey('orderitems.id', ondelete='CASCADE'), default=None)
    user = relationship('User', backref="orders")
    products = relationship('OrderItem', backref="orders")


class OrderItem(Base):
    __tablename__ = "orderitems"
    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float, nullable=True, default=0)
    note = Column(String, nullable=True)
    order_id = Column(ForeignKey('orders.id', ondelete='CASCADE'), default=None)
    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), default=None)
    product = relationship('Product', backref="orderitems")
    order = relationship('Order', backref="orderitems")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    refresh_token = Column(String(255), nullable=True)
    password_reset_token = Column(String(255), nullable=True)
    avatar = Column(String(255), nullable=True)
    roles = Column('roles', Enum(Role), default=Role.user)
    confirmed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    api_key = Column(String(100), nullable=True)

Base.metadata.create_all(engine)
Base.metadata.bind = engine
