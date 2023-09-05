from collections import UserDict

class Field:
    pass

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Name(Field):
    def __init__(self, name):
        self.name = name

class Record:
    def __init__(self, name: Name, *phones):
        self.name = name
        self.phones = list(phones)

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, phone_number_old: Phone, phone_number_new: Phone):
        self.phones.remove(phone_number_old)
        self.phones.append(phone_number_new)

    def del_phone(self, phone_number: Phone):
        self.phones.remove(phone_number)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.name] = record
