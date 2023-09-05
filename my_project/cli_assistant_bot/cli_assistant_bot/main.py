import os
from .addressbook import main as ab
from .calculator import main as calc
from .notebook import main as nb, NoteBook, Record, Tag
from .file_sort_ import main as fs
from time import sleep


def main():
    while True:
        os.system('cls')
        print(f'{" " * 10}CLI ASSISTANT BOT')
        print(f"{'*' * 16} {'menu'} {'*' * 16}",
              '1| address_book',
              '2| note_book',
              '3| clean_folder',
              '4| calculator',
              '5| exit',
              f"{'*' * 38}\n", sep='\n')

        try:
            command = int(input('Your choose >>>: '))
            if command == 1:
                result = ab()
                if result == 'exit':
                    continue

            elif command == 2:
                result = nb()
                if result == 'exit':
                    continue

            elif command == 3:
                result = fs()
                if result == 'exit':
                    continue

            elif command == 4:
                result = calc()
                if result == 'exit':
                    continue

            elif command == 5:
                print('good bye!')
                sleep(1.5)
                break

            else:
                raise ValueError

        except Exception:
            print('incorrect input, try again')
            input('<press Enter to continue>')
            continue


if __name__ == '__main__':
    main()
