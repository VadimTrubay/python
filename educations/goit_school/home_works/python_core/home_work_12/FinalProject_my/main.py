import os
import time
from bot import Bot


def command_help():
    print('Command                                       Action\n'
          '----------------------------------------------------\n'
          'hello                                       greeting\n'
          'add                                      add contact\n'
          'all                                view all contacts\n'
          'search                                search contact\n'
          'edit                                    edit contact\n'
          'congratulate                    congratulate contact\n'
          'delete                                delete contact\n'
          'clear                                clear phonebook\n'
          'load                                  load phonebook\n'
          'save                                  save phonebook\n'
          'exit                            application shutdown\n'
          '----------------------------------------------------')


if __name__ == '__main__':
    command_help()
    bot = Bot()
    bot.book.load('auto_save')
    while True:
        print('----------------------------------------------------')
        command = input('>enter_command: ').strip().lower()
        os.system('cls')
        command_help()
        bot.handle(command)
        if command in ['add', 'delete', 'edit', 'clear']:
            bot.book.save('auto_save')
        if command == 'exit':
            bot.book.save('auto_save')
            print('good_bye (-)(-)')
            time.sleep(2)
            break
