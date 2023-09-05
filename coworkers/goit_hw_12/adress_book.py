import pickle

from collections import UserDict
from datetime import datetime
from re import findall
from pathlib import Path

class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == None:
            self.value = ''
        return self.value


class Bithday(Field):  # 'd[d] m[m] yyyy' "03 05 2004" or "3 5 2004"

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if findall(r"\d{1,2} \d{1,2} \d{4}", new_value):
            bd_date = None
            try:
                bd_date = datetime.strptime(
                    str(findall(r"\d{1,2} \d{1,2} \d{4}", new_value)[0]), '%d %m %Y').date()
            except:
                pass
            if bd_date:
                current_year = datetime.now().year
                if current_year - 100 < bd_date.year < current_year:
                    self.__value = findall(
                        r"\d{1,2} \d{1,2} \d{4}", new_value)[0]


class Phone(Field):

    def __init__(self, value):
        self.__phone = None
        self.value = value

    @property
    def value(self):
        return self.__phone

    @value.setter
    def value(self, new_value):
        if findall(r"\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}", new_value):
            self.__phone = new_value


class Name(Field):

    def __init__(self, value):
        self.__name = None
        self.value = value

    @property
    def value(self):
        return self.__name

    @value.setter
    def value(self, name):
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


class Record:
    def __init__(self, name: Name, *phones):
        self.name = name
        self.phones = list(phones)
        self.bithday = None

    def __str__(self):
        s_phones = ''
        for s in self.phones:
            s_phones = s_phones + str(s) + '  '
        return f'Name: {self.name}  Bithday: {self.bithday}  Phone(s): {s_phones}'

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, phone_number_old: Phone, phone_number_new: Phone):
        self.del_phone(phone_number_old)
        self.phones.append(phone_number_new)

    def del_phone(self, phone_number: Phone):
        if phone_number in self.phones:
            self.phones.remove(phone_number)

    def add_bithday(self, bithday: Bithday):
        self.bithday = bithday

    def days_to_birthday(self):
        if self.bithday:
            current_datetime = datetime.now()
            bd_date = datetime.strptime(str(self.bithday), '%d %m %Y').date()
            bithday_this_year = datetime(
                current_datetime.year, bd_date.month, bd_date.day)
            if bithday_this_year.date() >= current_datetime.date():
                days_delta = bithday_this_year.date() - current_datetime.date()

            else:
                days_delta = datetime(current_datetime.year + 1, bd_date.month,
                                      bd_date.day).date() - current_datetime.date()
            return days_delta.days


class AddressBook(UserDict):

    def __str__(self):
        s_return = ''
        for value in self.data.values():
            s_return = s_return + str(value) + ' '
        return s_return

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, n: int = None):
        if not n:
            n = len(self.data)

        k = 1
        str_ret = str(k) + '_' * 40 + '\n'
        i = 0
        for v in self.data.values():
            str_ret += str(v) + '\n'
            if i < n - 1:
                i += 1
            else:
                yield str_ret
                i = 0
                k += 1
                str_ret = str(k) + '_' * 40 + '\n'
        yield str_ret

    def find(self, find_str: str):
        str_ret = '_' * 40 + '\n'
        for value in self.data.values():
            if find_str.isdigit():
                for phone in value.phones:
                    number = phone.value.replace(
                        '-', '').replace(')', '').replace('(', '')
                    if find_str in number:
                        str_ret += str(value) + '\n'
            elif find_str.isalpha() and find_str in str(value.name):
                str_ret += str(value) + '\n'
        return str_ret

    def write_to_file(self, filename):
        with open(filename, "wb") as fh:
            pickle.dump(self.data, fh)

    def read_from_file(self, filename):
        if Path(filename).exists():
            with open(filename, "rb") as fh:
                self.data = pickle.load(fh)
            return self.data
        else:
            print(f'{filename} not exist')
