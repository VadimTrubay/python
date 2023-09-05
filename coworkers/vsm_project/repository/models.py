from datetime import datetime
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, ListField, StringField, IntField, URLField
from .connect_db import connect


class User(Document):
    """Модель користувачів"""
    user_id = IntField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    created = DateTimeField(default=datetime.now())
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)


class Procedure(Document):
    """Модель для процедур"""
    title = StringField(max_length=120, required=True)
    image_url = StringField(max_length=120)
    desc_url = StringField(max_length=120)

