from datetime import datetime, date
import json
import os
import time
from pprint import pprint
import re
from collections import UserDict


# функция вывода в терминал списка возможных команд
def command_help():
    print('Command                                       Action\n'
          '----------------------------------------------------\n'
          'hello                                       greeting\n'
          'add                     add new phone number by name\n'
          'phone                              show phone number\n'
          'find          search for information about a contact\n'
          'all                           show all phone numbers\n'
          'delete                   delete phone number by name\n'
          'clear                                clear phonebook\n'
          'birthday                            days to birthday\n'
          '"bye" or "close" or "exit"      application shutdown\n'
          '----------------------------------------------------')


# open_and_read_file
def open_and_read_file(file_name):
    with open(file_name, 'r') as fh:
        d = json.load(fh)
        return d


# класс книги контактов, в словаре хранятся контакты, где ключ это имя
class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    # метод добавляет record в AddressBook
    def add_record(self, record):
        self.data[record.name] = [record.phone, record.birthday]

    # close_and_save_file
    def close_and_save_file(self, file_name):
        with open(file_name, 'w') as fh:
            json.dump(self.data, fh)

    def find_info(self, data):
        count = 0
        for k, v in self.data.items():
            sting = f'{k}{v[0]}{v[1]}'
            sting = sting.replace('+', '').replace('(', '').replace(')', '').replace('-', '', 2).replace('.', '')
            if data in sting:
                print(k, v)
                count += 1
        if not count:
            print('Data not found')

    # метод печатает в терминал n записей контактов телефонной книги
    def iterator(self, n=3):
        index = 0
        temp = []
        for k, v in self.data.items():
            temp.append(f'{k}: {v[0]}, {v[1]}')
            index += 1
            if index >= n:
                yield temp
                temp.clear()
                index = 0
        if temp:
            yield temp

    def get_page(self, n=3):
        gen = self.iterator(n)
        for i in range(len(self.data)):
            try:
                result = next(gen)
                pprint(result)
                print('----------------------------------------')
                print(f'Page{i + 1}')
                input('\nPress enter for next page: ')
                print('----------------------------------------\n')
                os.system('cls')
                command_help()
            except StopIteration:
                break


# класс записей в книгу контактов
class Record:
    def __init__(self, name, phone, birthday):
        super().__init__()
        self.name = name
        self.phone = phone
        self.birthday = birthday

    # метод добавляет контакт с именем, телефоном и днём рождения в Record
    def add_contact(self, name, phone, birthday):
        self.data["name"] = name.value
        self.data["phone"] = phone.value
        self.data["birthday"] = birthday.value

    # метод вычисляет количество дней до следующего дня рождения контакта по имени
    @staticmethod
    def days_to_birthday(name, birthday):
        birth_day = datetime.strptime(birthday, '%d.%m.%Y')
        birth_day = date(birth_day.year, birth_day.month, birth_day.day)
        current_date = date.today()
        user_date = birth_day.replace(year=current_date.year)
        delta_days = user_date - current_date
        if delta_days.days >= 0:
            print(f"{delta_days.days} days left until {name}'s birthday")
        else:
            user_date = user_date.replace(year=user_date.year + 1)
            delta_days = user_date - current_date
            print(f"{delta_days.days} days left until {name}'s birthday")


# родительский класс для всех полей контакта(имя, телефон, день рождения)
class Field:
    def __init__(self, value):
        self.value = value


# класс имени контакта
class Name(Field):
    pass


# класс телефона контакта
class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
        self.__private_phone = None

    @property
    def value(self):
        return self.__private_value

    @value.setter
    def value(self, val: str):
        match = re.fullmatch(r'[+]\d{3}[(]\d{2}[)]\d{3}-\d{2}-\d{2}', val)
        res = True if match else False
        not_exist = True if not val else False
        if res or not_exist:
            self.__private_value = val
        else:
            raise ValueError('Phone is invalid value')


# класс дня рождения контакта
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
        self.__private_birthday = None

    @property
    def value(self):
        return self.__private_value

    @value.setter
    def value(self, val: str):
        match = re.fullmatch(r'\d{2}[.]\d{2}[.]\d{4}', val)
        res = True if match else False
        not_exist = True if not val else False
        if res or not_exist:
            self.__private_value = val
        else:
            raise ValueError('Birthday is invalid value')


def main():
    file_name = 'phone_book_11.json'
    record = Record('', '', '')
    address_book = AddressBook()
    address_book.data = open_and_read_file(file_name)

    while True:
        print('----------------------------------------\n')
        command = input(">Enter_command: ").strip().lower()
        os.system('cls')
        print('----------------------------------------')
        command_help()
        try:
            if command == "hello":
                print("How can I help you?")

            elif command == "add":
                name = Name(input(">Enter_name_for_add: ").strip().lower())
                if name.value:
                    phone = Phone(input(">Enter_phone_for_add [+380(xx)xxx-xx-xx]: ").strip())
                    birthday = Birthday(input(">Enter_birthday_for_add(dd.mm.yyyy): ").strip())
                    record = Record(name.value, phone.value, birthday.value)
                    address_book.add_record(record)
                    print(f"Contact {name.value} added")
                    if not phone.value:
                        print('Attention, the contact was added without a phone number')
                    if not birthday.value:
                        print('Attention, the contact was added without a birthday')
                else:
                    print('Please enter a name')

            elif command == 'phone':
                name = Name(input('>Enter_name_for_show_phone: ').strip().lower())
                if name.value:
                    if name.value in address_book.data:
                        value = address_book[name.value][0]
                        if value:
                            print(f"{name.value}: {address_book.data[name.value][0]}")
                        else:
                            print('This contact does not phone')
                    else:
                        print('This name does not exist')
                else:
                    print('Please enter a name')

            elif command == 'find':
                data = input('>Enter data to search: ').strip().lower()
                if data:
                    address_book.find_info(data)
                else:
                    print('Please enter a data')

            elif command == 'all':
                if address_book.data:
                    address_book.get_page()
                else:
                    print('Dictionary empty')

            elif command == 'delete':
                name = Name(input('>Enter_name_for_delete: ').strip().lower())
                if name.value:
                    if name.value in address_book.data:
                        del address_book.data[name.value]
                        print(f'Name {name.value} deleted')
                    else:
                        print('This name does not exist')
                else:
                    print('Please enter a name')

            elif command == 'clear':
                address_book.data.clear()
                print('Dictionary cleared')

            elif command == 'birthday':
                name = Name(input('>Enter_name: ').strip().lower())
                if name.value:
                    if name.value in address_book.data:
                        birthday = address_book[name.value][1]
                        if birthday:
                            record.days_to_birthday(name.value, birthday)
                        else:
                            print('This contact does not birthday')
                    else:
                        print('This name does not exist')
                else:
                    print('Please enter a name')

            elif command in ['bye', 'close', 'exit']:
                address_book.close_and_save_file(file_name)
                print('Good bye!')
                time.sleep(2)
                break
            else:
                print('Invalid command')
        except Exception as error:
            print(f'Error! {error}')
        finally:
            address_book.close_and_save_file(file_name)


if __name__ == '__main__':
    command_help()
    main()