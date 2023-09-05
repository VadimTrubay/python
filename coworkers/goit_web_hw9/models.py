from mongoengine import *

import connect


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=100)
    description = StringField()

class Quote(Document):  
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=80))
    content = StringField()
