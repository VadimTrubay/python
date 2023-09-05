# from collections import Counter, defaultdict
#
# text = "There are many variations of passages of Lorem Ipsum available, " \
#        "but the majority have suffered alteration in some form, " \
#        "by injected humour, or randomised words which don't look even " \
#        "slightly believable"


# def get_chars_in_text(text):
#     dict_chars = {}
#     for i in text:
#         num = dict_chars.get(i)
#         if num:
#             dict_chars[i] = num + 1
#         else:
#             dict_chars[i] = 1
#     return dict_chars
# print(get_chars_in_text(text))
# counter = Counter(text)
# print(counter.most_common())

# def get_word_list(text):
#     word_list = text.split(" ")
#     word_dict = {}
#     for i in word_list:
#         word = word_dict.get(i[0])
#         if word:
#             word.append(i)
#         else:
#             word_dict[i[0]] = [i]
#     return word_dict
# print(get_word_list(text))

# def get_word_list(text):
#     word_list = text.split(" ")
#     word_dict = defaultdict(list)
#     for i in word_list:
#         word_dict[i[0]] = i
#     return word_dict
# print(get_word_list(text))

# from collections import deque
# def main():
#     d = deque(maxlen=5)
#     for i in range(10):
#         d.appendleft(i)
#     print(d)
#     start = d.popleft()
#     end = d.pop()
#     print(start, end)
# main()

# TODO really important code
#
# from collections import deque
# def main():
#     user_inputs = deque(maxlen=20)
#     while True:
#         user_input = input('>>>>>: ')
#         user_inputs.append(user_input)
#         if user_input == 'exit':
#             break
#     print('good bye')
#     print(f'steps: {user_inputs}')
# main()

# def get_numbers(x):
# num = []
# for i in range(x):
#     n = i ** 2
#     if not n % 2:
#         num.append(n)
# print(num)
# get_numbers(12)

# def get_numbers(x):
#     print([i ** 2 for i in range(x) if not i % 2])
# get_numbers(12)

# a = 'vad 0965678667'
# print(a.split(' '))

# def add_contact(contact: str) -> str:
# dict_contact = {}
# while True:
#     contact = input('>>>>>').split(' ')
#     print(len(dict_contact))
#     dict_contact[contact[0]] = contact[1]
#
#     print(dict_contact)
# print(add_contact(input('>>>>>')))

# DEFAULT_DISCOUNT = 0.05
# def get_discount_price_customer(price, customer):
#     if "discount" in customer.keys():
#         result_price = price * (1 - customer["discount"])
#         return result_price
#     else:
#         finally_price = price * (1 - DEFAULT_DISCOUNT)
#         return finally_price
# print(get_discount_price_customer(10, {"name": "Boris", "discount": 0.15}))

# def caching_fibonacci():
#     cache = {}
#     def fibonacci(n):
#         if n not in cache:
#             if n == 0:
#                 result = 0
#             elif n == 1:
#                 result = 1
#             else:
#                 result = fibonacci(n-1) + fibonacci(n-2)
#             cache[n] = result
#             return result
#         return cache[n]
#     return fibonacci

# def discount_price(discount):
#     return A[discount]
#
# def cost_25(price):
#     return price * (1 - 0.25)
# def cost_20(price):
#     return price * (1 - 0.20)
# def cost_15(price):
#     return price * (1 - 0.15)
# def cost_10(price):
#     return price * (1 - 0.10)
# def cost_05(price):
#     return price * (1 - 0.05)
# def cost_0(price):
#     return price
#
# A = {
#     0.25: cost_25,
#     0.20: cost_20,
#     0.15: cost_15,
#     0.10: cost_10,
#     0.05: cost_05,
#     0: cost_0
# }
# price = 100
#
# cost_25 = discount_price(0.25)
# cost_20 = discount_price(0.20)
# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)
# cost_0 = discount_price(0)
#
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))


# def format_phone_number(func):
#     def inner(*args):
#         result = func(*args)
#         if len(result) == 10:
#             return '+38' + result
#         elif len(result) == 12:
#             return '+' + result
#     return inner
#
#
# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone
# print(sanitize_phone_number("38050-111-22-22"))

# def interval_generator(x, y):
#     while x <= y:
#         yield x
#         x += 1
# a = interval_generator(5, 7)
# print(next(a))
# print(next(a))
# print(next(a))

# import re
# def generator_numbers(string):
#     for i in re.findall(r'\d+', string):
#         yield i
# def sum_profit(string):
#     result = 0
#     for i in generator_numbers(string):
#         result += int(i)
#     print(result)
#     return result

# def normal_name(list_name):
#     a = []
#     for i in map(lambda x: x.capitalize(), list_name):
#         a.append(i)
#     return a

# def get_emails(list_contacts):
#     mail_list = []
#     for i in map(lambda x: x["email"] , list_contacts):
#         mail_list.append(i)
#     return mail_list

