from mongoengine import Document, ReferenceField
from mongoengine.fields import StringField, ListField


class Authors(Document):
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=500)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Authors)
    quote = StringField(max_length=1500, required=True)
