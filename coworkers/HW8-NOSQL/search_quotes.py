from models import *
from colorit import *


def main():
    while True:
        command = input(color("Enter your command: ",Colors.green))
        if command in ["exit", "."]:
            print(color("Goodbye",Colors.red))
            break

        elif command.startswith("tag:"):
            search = command.split(":")[1]
            res = Quotes.objects(tags = search)
            for quot in res:
                author_id = quot.author.id
                author = Authors.objects(id= author_id)[0]
                print(color(f'''
                Author = {author.fullname}.
                Quotes = {quot.quote}
                ''',Colors.blue
                ))

        elif command.startswith("tags:"):
            search = command.split(":")[1].split(",")
            quotes = Quotes.objects(tags__in =search)

            for quote in quotes:
                author_id = quote.author.fullname
                print(color(f'''
                Author = {author_id}.
                Quotes = {quote.quote}
                ''',Colors.blue))

        elif command.startswith("name:"):
            search = command.split(":")[1].strip()
            author_id = Authors.objects(fullname = search)[0].id
            author_name = Authors.objects(fullname = search)[0].fullname
            list_quotes = Quotes.objects(author = author_id)
            for quote in list_quotes:
                print(color(f"""
                Author = {author_name}.
                Quotes = {quote.quote}
                """,Colors.blue))

        else:
            print(color("Wrong command",Colors.red))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(color("Something went wrong, check ur values",Colors.red))