from abc import ABC, abstractmethod
import re


class Record:
    def __init__(self, name, phone='', birthday=''):
        self.name = name
        self.phone = phone
        self.birthday = birthday


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

    def __init__(self, value):
        try:
            match = re.match(r'^\+380\d{9}$', value)
            res = True if match else False
            not_exist = True if not value else False
            if res or not_exist:
                self.value = value
        except ValueError:
            print('incorrect  number')

    def __getitem__(self):
        return self.value


class Birthday(Field):

    def __init__(self, value):
        try:
            match = re.match(r'^\d{2}.\d{2}.\d{4}$', value)
            res = True if match else False
            not_exist = True if not value else False
            if res or not_exist:
                self.value = value
        except ValueError:
            print('incorrect birthday')

    def __getitem__(self):
        return self.value