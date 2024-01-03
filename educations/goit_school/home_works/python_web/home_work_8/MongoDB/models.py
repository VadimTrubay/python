from mongoengine import Document, ReferenceField
from mongoengine.fields import StringField, ListField


class Authors(Document):
    fullname = StringField(max_length=60)
    born_date = StringField(max_length=60)
    born_location = StringField(max_length=60)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=60))
    author = ReferenceField(Authors)
    quote = StringField(max_length=1500, required=True)
