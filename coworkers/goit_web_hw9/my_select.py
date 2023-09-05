from models import Author, Quote
from redis_cache import cache


@cache
def by_author(author: str):
    """
    пошук цитат за ім'ям автора
    Search for quotes by author name
    """
    author_id = Author.objects(fullname__istartswith=author).first().id
    name = Author.objects(fullname__istartswith=author).first().fullname
    quotes = Quote.objects(author=author_id)
    return quotes, name


@cache
def by_tag(tag: str):
    """
    пошук цитат за тегом
    Search for quotes by tag
    """
    quotes = Quote.objects(tags__istartswith=tag)
    return quotes


@cache
def by_tags(tags_list: list):
    """
    пошук цитат за набором тегів
    Search for quotes by a set of tags
    """
    quotes = Quote.objects(tags__in=tags_list)
    return quotes


if __name__ == '__main__':
    while True:
        print("""Format input query:
            name: fullname      -   Search for quotes by author name
                example - name: Albert Einstein or short - name: al
            tag: tag1           -   Search for quotes by tag
                example - tag: life or short - tag: li
            tags: tag1,tag2,... -   Search for quotes by a set of tags
                example - tags: life,live
            exit    -  exit from the application
        """)
        query = input("Input query:")
        if query == 'exit':
            break
        try:
            command, value = query.split(':')
        except ValueError as vr:
            print(f'ValueError: {vr}\nTry againe')
            continue

        command = command.strip()
        value = value.strip()

        if command == 'name':
            result, author = by_author(value)
            print(f'Search for quotes by author name "{author}"')
            
        elif command == 'tag':
            result = by_tag(value)
            print(f'Search for quotes by tag "{value}"')
            
        elif command == 'tags':
            list_tags = value.split(',')
            result = by_tags(list_tags)
            print(f'Search for quotes by a set of tags = {list_tags}')

        else:
            print('Wrong query\nTry again')
            continue

        print(30 * '-')
        for res in result:
            print(res.content)
        print(30 * '-')
