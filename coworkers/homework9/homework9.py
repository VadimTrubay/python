dict_users = {    # словник з номерами и именами людей
    "dima": "039902003",
    "elena": "9000299192",
    "arsen": "9292123222"
}   


def input_error(func):    #декоратор
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Something went wrong"
        except ValueError:
            return "Something went wrong"
    return inner


def say_bye():
    return "Goob bye, see u soon"


def hello_answer(*args):
    return "Hello, glad to see u\nHow can I help you?"


@input_error
def show_all(*args):
    info = ""
    for name, number in dict_users.items():
        info += f"Name: {name.title()}  Number: {number}\n"
    return info


@input_error
def add_user(*args):
    name = args[-2]
    phone = args[-1]
    dict_users[name]= phone
    return f"You added new user {name.title()} with phone {phone}"


@input_error
def change_user(*args):
    name = args[-2]
    phone = args[-1]
    if name in dict_users:
        dict_users[name] = phone
        return f"Now {name.title()} has new number - {phone}"
    else:
        return f"{name.title()} not exist in dictionary"


@input_error
def show_phone(*args):
    user = args[-1]
    phone = dict_users.get(user)
    return f"{user.title()} has phone - {phone}"


OPERATIONS = {
    "hello":    hello_answer,
    "show all": show_all,
    "phone":    show_phone,
    "change":   change_user,
    "add":      add_user,
    "good bye": say_bye,
    "close":    say_bye,
    "exit":     say_bye,
    ".":        say_bye
    
}


def command_parser(text: str):
    for command_name, command in OPERATIONS.items():
        if text.startswith(command_name):
            return command, text.replace(command_name, '').strip().split()
    return None, None


def main():
    while True:
        input_user = input("Enter your command: ").lower()
        command, data = command_parser(input_user)
        if command:
            print(command(*data))
        elif input_user == ".":
            break
        else:
            print("Not found your command")  
 
      
        
           
if __name__ == "__main__":
    main()





























































        
