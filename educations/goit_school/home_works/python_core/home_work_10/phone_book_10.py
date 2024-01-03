import json
import os
import pprint
import time
from collections import UserDict, UserList


def command_help():
    print('Command                                       Action\n'
          '----------------------------------------------------\n'
          'hello                                       greeting\n'  # 1 command
          'add                     add new phone number by name\n'  # 3 command
          'change                   change phone number by name\n'  # 3 command
          'show phone                         show phone number\n'  # 2 command
          'show all                      show all phone numbers\n'  # 1 command
          'delete                   delete phone number by name\n'  # 2 command
          'clear                                clear phonebook\n'  # 1 command
          '"bye" or "close" or "exit"      application shutdown\n'  # 1 command
          '----------------------------------------------------')


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()


class Record(AddressBook):
    def __init__(self, name, phone, new_phone):
        super().__init__()
        self.name = name
        self.phone = phone
        self.new_phone = new_phone

    def add_contact(self, name, phone):
        phone_list = self.data.get(name, [])
        phone_list.append(phone)
        self.data[name] = phone_list

    def change_contact(self, name, phone, new_phone):
        for i in self.data[name]:
            if i == phone:
                self.data[name].remove(phone)
                self.data[name].append(new_phone)

    def delete_contact(self, name):
        del self.data[name]


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


def main():

    record = Record('', '', '')
    with open('phone_book.json', 'r') as fh:
        d = json.load(fh)
    record |= d

    while True:
        print('___________________________\n')
        command = input('>Enter_command: ').strip().lower()
        os.system('cls')
        # command_help()
        print('___________________________\n')
        try:
            if command == 'hello':
                print('How can I help you?')

            elif command == 'add':
                name = Name(input('>Enter_name_for_add: ').strip().lower())
                if name.value:
                    phone = Name(int(input('>Enter_phone_for_add: ').strip()))
                    record.add_contact(name.value, phone.value)
                    print(f'Phone {name.value} added')
                    if not phone.value:
                        print('Attention, the contact was added without a phone number')
                else:
                    print('Please enter a name')

            elif command == 'change':
                name = Name(input('>Enter_name_for_change: ').strip().lower())
                if name.value:
                    if name.value in record:
                        phone = Name(int(input('>Enter_phone_for_change: ').strip()))
                        if phone.value:
                            if phone.value in record.data[name.value]:
                                new_phone = input('>Enter_new_phone: ').strip()
                                if new_phone:
                                    record.change_contact(name.value, phone.value, new_phone)
                                    print(f'Phone {name.value} updated')
                                else:
                                    print('Please enter a new_phone')
                            else:
                                print('This phone does not exist')
                        else:
                            print('Please enter a phone')
                    else:
                        print('This name does not exist')
                else:
                    print('Please enter a name')

            elif command == 'show phone':
                name = Name(input('>Enter_name_for_show_phone: ').strip().lower())
                if name.value:
                    if name.value in record:
                        print(f"{name.value}: {record.data.get(name.value)}")
                    else:
                        print('This name does not exist')
                else:
                    print('Please enter a name')

            elif command == 'show all':
                if record.data:
                    for k, v in record.data.items():
                        print(f"{k}: {v}")
                else:
                    print('Dictionary empty')

            elif command == 'delete':
                name = Name(input('>Enter_name_for_delete: ').strip().lower())
                record.delete_contact(name)
                print(f'Name {name.value} deleted')

            elif command == 'clear':
                record.data.clear()
                print('Dictionary cleared')

            elif command in ['bye', 'close', 'exit']:
                with open('phone_book.json', 'w') as fh:
                    json.dump(record.data, fh)
                print('Good bye!')
                time.sleep(2.2)
                break
            else:
                print('Invalid command')
        except Exception as error:
            print(f'Error! {error}')
        finally:
            with open('phone_book.json', 'w') as fh:
                json.dump(record.data, fh)


if __name__ == '__main__':
    # command_help()
    main()