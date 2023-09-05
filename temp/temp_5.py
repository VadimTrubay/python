# import csv
# with open('eg56s.csv', 'w', newline='') as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
# with open('egg45s.csv', newline='') as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(', '.join(row))

# import json
# def write_contacts_to_file(filename, contacts):
#     with open(filename, "w") as fh:
#         c = {'contacts': [contacts] for i in contacts}
#         json.dump(c, fh)
#
# def read_contacts_from_file(filename):
#     with open(filename, "r") as fh:
#         unpacked = list(json.load(fh))
#     return unpacked
#
# print(write_contacts_to_file('qq54.json', {
#                         "name": "Allen Raymond",
#                         "email": "nulla.ante@vestibul.co.uk",
#                         "phone": "(992) 914-3792",
#                         "favorite": False}))

# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Hello i am {self.name} and {self.age} years old'
#
# bill = Human('bill', 12)
# print(bill)

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

# @property
# def y(self):
#     return self.__y
#
# @y.setter
# def y(self, y):
#     if (type(y) == int) or (type(y) == float):
#         self.__y = y

# def __str__(self):
#     return f"Point({self.x},{self.y})"


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
#
#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y
#
#     def __add__(self, vector):
#         vector = vector2 + vector1
#         return vector

# def __sub__(self, vector):
#     return

# def __str__(self):
#     return f"Vector({self.coordinates.x},{self.coordinates.y})"

# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# vector3 = vector2 + vector1
# vector4 = vector2 - vector1

# print(vector3)  # Vector(11,20)
# print(vector4)  # Vector(9,0)

# class A:
#     def __str__(self):
#         return f"{a}"
#
# a = A()
# print(a)

# a = [{"name": "John", "age": 35, "city": ["San Francisco"]},
#      {"name": "Zoe", "age": 34, "city": ["Los Angeles"]}]
#
# for i in a:
#     for j in i:
#         b = j.replace("'", '"')
#         print(b)
# from collections import UserDict
# class Iterable(UserDict):
#     def __init__(self):
#         super().__init__()
#         self.current_value = self.data[]
#         self.data = {"1": "1", "2": "3", 4: 5, 6: 7, 8: 9}
#
#     def __next__(self):
#         if self.current_value < len(self.data):
#             self.current_value += 1
#             return self.current_value
#         raise StopIteration
#     def __iter__(self):
#         return self
# c = Iterable()
# for i in c:
#     print(i)

# Функции-генераторы
# Функция iter()

# class Phone:
#     def __init__(self, p):
#         self.__private_phone = None
#         self.p = p
#
#     @property
#     def p(self):
#         return self.__private_phone
#
#     @p.setter
#     def p(self, value: str):
#         if value.isdigit():
#             self.__private_phone = value
#         else:
#             raise ValueError('Invalid value')
#
#
# p = Phone(input('enter:   '))
# print(p.p)

# import re
# match = re.fullmatch(r'[+][3][8][0]\d{9}', '+380965678667')
# res = True if match else False
# print(res)


# alist = ['Python', 'Java', 'C', 'C++', 'CSharp']
# def list_items():
#     count = 0
#     a = []
#     for item in alist:
#         a.append(item)
#         count += 1
#         if count == 2:
#             yield a
#             list_items()
#
# print(next(list_items()))
# print(next(list_items()))
# a = {"vad": ["+380(96)567-86-67", "06.08.1982"], "vika": ["+380(96)266-50-09", "09.07.1984"],
#      "nik": ["+380(99)987-85-96", "15.03.2010"], "ret": ["+380(96)266-50-09", "09.07.1984"],
#      "hjk": ["+380(96)266-50-09", "09.07.1984"], "rgf": ["+380(96)266-50-09", "09.07.1984"],
#      "kjl": ["+380(96)266-50-09", "09.07.1984"], "iiu": ["+380(96)266-50-09", "09.07.1984"]}
# def test():
#     while True:
#         count = 0
#         for k, v in a.items():
#             print(k, v)
#             count += 1
#             if count == 3:
#                 yield
# print(next(test()))
# print(next(test()))
# print(next(test()))

# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return self.__class__.__name__
# cat = Cat('vasia')
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#     def __len__(self):
#         return len(self.__coords)
# p = Point(1, 2, 4, 5, 6, 7, 8, 9)
# print(len(p))

# import json
# def write_contacts_to_file(filename, contacts):
#     with open(filename, "w") as fh:
#         c['contacts'] = [contacts]
#         json.dump(c, fh)
#
# def read_contacts_from_file(filename):
#     with open(filename, "r") as fh:
#         unpacked = list(json.load(fh))
#     return unpacked