# def positive_values(list_payment):
#     result = [i for i in filter(lambda x: x >= 0, list_payment)]
#     print(result)
#     return result
#
# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x.islower(), some_str):
#     print(i)

# def get_favorites(contacts):
#     a = [i for i in filter(lambda x: x["favorite"] is True , contacts)]
#     return a

# from functools import reduce
# def sum_numbers(numbers):
#     result = reduce((lambda x, y: x + y), numbers)
#     return resul

# from functools import reduce
# def amount_payment(payment):
#     result = [i for i in payment if i > 0]
#     a = reduce((lambda x, y: x + y), result)
#     return a
# def calculator(number1, operator, number2):
#     if operator == '+':
#         return number1 + number2
#     elif operator == '-':
#         return number1 - number2
#     elif operator == '/':
#         if number2 == 0:
#             return "Нельзя делить на 0!"
#         else:
#             return number1 / number2
#     elif operator == '*':
#         return number1 * number2


# def calculator(number1, operator, number2):
#     try:
#         return eval(str(number1)+operator+str(number2))
#     except ZeroDivisionError:
#         return "Нельзя делить на 0!"
#
#
# print(calculator(2, '/', 0))

# class Person:
#     l = []
#     def __init__(self, name, age, hobbies):
#         self.name = name
#         self.age = age
#         self.hobbies = hobbies
#         self.l.append(self.name)
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_hobbies(self):
#         return self.hobbies
# vad = Person('vad', 40, 'it')
# nik = Person('nik', 13, 'it')
# print(vad.name)
# print(Person.l)
# print(nik.name, nik.age)

# from datetime import datetime
# class Animals:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def get_birthday_year(self) -> int:
#         return datetime.now().year - self.age
#
#     def make_sound(self):
#         pass
#
#     def eat(self):
#         print('Eating')
#
#
# class Dog(Animals):
#
#     def get_birthday_year(self) -> int:
#         return datetime.now().year - self.age
#
#     def make_sound(self):
#         print('woof')
#
#     def jamp(self):
#         print('jamp')
#
#     def play(self):
#         print('play with animation')
#
#
# class Cat(Animals):
#     def __init__(self, name: str, age: int, color: int):
#         super().__init__(name, age)
#         self.color = color
#
#     def get_birthday_year(self) -> int:
#         return datetime.now().year - self.age
#
#     def make_sound(self):
#         print('meow')
#
#
# class Bird(Animals):
#
#     def get_birthday_year(self) -> int:
#         return datetime.now().year - self.age
#
#     def make_sound(self):
#         print('chirp')
#
#
# dog = Dog('rex', 5)
# cat = Cat('gil', 8, 'red')
# bird = Bird('rich', 3)
#
# print(cat.color)

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#
# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
#     def info(self):
#         return {'name': self.name, 'age': self.age, 'address': self.address}
#
#
# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)
#
#     def say(self):
#         return "Woof"
#
#     def who_is_owner(self, owner):
#         return self.owner
#
# owner = Owner('vad', 34, 'vvvvvvvvv')
# dog = Dog('rex', 4, 'drgdrg', owner)
# print(dog.who_is_owner(owner))

# class Character:
#     hp = 100
#     mp = 100
#
#     def __init__(self, name, x, y):
#         self.left_hand = None
#         self.right_hand = None
#         self.name = name
#         self.x = x
#         self.y = y
#
#     def pick_weapon(self, weapon):
#         if self.left_hand is None:
#             self.left_hand = weapon
#         elif self.right_hand is None:
#             self.right_hand = weapon
#         else:
#             print('full weapon')
#
#     def show_weapon(self):
#         return self.left_hand, self.right_hand
#
#     def moving(self, name):
#         print('im moving')
#
#     def identify(self):
#         print(self.name)
#
#     def die(self):
#         return self.left_hand, self.right_hand
#     def damage_left(self):
#         self.left_hand.kick_ass()
#     def damage_right(self):
#         self.right_hand.kick_ass()
#
# class Weapon:
#     def __init__(self):
#         self.damage = 10
#     def kick_ass(self):
#         return self.damage
#
#
# class Knife(Weapon):
#     def __init__(self):
#         self.damage = 5
#
#     def thow(self):
#         return self.damage - 2
#     def kick_ass(self):
#         print('chick')
#         return self.damage
#
#
# class Sword(Weapon):
#     def __init__(self):
#         self.damage = 15
#     def kick_ass(self):
#         print('bik')
#         return self.damage
#
# class Axe(Weapon):
#     def __init__(self):
#         self.damage = 20
#     def kick_ass(self):
#         print('trick')
#         return self.damage
# class Gun(Weapon):
#     def __init__(self):
#         self.damage = 20
#     def kick_ass(self):
#         print('Baam')
#         return self.damage
#
# char1 = Character('vad', 0, 0)
# char2 = Character('nik', 0, 0)
# knife = Knife()
# sword = Sword()
# print(knife.kick_ass())
# print(sword.kick_ass())
# char1.pick_weapon(knife)
# char1.pick_weapon(sword)
# print(char1.left_hand)
# print(char1.damage_left())
# print(char1.damage_right())
# left_hand, right_hand = char1.die()

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#
# class Cat(Animal):
#     def say(self):
#         return "Meow"
#
#
# class Dog(Animal):
#     def say(self):
#         return "Woof"
#
# class CatDog(Cat, Dog):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"
#
# class DogCat(Dog, Cat):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# def is_subset(list1, list2):
# 	return True if set(list1) <= set(list2) else False
#
# print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6])) #➞ True

