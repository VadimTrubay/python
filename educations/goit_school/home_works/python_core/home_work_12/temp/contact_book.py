from abc import ABC, abstractmethod
from datetime import datetime, timedelta, date
from collections import UserList
import pickle
from contact_fields import *
import os


class PrintInfo(ABC):
    @abstractmethod
    def print_info(self, command):
        pass


class Logger:
    @staticmethod
    def log(command):
        current_time = datetime.strftime(datetime.now(), '%H:%M:%S')
        message = f'{current_time} - {command}'
        with open('logs.txt', 'a') as file:
            file.write(f'{message}\n')


class CommandHelp:
    @staticmethod
    def command_help():
        print('----------------------------------------------------\n'
              'Command                                       Action\n'
              '----------------------------------------------------\n'
              'hello                                       greeting\n'
              'add                                      add contact\n'
              'all                                view all contacts\n'
              'find                                  search contact\n'
              'edit                                    edit contact\n'
              'birthday                            days to birthday\n'
              'delete                                delete contact\n'
              'clear                             clear address_book_vad_1.0.01\n'
              'load                               load address_book_vad_1.0.01\n'
              'save                               save address_book_vad_1.0.01\n'
              'exit                            application shutdown')


class ContactBook(UserList, PrintInfo):

    def __init__(self):
        super().__init__()
        self.data = []

    # def __str__(self):
    #     result = []
    #     for key in self.data:
    #         result.append(f"name: {key['name']}"
    #                       f"\nphone: {key['phone']}"
    #                       f"\nbirthday: {key['birthday']}\n" + '-' * 52)
    #     return '\n'.join(result)

    def __setitem__(self, key, value):
        self.data[key] = {'name': value.name,
                          'phone': value.phone,
                          'birthday': value.birthday}

    def __getitem__(self, key):
        return self.data[key]

    def print_info(self, contact):
        print('-' * 52 + f"\nname: {contact['name']}"
                         f"\nphone: {contact['phone']}"
                         f"\nbirthday: {contact['birthday']}")

    def add(self, record):
        contact = {'name': record.name,
                   'phone': record.phone,
                   'birthday': record.birthday}
        self.data.append(contact)
        Logger.log(f'contact {record.name} added')
        print(f'contact {record.name} added')

    def iterator(self, n):
        index = 0
        temp = []
        for contact in self.data:
            temp.append(contact)
            index += 1
            if index >= n:
                yield temp
                temp.clear()
                index = 0
        if temp:
            yield temp

    def get_page(self, n):
        gen = self.iterator(n)
        for i in range(len(self.data)):
            try:
                result = next(gen)
                for contact in result:
                    self.print_info(contact)
                print('-' * 52)
                print(f'page {i + 1}')
                input('press enter for next page>')
            except StopIteration:
                break

    def find_info(self, pattern):
        count = 0
        result = []
        for contact in self.data:
            string = contact.values()
            string = ''.join(string)
            string.replace('+', '').replace('.', '')
            if pattern in string:
                result.append(contact)
                count += 1
        if not count:
            Logger.log('data not found')
            print('data not found')

        for contact in result:
            self.print_info(contact)

    def edit(self, name, parameter, new_value):
        for key in self.data:
            if key['name'] == name:
                if parameter in key.keys():
                    key[parameter] = new_value
                    print(f'contact {name} edited')
                    log(f'contact {name} edited')
                    break
        else:
            Logger.log('contact not found')
            print('contact not found')

    def days_to_birthday(self, name):
        for contact in self.data:
            if name == contact['name']:
                birthday = contact['birthday']
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
                break
        else:
            Logger.log('contact not found')
            print('contact not found')

    def save(self, file_name):
        with open(file_name + '.bin', 'wb') as file:
            pickle.dump(self.data, file)
        Logger.log('address_book_vad_1.0.01 saved')

    def load(self, file_name):
        empty_ness = os.stat(file_name + '.bin')
        if empty_ness.st_size != 0:
            with open(file_name + '.bin', 'rb') as file:
                self.data = pickle.load(file)
            Logger.log('address_book_vad_1.0.01 loaded')
        else:
            print('address_book_vad_1.0.01 created')
            Logger.log('address_book_vad_1.0.01 created')
        return self.data

    def delete(self, value):
        for key in self.data:
            if key['name'] == value:
                self.data.remove(key)
                print(f'contact {key["name"]} deleted')
                Logger.log(f'contact {key["name"]} deleted')
                break
        else:
            Logger.log('contact not found')
            print('contact not found')

    def clear_book(self):
        self.data.clear()
        print('address_book_vad_1.0.01 cleared')
        Logger.log('address_book_vad_1.0.01 cleared')
