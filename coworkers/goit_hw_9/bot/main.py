def input_error(func):
    def func_wrapper(*args):
        try:
            return func(*args)

        except IndexError:
            return 'Wrong input. Try agane.'

        except ValueError:
            return 'Wrong input. Try agane.'

        except KeyError:
            return 'Wrong input. Try agane.'

    return func_wrapper


def main():
    stop = ('.', 'good bye', 'close', 'exit', 'break')

    work = ('help', 'hello', 'add', 'change', 'phone', 'show all')

    print('', 'Please, enter comand:',
          '1. Hello!',
          '2. Help',
          '3. Add Name phone_number',
          '4. Change Name old_phone_number new_phone_number',
          '5. Phone Name',
          '6. Show all',
          sep='\n'
          )

    while True:

        string = input('\nPlease, enter comand\nHelp for promt\n>>>').lower()
        answer = None
        if string.startswith(stop):
            print('Good bye!')
            break
        elif string.startswith(work):
            answer = handler(string)
            print(answer)
        else:
            print('Wrong input. Try agane.')


contacts = {}


def handler(string):
    work_list = string.split()
    if string.startswith('hello'):
        return 'How can I help you?'

    elif string.startswith('help'):
        return ('\nPlease, enter comand:\n1. Hello!\n2. Help\n' +
                '3. Add Name phone_number\n' +
                '4. Change Name old_phone_number new_phone_number\n' +
                '5. Phone Name\n6. Show all'
                )

    elif string.startswith('add'):
        return handler_add(string)

    elif string.startswith('change'):
        return handler_change(string)

    elif string.startswith('phone'):
        return handler_phone(string)

    else:
        return handler_show_all()


@input_error
def handler_add(string):
    work_list = string.split()
    name = work_list[1]
    number_phone = work_list[2]
    if name.capitalize() in contacts:
        contacts[name.capitalize()].append(number_phone)
        return 'This name already exists! Number successfully added.'
    else:
        contacts[name.capitalize()] = []
        contacts[name.capitalize()].append(number_phone)
        return 'Contact successfully added.'


@input_error
def handler_change(string):
    work_list = string.split()
    name = work_list[1]
    number_phone_old = work_list[2]
    number_phone_new = work_list[3]
    if name.capitalize() in contacts:
        if number_phone_old in contacts[name.capitalize()]:
            contacts[name.capitalize()].remove(number_phone_old)
            contacts[name.capitalize()].append(number_phone_new)
        else:
            return 'This number ' + number_phone_old + ' not exist.\n Try again.'
    else:
        return 'This Name ' + name.capitalize() + ' not exist.\n Try again.'
    return 'Contact successfully changed.'


@input_error
def handler_phone(string):
    work_list = string.split()
    name = work_list[1]
    str_return = name.capitalize()
    if name.capitalize() in contacts:
        for number in contacts[name.capitalize()]:
            str_return = str_return + ' ' + number
        return str_return
    else:
        return 'This Name ' + name.capitalize() + ' not exist.\nTry again.'


def handler_show_all():
    str_return = ''
    for name in contacts:
        str_return = str_return + name + ': '
        for number in contacts[name]:
            str_return = str_return + number + '| '
        str_return = str_return + '\n'
    return str_return


if __name__ == "__main__":
    main()