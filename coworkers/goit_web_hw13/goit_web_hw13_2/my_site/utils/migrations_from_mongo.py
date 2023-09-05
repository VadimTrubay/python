import os
import django

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

from quotes.models import Quote, Tag, Author  # noqa
from quotes.utils import get_mongodb

db = get_mongodb()

authors = db.author.find()

for a in authors:
    Author.objects.get_or_create(
        fullname=a['fullname'],
        born_date=a['born_date'],
        born_location=a['born_location'],
        description=a['description']
    )

quotes = db.quote.find()

for q in quotes:
    tags = []
    for tag in q['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=q['content'])))

    if not exist_quote:
        author = db.author.find_one({'_id': q['author']})
        
        a = Author.objects.get(fullname=author['fullname'])
        qu = Quote.objects.create(
            quote=q['content'],
            author=a
        )
        for tag in tags:
            qu.tags.add(tag)