# class Record:
#     def __init__(self, name):
#         self.name = name
# class Name:
#     value = 'vad'
# record = Record(Name())
# print(record.name.value)


# from collections import UserDict
# class ValueSearchableDict(UserDict):
#     def has_in_values(self):
#         return self.data
#
# as_dict = ValueSearchableDict()
# as_dict['a'] = 1
# print(as_dict.has_in_values())  # True
# print(as_dict.has_in_values(2))  # False

# from collections import UserList
# class CountableList(UserList):
#     def sum(self):
#         return sum(map(lambda x: int(x), self.data))
#
# countable = CountableList([1, '2', 3, '4'])
# countable.append('5')
# countable.sum()  # 15
#
#
# from collections import UserDict
# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         keys = []
#         for key in self.data:
#             if self.data[key] == value:
#                 keys.append(key)
#         return keys

# TODO: проверка на ввод числа
# def input_number():
#     while True:
#         try:
#             num = input("Enter integer number: ")
#             return int(num)
#         except Exception:
#             print(f'"{num}" is not a number. Try again')
# num = input_number()
# print(num)

# TODO: проверка на ввод имени с большой буквы не менее 3 символа
# import string
# class NameTooShortError(Exception):
#     pass
# class NameStartsFromLowError(Exception):
#     pass
# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 3:
#         raise NameTooShortError
#     if name[0] not in string.ascii_uppercase:
#         raise NameStartsFromLowError
#
# while True:
#     try:
#         name = enter_name()
#         break
#     except NameTooShortError:
#         print('Name is too short, need more than 3 symbols. Try again.')
#     except NameStartsFromLowError:
#         print('Name should start from capital letter. Try again.')

# l = [int(input(f'Enter number {i + 1} >: ')) for i in range(5)]
# print(l)

# class Contacts:
#     current_id = 1
#
#     def __init__(self):
#         self.contacts = []
#
#     def list_contacts(self):
#         return self.contacts
#
#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1
#
#     def get_contact_by_id(self, id):
#         for i in self.list_contacts():
#             if i['id'] == id:
#                 return i
#         return None

# class Contacts:
#     current_id = 1
#
#     def __init__(self):
#         self.contacts = []
#
#     def list_contacts(self):
#         return self.contacts
#
#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1
#
#     def get_contact_by_id(self, id):
#         result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
#         return result[0] if len(result) > 0 else None
#
#     def remove_contacts(self, id):
#         for i in self.contacts:
#             if i['id'] == id:
#                 self.contacts.remove(i)

# contact = Contacts()
# contact.add_contacts('vad', '34534', 'fs@43', True)
# contact.add_contacts('ret', '67u435', 'ewr@4ewr', True)
# contact.add_contacts('435', 'fbcb', 'egnwr@hjmr', True)
# contact.add_contacts('rfgbt', '6,', 'ewr@4ewr', True)
# print(contact.list_contacts())
# print(contact.get_contact_by_id(1))
# print(contact.get_contact_by_id(2))
# print(contact.get_contact_by_id(3))
# print(contact.get_contact_by_id(4))
# contact.remove_contacts(2)
# print(contact.list_contacts())

# user_input = input('>Enter_command: ')
# a = user_input.split(' ')
# print(a)

# a = {'q': ['1', '2']}
# for i in a.items():
#     print(i)

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y
#     @property
#     def x(self):
#         return self.__x
#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x
#     @property
#     def y(self):
#         return self.__y
#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y
# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates
#
#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value
#
#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

# vector = Vector(Point(1, 10))
# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10
# print(vector.coordinates)  # 10
# vector[0] = 16  # Устанавливаем координату x вектора в 10
# print(vector[0])  # 10
# print(vector[1])  # 10

# def decor(func):
#     def wrapper(x, y):
#         try:
#             func(x, y)
#         except ValueError:
#             return print('Error')
#
#     return wrapper
#
# @decor
# def main(x, y):
#     return x / y

# print(main(12, 0))

# class Person:
#     def __init__(self, name):
#         self.__name = None
#         self.name = name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         if (type(name) == str) and (len(name) > 0):
#             self.__name = name
# person = Person('123')
# print(person.name)  # None

# def get_input():
#     a = input('dsg: ')
#     return a
# def a():
#     print('a')
# def b():
#     print('b')
# dispatch = {'go': a, 'stop': b} # Note lack of parens for funcs
# dispatch[get_input()]()

