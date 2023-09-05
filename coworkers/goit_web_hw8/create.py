import json

from mongoengine import disconnect

from models import Author, Quote


def load_json_author(file):
    with open(file, 'r', encoding='utf-8') as f:
        authors = json.load(f)
        for atr in authors:
            author = Author(
                fullname=atr['fullname'],
                born_date=atr['born_date'],
                born_location=atr['born_location'],
                description=atr['description']
            ).save()


def load_json_quote(file):
    with open(file, 'r', encoding='utf-8') as f:
        quotes = json.load(f)        
        for qt in quotes:
            quote_author = Author.objects(fullname=qt["author"])    
            quote = Quote(
                author=quote_author[0],
                tags=qt['tags'],
                content=qt['quote']
            ).save()

if __name__ == '__main__':
    load_json_author('authors.json')
    load_json_quote('quotes.json')

    disconnect()
