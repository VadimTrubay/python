from models import Authors, Quotes
import connect
import json


def load_quote_to_database(file_path):
    with open(file_path, encoding='UTF-8') as file:
        data = json.load(file)
        for item in data:
            author_name = item['author']
            author = Authors.objects(fullname=author_name).first()
            if not author:
                author = Authors(fullname=author_name)
                author.save()

            quote = Quotes(author=author, quote=item['quote'], tags=item['tags'])
            quote.save()


def load_author_to_database(file_path):
    with open(file_path, encoding='UTF-8') as file:
        data = json.load(file)
        for item in data:
            document = Authors(**item)
            document.save()


if __name__ == '__main__':

    load_author_to_database('authors.json')
    load_quote_to_database('quotes.json')
    print('Loading successfully')

