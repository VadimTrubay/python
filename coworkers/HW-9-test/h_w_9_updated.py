user_dict = {}

def catcher_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Name should be spelled correctly'
        except TypeError:
            return 'Command Not Found'
        except IndexError:
            return 'Value Not Found, Please Use commands carrifuly.'
        except ValueError as ex:
            return ex.args[0]
    return inner


@catcher_errors
def hello_function():
    return 'How can i help you?'


@catcher_errors
def add_func(data):
    name, phone = create_data(data)
    if name in user_dict:
        raise ValueError('This contact already exist!')
    user_dict[name] = phone
    return f'Added to list: {name.title()}, {phone}'


@catcher_errors
def change_function(data):

    name, phone = create_data(data)
    if name in user_dict:
        user_dict[name] = phone
        return f'Contuct {name} number changed to {phone}.'
    return 'You are trying to change not existed contact.'


@catcher_errors
def phone_function(name):
    if name.strip() not in user_dict:
        raise ValueError('You are trying to enter not existed name!')
    return user_dict.get(name.strip())


@catcher_errors
def show_all_function():
    char = ''
    for k, v in user_dict.items():
        char += f'{k} : {v} \n'
    return char


@catcher_errors
def good_bye_function():
    return 'Good Bye!'


COMAND_LIST = {
            'hello': hello_function,
            'add': add_func,
            'change': change_function,
            'phone': phone_function,
            'show all': show_all_function,
            "good bye": good_bye_function,
            "close": good_bye_function,
            "exit": good_bye_function
        }


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMAND_LIST:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()


def reaction_func(reaction):
    return COMAND_LIST.get(reaction, break_func)


def create_data(data):
    new_data = data.strip().split(' ')
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError('Incorrect name!')
    if not phone.isnumeric():
        raise ValueError('Incorrect phone number!')
    return name, phone


def break_func():
    return 'Incorrect input, please spell data again!'


def main():
    while True:
        user_input = input('Enter command here: ')
        result = change_input(user_input)
        print(result)
        if result == 'Good Bye!':
            break






if __name__ == '__main__':
    main()

