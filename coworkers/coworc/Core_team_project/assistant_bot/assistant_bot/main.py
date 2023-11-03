from functions import commands_dict, parser, users, hello
import addressbook
import console

# from addressbook import *
# from functions import *
# from assistant_bot.addressbook import *
# from assistant_bot.functions import *


the_end = False


def main():
    try:
        print(hello())
        while not the_end:
            #user_input = input("Enter please: ").lower()
            user_input = console.get_input("Enter please: ").lower()
            if user_input in ["good_bye", "close", "exit"]:
                print(commands_dict.get("exit")())
                break
            else:
                print(parser(user_input))
    finally:
        users.save_file()


if __name__ == '__main__':
    main()
