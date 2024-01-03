from datetime import datetime
import re
from abc import ABC, abstractmethod


class Record:

    def __init__(self, name, phone='', birthday='', email='', status='', note=''):

        self.birthday = birthday
        self.name = name
        self.phone = phone
        self.email = email
        self.status = status
        self.note = note

    def days_to_birthday(self):
        current_datetime = datetime.now()
        self.birthday = self.birthday.replace(year=current_datetime.year)
        if self.birthday >= current_datetime:
            result = self.birthday - current_datetime
        else:
            self.birthday = self.birthday.replace(year=current_datetime.year + 1)
            result = self.birthday - current_datetime
        return result.days


class Field(ABC):

    @abstractmethod
    def __getitem__(self):
        pass


class Name(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


class Phone(Field):

    def __init__(self, value=''):
        while True:
            self.value = []
            if value:
                self.values = value
            else:
                self.values = input('phone: ')
            try:
                for number in self.values.split(' '):
                    if re.match(r'^\+380\d{9}$', number) or number == '':
                        self.value.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print('incorrect phone number formate')
            else:
                break

    def __getitem__(self):
        return self.value


class Birthday(Field):

    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input('birthday(dd.mm.YYYY): ')
            try:
                if re.match(r'^\d{2}.\d{2}.\d{4}$', self.value):
                    self.value = datetime.strptime(self.value.strip(), '%d.%m.%Y')
                    break
                elif self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('incorrect birthday')

    def __getitem__(self):
        return self.value


class Email(Field):

    def __init__(self, value=''):
        while True:

            if value:
                self.value = value
            else:
                self.value = input('email: ')
            try:
                if re.match(r'^(\w|\.|_|-)+@(\w|_|-|\.)+[.]\w{2,3}$', self.value) or self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please provide correct email.')

    def __getitem__(self):
        return self.value


class Status(Field):

    def __init__(self, value=''):
        while True:
            self.status_types = ['', 'family', 'friend', 'work']
            if value:
                self.value = value
            else:
                self.value = input('type of relationship (family, friend, work): ')
            try:
                if self.value in self.status_types:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('there is no such status')

    def __getitem__(self):
        return self.value


class Note(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value
