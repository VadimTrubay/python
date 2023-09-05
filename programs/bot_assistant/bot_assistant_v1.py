import os
import time


def clear_dict():
    with open('phone_list_v1.txt', 'w'):
        print('Dictionary cleared! Please add a new number!')


def show_all():
    with open('phone_list_v1.txt') as fh:
        while True:
            phone_contact = fh.readline().splitlines()
            if phone_contact:
                print(''.join(phone_contact))
            else:
                break
        phone_contact = fh.readline().splitlines()
        if not phone_contact:
            print('Dictionary empty! Please add a new number!')

# def phone(user_input: str):  # phone vad
#     print_phone = user_input.split(' ')
#     with open('phone_list_v1.txt') as fh:
#         while True:
#             phone_contact = fh.readline().splitlines()
#             if phone_contact.startswith(print_phone[1]):
#                 print(phone_contact)
#                 break
#             print('This contact does not exist, please try again!')
#             break


# def add_contact(user_input: str):  # add vad 1111
#     add_cont = user_input.split(' ')
#     with open('phone_list_v1.txt') as fh:
#         read_list_phone_contact = fh.read().splitlines()
#         for name in read_list_phone_contact:
#             if name.split(' ')[0] == add_cont[1]:
#                 print('This contact already exists, please try again!')
#         if name.split(' ')[0] != add_cont[1]:
#             with open('phone_list_v1.txt', 'a') as f:
#                 f.writelines(f'{add_cont[1]} {add_cont[2]}\n')
#                 print('Number added!')


# def delete_contact(user_input: str):  # delete vad
#     delete_cont = user_input.split(' ')
#     with open('phone_list_v1.txt') as fh:
#         read_list_phone_contact = fh.readline().splitlines()
#         for name in read_list_phone_contact:
#             if name.split(' ')[0] == delete_cont[1]:
#                 with open('phone_list_v1.txt', 'a') as f:
#                     f.(f'{add_cont[1]} {add_cont[2]}\n')
#                     print('Number added!')
#         if name.split(' ')[0] != add_cont[1]:
#             print('This contact already exists, please try again!')




def good_bye():
    print("Good bye!")

#
#
def hello():
    print("How can I help you?")
#

# def change_contact(user_input: str, dict_contact: dict) -> dict:
#     change_contact = user_input.split(' ')
#     change_cont = change_contact[1:]
#     if change_cont[0] in dict_contact.keys():
#         dict_contact.update([change_cont])
#         print('Number updated!')
#     else:
#         print('This contact does not exist, please try again!')
#
#     return dict_contact
#
#
def command_help():
    print('Welcome to bot assistant.\n'
          'Command                                       Action\n'
          '----------------------------------------------------\n'
          'hello                                      greetings\n'
          'add ...                 add new phone number by name\n'
          'change ...               change phone number by name\n'
          'phone ...                 print phone number by name\n'
          'delete ...               delete phone number by name\n'
          'show all                      show all phone numbers\n'
          'clear                                clear phonebook\n'
          '"good bye", "close", "exit"     application shutdown\n'
          '----------------------------------------------------\n')


def main():

    while True:
        print('___________________________')
        user_input = input('>Enter_command: ')  # sys.argv[1]
        user_inp = user_input.split(' ')[0]
        os.system('cls')
        command_help()
        if user_inp.lower() == 'hello':
            hello()
        elif user_inp.lower() == 'phone':
            phone(user_input)

        elif user_input == 'show all':
            show_all()

        elif user_inp.lower() == 'add':
            add_contact(user_input)

        # elif user_inp.lower() == 'change':
        #     change_contact(user_input, dict_contact)

        elif user_inp.lower() == 'clear':
            clear_dict()

        # elif user_inp.lower() == 'delete':
        #     delete_contact(user_input, dict_contact)

        elif user_inp.lower() in ['good bye', 'close', 'exit']:
            good_bye()
            time.sleep(2.2)
            break
        else:
            print('Invalid command! Try again!')


if __name__ == '__main__':
    command_help()
    main()
