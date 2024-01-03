from models import Quotes, Authors
import connect


def search_by_author(author_fullname):
    auth = Authors.objects(fullname=author_fullname).first()
    if author:
        quotes = Quotes.objects(author=auth)
        for quote in quotes:
            print(f"{author_fullname}- {quote.quote}")
            print()


def search_by_tag(tag):
    quotes = Quotes.objects(tags=tag)
    for quote in quotes:
        print(f"{tag}- {quote.quote}")
        print()


def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quotes.objects(tags__in=tag_list)
    for quote in quotes:
        print(f"{tags}- {quote.quote}")
        print()


if __name__ == '__main__':
    while True:
        user_input = input('enter command \n(name:<author>, tag:<tag>, tags:<tag1,tag2>, or exit)\n>>>: ')
        first_line = user_input.split(':')
        if first_line[0] == 'name':
            author = first_line[1].strip()
            search_by_author(author)
        elif first_line[0] == 'tag':
            tag = first_line[1].strip()
            search_by_tag(tag)
        elif first_line[0] == 'tags':
            tags = first_line[1].strip()
            search_by_tags(tags)
        elif first_line[0] == 'exit':
            break
        else:
            print("unknown command, try again")