# print(write_contacts_to_file('filename.txt', {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }))

# from random import randrange
#
#
# from random import randrange

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y
#
#     def __str__(self):
#         return f"Point({self.x},{self.y})"
#
#
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
#
#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y
#
#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))
#
#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))
#
#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )
#
#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5
#
#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"
#
#     def __eq__(self, vector):
#         return self.len() == vector.len()
#
#     def __ne__(self, vector):
#         return self.len() != vector.len()
#
#     def __lt__(self, vector):
#         return self.len() < vector.len()
#
#     def __gt__(self, vector):
#         return self.len() > vector.len()
#
#     def __le__(self, vector):
#         return self.len() <= vector.len()
#
#     def __ge__(self, vector):
#         return self.len() >= vector.len()
#
#
# class Iterable:
#     def __init__(self, max_vectors, max_points):
#         self.current_index = 0
#         self.vectors = []
#         for _ in range(max_vectors):
#             self.vectors.append(Vector(Point(randrange(0, max_points), randrange(0, max_points))))
#     def __next__(self):
#         try:
#             result = self.vectors[self.current_index]
#             self.current_index += 1
#             return result
#         except IndexError:
#             raise StopIteration
#
#
# class RandomVectors:
#     def __init__(self, max_vectors, max_points):
#         self.max_vectors = max_vectors
#         self.max_points = max_points
#
#     def __iter__(self):
#         return Iterable(self.max_vectors, self.max_points)
#
#
# vectors = RandomVectors(5, 10)
# for vector in vectors:
#     print(vector)


# import csv
# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'w', newline='') as fh:
#         field_names = ["name", "email", "phone", "favorite"]
#         writer = csv.DictWriter(fh, fieldnames=field_names)
#         writer.writeheader()
#         for i in contacts:
#             writer.writerow({'name': i['name'], 'email': i['email'], 'phone': i['phone'], 'favorite': i['favorite']})
#
#
# def read_contacts_from_file(filename):
#     with open(filename, newline='') as fh:
#         reader = csv.DictReader(fh)
#         a = []
#         for row in reader:
#             a.append(
#                 {'name': row['name'], 'email': row['email'], 'phone': row['phone'], 'favorite': bool(row['favorite'])})
#         return a
# write_contacts_to_file()
# read_contacts_from_file()

# def decorator(func):
#     def inner():
#         try:
#             func()
#         except Exception as e:
#             print(f"Error {e}")
#     return inner
#
# @decorator
# def my_func():
#     while True:
#         a = int(input("Enter int: "))
#         if a:
#             print('ok')
#         else:
#             raise Exception
#
# my_func()
# x = int(input("Enter x: "))

# f = lambda x, y: x + y
# print(f(4, 4))

# import pickle
#
# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite
#
#
# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         self.contacts = contacts
#         if self.contacts is None:
#             self.contacts = []
#
#     def save_to_file(self):
#         with open(self.filename, "wb",) as fh:
#             pickle.dump(persons, fh)
#
#     def read_from_file(self):
#         with open(self.filename, "rb") as fh:
#             unpacked = pickle.load(fh)
#         return unpacked

# class Char:
#     def move(self):
#         print("Move")
#     def speed(self):
#         print("Speed")
#
# class Enemy(Char):
#     pass
#
# enemy = Enemy()
# enemy.move()

# class A:
#     a = 5
# class B(A):
#     b = 9
# class C:
#     a = 100
# class D(B, C):
#     b = 1
# asd = D()
# print(asd.a)


# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
# print(total(10, 1, 2, 3, extra_number=50))

# def printMax(x, y):
#     """Выводит максимальное из двух чисел.
#     Оба значения должны быть целыми числами."""
#     x = int(x)  # конвертируем в целые, если возможно
#     y = int(y)
#     if x > y:
#         print(x, 'наибольшее')
#     else:
#         print(y, 'наибольшее')
#
#
# printMax(3, 5)
# print(printMax.__doc__)

#pagination
# a = ['1', '2', '3', '4', '5', '6', '7', '8']
# def func():
#     count = 0
#     temp = []
#     for i in a:
#         count += 1
#         temp.append(i)
#         if count == 3:
#             yield temp
#             count = 0
#             temp = []
#             print(input("enter"))
#     else:
#         yield temp
#
# def generat(func):
#     for i in func:
#         print(i)
#
# generat(func())






