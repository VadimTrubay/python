from mongoengine import connect
from mongoengine import EmbeddedDocument, Document, ReferenceField
from mongoengine.fields import BooleanField, DateTimeField,EmbeddedDocumentField, ListField,StringField

connect(host="mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/module8?retryWrites=true&w=majority")

class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {"allow_inheritance": True}
    

class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors)
    quote = StringField()
    meta = {"allow_inheritance": True}

























