from contact_bot import *
import os
import time


def command_help():
    print('Command                                       Action\n'
          '----------------------------------------------------\n'
          'hello                                       greeting\n'
          'add                                      add contact\n'
          'all                                view all contacts\n'
          'find                                  search contact\n'
          'edit                                    edit contact\n'
          'birthday                            days to birthday\n'
          'delete                                delete contact\n'
          'clear                                clear address_book_vad_1.0.01\n'
          'load                                  load address_book_vad_1.0.01\n'
          'save                                  save address_book_vad_1.0.01\n'
          'exit                            application shutdown\n'
          '----------------------------------------------------\n')


if __name__ == "__main__":
    bot = Bot()
    command_help()
    bot.book.load('save')
    while True:
        print('-' * 52)
        command = input('enter command: ').strip().lower()
        os.system('cls')
        command_help()
        bot.handler(command)
        if command in ['add', 'delete', 'edit', 'clear']:
            bot.book.save('save')
        if command == 'exit':
            bot.book.save('save')
            print('goodbye my little friend')
            time.sleep(2)
            break