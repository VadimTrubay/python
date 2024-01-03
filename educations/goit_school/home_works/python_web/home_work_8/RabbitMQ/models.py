from mongoengine import Document, ReferenceField
from mongoengine.fields import StringField, BooleanField


class Contact(Document):
    name = StringField(max_length=60, min_length=5)
    email = StringField(max_length=40, min_length=5)
    is_delivered = BooleanField(default=False)
