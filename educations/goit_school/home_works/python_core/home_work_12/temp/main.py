from goit_school.home_works.python_core.home_work_12.temp.contact_bot import *


if __name__ == "__main__":
    bot = Bot()
    bot.book.load('save')

    while True:
        print('-' * 52)
        print('Hello. I am your contact-assistant.\n'
              'What should I do with your contacts?')
        print('-' * 52)
        command = input('Enter command(type help for a list of commands):\n>').strip().lower()
        bot.handler(command)
        if command in ['add', 'delete', 'edit', 'clear']:
            bot.book.save('save')
        if command == 'exit':
            bot.book.save('save')
            print('goodbye my little friend')
            break