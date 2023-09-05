"""
for mongodb
"""

# # from bson.objectid import ObjectId
# from django import template

# from ..utils import get_mongodb

# from quotes.models import Quote, Tag, Author

# register = template.Library()


# def get_author(id_):
#     db = get_mongodb()
# #    author = db.author.find_one({'_id':ObjectId(id_)})
# #    author = Author.objects.get(id=id_)
#     author = db.author.find_one({'_id':id_})
#     if author: 
#        return author['fullname']
#     else:
#         print(1111111111111)


# register.filter('author', get_author)