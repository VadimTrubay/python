from datetime import datetime, timedelta
from collections import UserList
import pickle
from fields import *
import os


class AddressBook(UserList):

    def __init__(self):
        super().__init__()
        self.data = []
        self.counter = -1

    def __str__(self):
        result = []
        for key in self.data:
            if key['birthday']:
                birth = key['birthday'].strftime('%d.%m.%Y')
            else:
                birth = ''
            if key['phone']:
                new_value = []
                for phone in key['phone']:
                    if phone:
                        new_value.append(phone)
                phone = ', '.join(new_value)
            else:
                phone = ''
            result.append(f"name: {key['name']}"
                          f"\nphone: {phone}"
                          f"\nbirthday: {birth}\n" + '-' * 50)
        return '\n'.join(result)

    @property
    def __next__(self):
        phone = []
        self.counter += 1
        if self.data[self.counter]['birthday']:
            birth = self.data[self.counter]['birthday'].strftime('%d.%m.%Y')
        if self.counter == len(self.data):
            self.counter = -1
            raise StopIteration
        for number in self.data[self.counter]['phone']:
            if number:
                phones.append(number)
        result = f"name: {self.data[self.counter]['name']}" \
                 f"\nphone: {', '.join(phone)}" \
                 f"\nbirthday: {birth}\n" + '-' * 50
        return result

    def __iter__(self):
        return self

    def __setitem__(self, key, value):
        self.data[key] = {'name': value.name,
                          'phones': value.phone,
                          'birthday': value.birthday}

    def __getitem__(self, key):
        return self.data[key]

    def log(self, action):
        current_time = datetime.strftime(datetime.now(), '%H:%M:%S')
        message = f'[{current_time}] {action}'
        with open('logs.txt', 'a') as file:
            file.write(f'{message}\n')

    def add(self, record):
        contact = {'name': record.name,
                   'phone': record.phone,
                   'birthday': record.birthday}
        self.data.append(contact)
        print(f'>contact {record.name} added')
        self.log(f'>contact {record.name} added')

    def save(self, file_name):
        with open(file_name + '.bin', 'wb') as file:
            pickle.dump(self.data, file)
        print('>address_book saved')
        self.log('>address_book saved')

    def load(self, file_name):
        empty_ness = os.stat(file_name + '.bin')
        if empty_ness.st_size != 0:
            with open(file_name + '.bin', 'rb') as file:
                self.data = pickle.load(file)
            self.log('>address_book loaded')
            print('>address_book loaded')
        else:
            print('>address_book created')
            self.log('>address_book_vad_1.0.01 created')
        return self.data

    def search(self, pattern, category):
        result = []
        category_new = category.strip().lower().replace(' ', '')
        pattern_new = pattern.strip().lower().replace(' ', '')

        for key in self.data:
            if category_new == 'phone':
                for phone in key['phone']:
                    if phone.lower().startswith(pattern_new):
                        result.append(key)
            elif key[category_new].lower().replace(' ', '') == pattern_new:
                result.append(key)
        if not result:
            print('contact not found')
        return result

    def edit(self, contact_name, parameter, new_value):
        names = []
        try:
            for key in self.data:
                names.append(key['name'])
                if key['name'] == contact_name:
                    if parameter == 'birthday':
                        new_value = Birthday(new_value).value
                    elif parameter == 'phone':
                        new_contact = new_value.split(' ')
                        new_value = []
                        for number in new_contact:
                            new_value.append(Phone(number).value)
                    if parameter in key.keys():
                        key[parameter] = new_value
                    else:
                        raise ValueError
            if contact_name not in names:
                raise NameError
        except ValueError:
            print('>incorrect parameter')
        except NameError:
            print('>contact not found')
        else:
            print(f'>contact {contact_name} edited')
            self.log(f'>contact {contact_name} edited')
            return True
        return False

    def delete(self, value):
        flag = False
        for key in self.data:
            if key['name'] == value:
                self.data.remove(key)
                print(f'>contact {key["name"]} deleted')
                self.log(f'>contact {key["name"]} deleted')
                flag = True
        return flag

    def clear_book(self):
        self.data.clear()
        print(f'>address_book_vad_1.0.01 cleared')
        self.log(f'>address_book_vad_1.0.01 cleared')

    def __get_current_week(self):
        now = datetime.now()
        current_weekday = now.weekday()
        if current_weekday < 5:
            week_start = now - timedelta(days=2 + current_weekday)
        else:
            week_start = now - timedelta(days=current_weekday - 5)
        return [week_start.date(), week_start.date() + timedelta(days=7)]

