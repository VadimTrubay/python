import os
import time


def input_error(function):
    """
    Створюємо декоратор для обробки помилок, котрі можуть виникнути через
    ввід користувача.
    :param function: Функція вводу від користувача.
    :return: Або роботу функції або текст з помилкою, для повторного вводу.
    """

    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'

    return inner


@input_error
def add_contact(name, phone, dict_contact):
    if name in dict_contact:
        print('This contact already exists, please try again!')
    else:
        dict_contact[name] = phone
        print('Number added!')

    return dict_contact


@input_error
def delete_contact(dict_contact):
    name = input('Enter name>>: ')
    if not name in dict_contact:
        print('This contact does not exist, please try again!')
    else:
        del dict_contact[name]
    print('Number deleted!')
    return dict_contact


def good_bye():
    print("Good bye!")
    time.sleep(2.2)


@input_error
def show_phone(dict_contact):
    name = input('Enter name>>: ')
    if name in dict_contact.keys():
        print(f"{name}: {dict_contact[name]}")
    else:
        print('This contact does not exist, please try again!')


def hello():
    print("How can I help you?")


def clear_dict(dict_contact):
    dict_contact.clear()
    print('Dictionary cleared! Please add a new number!')
    return dict_contact


@input_error
def change_contact(dict_contact):
    name = input('Enter name>>: ')
    phone = input('Enter phone>>: ')
    if name in dict_contact.keys():
        dict_contact.update({name: phone})
        print('Number updated!')
    else:
        print('This contact does not exist, please try again!')

    return dict_contact


def show_all(dict_contact):
    if dict_contact:
        for k, v in dict_contact.items():
            print(f'{k}: {v}')
    else:
        print('Dictionary empty! Please add a new number!')


def command_help():
    print('Welcome to bot assistant.\n'
          'Command                                       Action\n'
          '----------------------------------------------------\n'
          'hello                                      greetings\n'  # 1 command
          'add ...                 add new phone number by name\n'  # 3 command
          'change ...               change phone number by name\n'  # 3 command
          'phone ...                 print phone number by name\n'  # 2 command
          'delete ...               delete phone number by name\n'  # 2 command
          'show all                      show all phone numbers\n'  # 1 command
          'clear                                clear phonebook\n'  # 1 command
          '"good bye", "close", "exit"     application shutdown\n'  # 1 command
          '----------------------------------------------------\n')


def main():
    dict_contact = dict()
    with open('phone_book.txt') as fh:
        while True:
            data = fh.readline().split()
            if not data:
                break
            d = dict([data])
            dict_contact |= d

    while True:
        print('___________________________')
        user_input = input('>Enter_command: ')
        os.system('cls')
        command_help()
        if user_input.lower() == 'hello':
            hello()

        elif user_input.lower() == 'phone':
            show_phone(dict_contact)

        elif user_input.lower() == 'show all':
            show_all(dict_contact)

        elif user_input.lower() == 'add':
            name = input('Enter name>>: ')
            phone = input('Enter phone>>: ')
            add_contact(name, phone, dict_contact)

        elif user_input.lower() == 'change':
            change_contact(dict_contact)

        elif user_input.lower() == 'clear':
            clear_dict(dict_contact)

        elif user_input.lower() == 'delete':
            delete_contact(dict_contact)

        elif user_input.lower() in ['good bye', 'close', 'exit']:
            with open('phone_book.txt', 'w') as fh:
                for k, v in dict_contact.items():
                    fh.write(f'{k} {v}\n')
            good_bye()
            break
        else:
            print('Invalid command! Try again!')
        with open('phone_book.txt', 'w') as fh:
            for k, v in dict_contact.items():
                fh.write(f'{k} {v}\n')


if __name__ == '__main__':
    command_help()
    main()
