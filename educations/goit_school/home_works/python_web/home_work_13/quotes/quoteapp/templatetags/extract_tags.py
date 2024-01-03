# from django import template
#
# register = template.Library()
#
#
# def tags(quote_tags):
#     return ', '.join([str(name) for name in quote_tags.all()])
#
#
# register.filter('tags', tags)
#
#
# def authors(author_tags):
#     return ', '.join([str(author) for author in author_tags.all()])
#
#
# register.filter('authors', authors)
#
#
# def author_id(authors_id):
#     a = authors_id.all()
#     return str(a)[-3]
#
# register.filter('author_id', author_id)