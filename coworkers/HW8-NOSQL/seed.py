from models import *
import pprint
import json



def seed_authors():
    with open("authors.json") as file:
        authors = json.load(file)

    for i in authors:
        author = Authors(
            fullname = i["fullname"],
            born_date = i["born_date"],
            born_location = i["born_location"],
            description = i["description"]
            )
        author.save()

def seed_quotes():
    with open("quotes.json", encoding="utf8") as file:
        quotes = json.load(file)
    for i in quotes:
        auth = Authors.objects(fullname = i["author"]).first()
        quote = Quotes(
            tags = i["tags"],
            author = auth,
            quote = i["quote"]
            )
        quote.save()


if __name__ == "__main__":
    seed_authors()
    seed_quotes()



