from datetime import datetime
import re
from abc import ABC, abstractmethod


class Record:

    def __init__(self, name, phone='', birthday=''):

        self.birthday = birthday
        self.name = name
        self.phone = phone

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
                print('incorrect phone number')
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
