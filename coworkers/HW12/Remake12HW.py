import re
import os
from collections import UserDict
from datetime import datetime
import csv

from colorit import *


os.chdir(r"C:\Users\Admin\Desktop\TestCSV") # зминыв папку, бо не зручно було коли файл зберигався незрозумило куди и в яку папку



class Error(Exception):  #власне виключення
     pass
    #  def __str__(self) -> str:
    #       return "\n \nSomething went wrong\n Try again!\n"



class Field:
    
    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        return self._value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):   #клас для створення поля name

    def __str__(self) -> str:
        self._value : str
        return self._value.title()
    

class Phone(Field):   #клас для створення поля phone
    
    @staticmethod   #метод який не звязаний з класом
    def verify(number):  #перевирка номеру телефона
        number = re.sub(r"[\-\(\)\+\ a-zA-Zа-яА-я]", "", number)
        try:
            if len(number) == 12:
                number = "+" + number
            elif len(number) == 10:
                number = "+38" + number
            elif len(number) == 9:
                number = "+380" + number
            else:
                number = False
                raise Error
        except Error:
            print(color("\nSomething went wrong\n Try again!\n", Colors.green))
        
        if number:
            return number
        else:
            return ""


    def __init__(self, value) -> None:
        self._value = Phone.verify(value)

    @Field.value.setter
    def value(self, value):
        self._value =Phone.verify(value)


class Birthday:

    @staticmethod   #метод який не звязаний з класом
    def verify_date(birth_date: str):
        try:
            birthdate = re.findall(r"\d{4}\.\d{2}\.\d{2}", birth_date)
            if bool(birthdate) == False:
                raise Error
        except Error:
            print(color("\nYou enter wrong date.\nUse this format - YYYY.MM.DD \nTry again!\n", Colors.purple))

        if birthdate:
            return birthdate[0]
        else:
            return ""

    def __init__(self, birthday) -> None:
        self.__birthday = self.verify_date(birthday)

    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self,birthday):
        self.__birthday = self.verify_date(birthday)

    def __repr__(self) -> str:
        return self.__birthday
    
    def __str__(self) -> str:
        return self.__birthday



class Record:   #клас для запису инфи
    def __init__ (self, name : Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):  # додати телефон
        self.phones.append(phone)

    def remove_phone(self, phone):  # видалити телефон
        phone = Phone(phone)
        for ph in self.phones:
            if ph == phone:
                self.phones.remove(ph)

    def change_phone(self, oldphone, newphone): # зминити телефон користувача 
        oldphone = Phone(oldphone)
        newphone = Phone(newphone)

        for ph in self.phones:
            if ph == oldphone:
                self.phones.remove(oldphone)
                self.phones.append(newphone)

    def days_to_birthday(self):   #функция яка показуе скильки днив до наступного др
                                  # потрибно допрацювати
        try:
                
            if str(self.birthday) == None:
                return None
            
            current = datetime.now().date()
            current : datetime
            user_date = datetime.strptime(str(self.birthday), "%Y.%m.%d")
            user_date: datetime
            user_date = user_date.replace(year=current.year).date()

            if user_date < current:
                user_date = user_date.replace(year= current.year +1)
                res = user_date - current

                return color(f"{res.days} days before next birthday", Colors.purple)
            else:
                res = user_date - current
                return color(f"{res.days} days before next birthday", Colors.purple)
        except ValueError:
            print(color("You set wrong date. Try again set new date in format YYYY.MM.DD", Colors.red))
            return ""
    def __repr__(self) -> str:
        return f"Phone - {self.phone}, Birthday - {self.birthday}"

    

class AdressBook(UserDict): #адресна книга

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def generator(self): # генератор з yield
        for name, info in self.data.items():
            yield color(f"{name} has phone {info}",Colors.green)

    
    def iterator(self, value):  # функция яка показуе килькисть контактив яку введе користувач
        value = value
        gen = self.generator()
        try:
            if value > len(self.data):
                raise Error
        except:
            print(color("You set big value, list has less users. Try again.\n", Colors.red))

        while value > 0:
            try:
                print(next(gen))
                value -= 1
            except StopIteration:
                print(color(f"Try enter value less on {value}. Dict has {len(self.data)} contacts",Colors.purple))
                return ""
        return color("Thats all!",Colors.orange)
    

    
    def save(self):     #функция збереження даних адресбук у csv файл
        if len(self.data) == 0:
            print(color("Your AddressBook is empty",Colors.red))
        
        with open("savebook.csv", "w", newline="") as file:
            fields = ["Name", "Info"]
            writer = csv.DictWriter(file, fields)
            writer.writeheader()
            for name, info in self.data.items():
                name :str
                writer.writerow({"Name": name.title(), "Info": str(info)})
            return color("Succesfull save your AddressBook",Colors.green)



    def load(self):  # функция яка завантажуе контакти з збереженого csv файлу, якшо такого нема буде про це повидомлено
        try: 
            with open("savebook.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    saved = {row["Name"]: row["Info"]}
                    self.data.update(saved)

                print(color("\nSuccesfull load saved AddressBook", Colors.purple))
        except:
            print(color("\nDont exist file with saving contacts",Colors.blue))
        return ""
        




    def find(self, value: str):     #функция для пошуку по имя або телефону
        value = value.lower()
        res = ""
        fail = color("Finder not find any matches in AddressBook",Colors.red)
        for name, info in self.data.items():
            if value in name.lower() or value in str(info).lower():
                res += (f"Find similar contacts {name.title()} {str(info).title()}\n")
        return color(res.strip(), Colors.orange) if len(res) > 0 else fail
            

            



#ПЕРЕВИРКА СКРИПТА
name = Name("Dima")
phone = Phone("0993796625")
birth = Birthday("2001.08.12")
rec = Record(name, phone, birth)
ad = AdressBook()
ad.add_record(rec)
#=============================================================================
name1 = Name("Benderovec")
phone1 = Phone("0993790447")
birth1 = Birthday("2001.08.12")
rec1 = Record(name1, phone1, birth1)
ad.add_record(rec1)
#=============================================================================
# print(rec.days_to_birthday())
#=============================================================================
name2 = Name("Diana")
phone2 = Phone("099797484")
birth2 = Birthday("2003.04.01")
rec2 = Record(name2, phone2, birth2)
#============================================================================
ad.add_record(rec2)
print(ad.load())

# print(ad.iterator(6))
# print(ad.find("test"))
