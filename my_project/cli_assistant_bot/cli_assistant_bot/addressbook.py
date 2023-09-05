from collections import UserDict
from datetime import datetime, timedelta
import pickle
import re
import os


class AddressBook:
    def __init__(self):
        self.adressbk = {}

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value

    def add_record(self, record):
        self.adressbk[record['name']] = record
        self.current_value = 0

    def update_phone(self):
        self.u = 0
        if len(self.adressbk) == 0:
            print('The Addressbook is empty')
        else:
            contact_key = input("Input the contact name for which you would like to update phone number\n>>>: ")
            needed_contact = self.adressbk.get(contact_key)
            if needed_contact is None:
                print('There is no such contact in Addressbook')
            else:
                while self.u == 0:
                    new_phone = input('Kindly enter new phone number (11 digits, starts with 38)\n>>>: ')
                    if not new_phone.isdigit() and len(new_phone) != 11:
                        print('Incorrect number, there should be 11 digits without any other symbols')
                    else:
                        needed_contact['phone'] = new_phone
                        print('Phone number updated')
                        self.u = 1

    def add_phone(self):
        self.a = 0
        if len(self.adressbk) == 0:
            print('The Addressbook is empty')
        else:
            contact_key = input("Input the contact name for which you would like to add phone number\n>>>: ")
            needed_contact = self.adressbk.get(contact_key)
            if needed_contact is None:
                print('There is no such contact in Addressbook')
            else:
                while self.a == 0:
                    new_phone = input('Kindly enter new phone number (11 digits, starts with 38)\n>>>: ')
                    if not new_phone.isdigit() and len(new_phone) != 11:
                        print('Incorrect number, there should be 11 digits without any other symbols')
                    else:
                        needed_contact['phone'].append(new_phone)
                        print('New phone number has been added')
                        self.a = 1

    def update_address(self):
        self.ua = 0
        if len(self.adressbk) == 0:
            print('The Addressbook is empty')
        else:
            contact_key = input("Input the contact name for which you would like to update the address\n>>>: ")
            needed_contact = self.adressbk.get(contact_key)
            if needed_contact is None:
                print('There is no such contact in Addressbook')
            else:
                while self.ua == 0:
                    new_address = input('Please enter a new address\n>>>: ')
                    if len(new_address) <= 50:
                        needed_contact['address'] = new_address
                        print('New address has been added')
                        self.ua = 1
                    else:
                        print('The address is too long, it should be up to 50 symbols only')

    def delete_record(self):
        if len(self.adressbk) == 0:
            print('The Addressbook is empty')
        else:
            contact_key = input("Enter the contact name of the record that should be deleted\n>>>: ")
            needed_contact = self.adressbk.get(contact_key)
            if needed_contact is None:
                print('There is no such contact in Addressbook')
            else:
                del self.adressbk[contact_key]
                print('Record has been deleted')

    def save_contacts_to_file(self):
        filename = input("Enter the file name to save\n>>>: ")
        with open(filename + '.bin', "wb") as file:
            pickle.dump(self, file)
            print('All records were saved')

    def download_contacts_from_file(self):
        filename = input("Enter the file name to load\n >>: ")
        with open(filename + '.bin', "rb") as file:
            saved_data = pickle.load(file)
            self.adressbk.update(saved_data.adressbk)
            print('All records were loaded')

    def find_some_contact(self):
        result = []
        symbols_to_find = input(
            "Enter the part of the name or the phone number in order to find the match\n>>>: ").lower()
        if len(self.adressbk) != 0:
            for contact in self.adressbk.values():
                contact_name = str(contact['name']).lower()
                contact_phone = str(contact['phone']).lower()
                if contact_name.find(symbols_to_find) >= 0 or contact_phone.find(symbols_to_find) >= 0:
                    result.append(contact)
                if result == []:
                    print("Sorry, there are not matching contacts")
            print('\nHere are the records that matches: ')
            for i in result:
                print('\n**********************')
                for key, value in i.items():
                    print(f"{key}: {value}")
        else:
            print('The Addressbook is empty')

    def days_to_birthday(self):
        result = []
        self.dtb = 0
        while self.dtb == 0:
            days = int(input('Enter the number of days\n>>>: '))
            if type(days) == int and days < 1001:
                self.dtb = 1
            else:
                print('We count the days in numbers and it should not be more than 1000\n>>>: ')
        if len(self.adressbk) != 0:
            self.today = datetime.now()
            self.future = self.today + timedelta(days)
            self.future_datetime = self.future.date()
            possible_bdate = [self.future_datetime.year, self.future_datetime.month, self.future_datetime.day]
            for contact in self.adressbk.values():
                if int(contact['bdate'][1]) == int(self.future_datetime.month) and int(contact['bdate'][2]) == int(
                        self.future_datetime.day):
                    result.append(contact)
            if result == []:
                print("No records with birthday in entered number of days\n")
            else:
                print('\nHere is the contact with birthday:')
                for i in result:
                    print('\n**********************************')
                    for key, value in i.items():
                        print(f"{key}: {value}")
        else:
            print('The Addressbook is empty\n')

    def print_all_contacts(self):
        if self.adressbk:
            for k, v in self.adressbk.items():
                print('\n**********************')
                for key, value in v.items():
                    print(f"{key}: {value}")
        else:
            print('The Addressbook is empty\n')

    def menu(self):
        menu = ('*************************** menu ***********************************\n'
                '1| Add record\n'
                '2| Update phone number to the existing contact\n'
                '3| Add phone number to the existing contact\n'
                '4| Update address in the existing contact\n'
                '5| Save all contacts to the file\n'
                '6| Download contacts from the file\n'
                '7| Search contact by the letters from name or numbers from phone\n'
                '8| Show all contacts on the screen\n'
                '9| Delete contact\n'
                '10| Find all contacts whose birthday falls in current number of days\n'
                '11| Exit to the main menu\n'
                '********************************************************************\n')

        return menu

    def menu_assistant(self):
        self.all = 0
        self.p = 0
        print(self.menu())
        while self.all == 0:
            os.system('cls')
            print(self.menu())
            command = input('Enter command>>>: ')
            try:
                if command == '1':
                    while self.p == 0:
                        name = input('Please enter the contact name\n>>>: ')
                        if name in self.adressbk.keys():
                            print('The contact with such name already exists, enter another name\n>>>: ')
                        else:
                            self.p = 1
                    while self.p == 1:
                        phone_new = input('Kindly enter new phone number (11 digits, starts with 38)\n>>>: ')
                        phone = []
                        if not phone_new.isdigit() and len(phone_new) != 11:
                            print('Incorrect number, there should be 11 digits without any other symbols\n>>>: ')
                        else:
                            phone.append(phone_new)
                            self.p = 2
                    while self.p == 2:
                        year = input('Enter the birth year (4 numbers)\n>>>: ')
                        month = input('Enter the birth month (number)\n>>>: ')
                        day = input('Enter the day of birth (number)\n>>>: ')
                        bdate = [year, month, day]
                        if int(bdate[0]) >= 1920 and int(bdate[0]) <= 2023 and int(bdate[1]) <= 12 and int(bdate[2]) <= 31:
                            if int(bdate[0]) % 4 == 0 and int(bdate[1]) == 2 and int(bdate[2]) > 29:
                                print('Incorrect date, check the number of days in February \n')
                            if int(bdate[0]) % 4 != 0 and int(bdate[1]) == 2 and int(bdate[2]) > 28:
                                print('Incorrect date, check the number of days in February\n')
                            else:
                                self.p = 3
                        else:
                            print('Incorrect date, be closer to reality\n')
                    while self.p == 3:
                        address = input('Enter the address\n>>>: ')
                        if len(address) <= 50:
                            self.p = 4
                        else:
                            print('he address is too long, it should be up to 50 symbols only\n')
                    while self.p == 4:
                        email = input('Please enter email\n>>>: ')
                        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
                        if re.match(pattern, email) is None:
                            print('Enter real email\n>>>: ')
                        else:
                            self.p = 5
                    record = {'name': name, 'phone': phone, 'email': email, 'bdate': bdate, 'address': address}
                    AddressBook.add_record(self, record)
                    self.p = 0
                    print('Records were added')

                elif command == '2':
                    AddressBook.update_phone(self)
                elif command == '3':
                    AddressBook.add_phone(self)
                elif command == '4':
                    AddressBook.update_address(self)
                elif command == '5':
                    AddressBook.save_contacts_to_file(self)
                elif command == '6':
                    AddressBook.download_contacts_from_file(self)
                elif command == '7':
                    AddressBook.find_some_contact(self)
                elif command == '8':
                    AddressBook.print_all_contacts(self)
                elif command == '9':
                    AddressBook.delete_record(self)
                elif command == '10':
                    AddressBook.days_to_birthday(self)
                elif command == '11':
                    AddressBook.save_contacts_to_file(self)
                    self.all = 1
                    return ('exit')
                else:
                    print('There is no such command in the list')
                input('\n<press Enter to continue>')

            except Exception as e:
                print(f'{e}incorrect input, try again')
                input('<press Enter to continue>')
                continue


def main():
    ab = AddressBook()
    ab.menu_assistant()


if __name__ == "__main__":
    main()
