# class Geom:
#     pass
#
#
# class Point(Geom):
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#
#
# p = Point(2, 3)
# p.x = 3



#  operator math/case
# a = 'left'
#
# match a:
#     case 'top' | 'left':
#         print('top')
#     case 'left':
#         print('left')
#     case _:
#         print('any')
#
# print('check finally')


#  use operator match/case
# a = 'hgjhh'
# match a:
#     case str() | 'top' as b if len(b) > 4:
#         print(f'str: {b}')
#     case int() | float() as b if 0 < b < 9:
#         print(f'number: {b}')
#     case _:  # wildcard
#         print('other command')


# cmd = ('trubay', 'python', 1999, 1, 4)
# match cmd:
# case tuple() as book:
#     print(f'book: {book}')
# case a, b, c:
#     print(f'book: {a}, {b}, {c}')
# case (str() as a, b, int() | float() as c, *_) if len(cmd) < 5:
#     print(f'book: {a}, {b}, {c}')
# case int() | float() as b if 0 < b < 9:
#     print(f'number: {b}')
# case _:  # wildcard
#     print('other command')


# req = {'url': 'http://vad.ua', 'method': 'get', 'timeout': 50}
#
# match req:
#     case {'url': url, 'method': str(method) | int(method)}:
#         print(f'request: {url}, method: {method}')
#
#     case _:  # wildcard
#         print('other command')

# req = {'id': 2, 'access': True,
#        'info': ['23.12.09', {'login': '123', 'email': 'vad@fd.r'}, True]}
#
# match req:
#     case {'access': access, 'info': [_, {'email': email}, *_]}:
#         print(f'access: {access}, email: {email}')
#
#     case _:  # wildcard
#         print('other command')

# import re

# text = "+38(096)567-86-67"
# text = 'odessa vinnisa yman'
# text = 'gooogle, Google, gooooogle'
# match = re.findall(r'[Mm]a[Pp]', text)  #  Map, map, MaP, map
# match = re.findall(r'[0-9][^0-9]', text)  # ^ not
# match = re.findall(r'[a-zA-Z0-9]', text)  # interval
# match = re.match(r'\+380\d{9}', text)  # i+380965678667
# match = re.findall(r'[Mm]a[Pp]', text)  #
# match = re.match(r'^\+38\(0\d{2}\)\d{3}-\d{2}-\d{2}$', text)
# match = re.split(r'[\n,:;]+', text)
# match = re.sub(r'\s*(\w+)\s*', r'<option>\1</option>\n', text)
# print(match)


# class Point:
#     color = 'black'
#     circle = 4
#
#     def __init__(self, x=0, y=0): # initialize method
#         self.x = x
#         self.y = y
#
#     def __del__(self):  # delete method
#         print(f'delete obj {str(self)}')
#
#     def get_cords(self):
#         return self.x, self.y
#
#
# a = Point()
# print(a.get_cords())


# def singleton(cls):
#     instances = {}
#     def getinstance(x):
#         if cls not in instances:
#             instances[cls] = cls(x)
#         return instances[cls]
#     return getinstance
#
# @singleton
# class Database:  # pattern SINGLETON!!!
#     __instanse = None
#
#     def __new__(cls, *args, **kwargs): # initialize method
#         if cls.__instanse is None:
#             cls.__instanse = super().__new__(cls)
#         return cls.__instanse
#
#     def __del__(self):
#         Database.__instanse = None
#
#     def __init__(self, x): #constructor method
#         self.x = x
#         print(x)
#
# a = Database(3)
# b = Database(4)
#
# print(id(a), id(b))


# import random

# class Singleton:
#     """Classic singleton"""
#
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(Singleton)
#         return cls.__instance
#
#     def __init__(self, n):
#         self.n = n
#
# a = Singleton(5)
# b = Singleton(6)
#
# print(a.n, b.n)



# class Vector: # @classmethod
#     MIN = 0
#     MAX = 20
#
#     @classmethod
#     def valid(cls, arg):
#         return cls.MIN <= arg <= cls.MAX
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.valid(x) and self.valid(y):
#             self.x = x
#             self.y = y
#
#     def __str__(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm(a, b):  # @staticmethod
#         return a ** b
#
# v1 = Vector(20, 6)
#
# print(v1.x, v1.y)
#
# print(v1.norm(2, 2))

# private and protected method
# from accessify import private, protected
# class Point:
#     def __init__(self, x, y): # initialize method
#         if isinstance(x, int) and isinstance(y, int):
#             self.__x = x
#             self.__y = y
#
#     @private
#     @classmethod
#     def check_value(cls, x):
#         return type(x) in (int, float)
#
#     def get_value(self):
#         return self.__x, self.__y
#
#     def set_value(self, x, y):
#         if self.check_value(y) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError('not int')
#
# a = Point(1, 2)
# # print(a.get_value())
# print(a.set_value(3, 4))
# # print(a.get_value())
# print(a.check_value(56))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getattribute__(self, item): # вызывается при обращении к атрибуту через экземпляр класса
#         if item == 'x':
#             raise ValueError('access not')
#         return  object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):  # вызывается при присвоении атрибуту какого то значения
#         if key == 'z':
#             raise ValueError('access not')
#         return object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):  # вызывается при обращении к несуществующему атрибуту экземпляра класса
#         return False
#
#     def __delattr__(self, item):  # вызывается при удалении атрибута экземпляра класса
#         object.__delattr__(self, item)
#
# a = Point(1, 3)
# a.x = 2
# a.z = 6
# print(a.r)

# pattern MONOSTATION
# class Data:
#     __attr = {
#         'name': 'vad',
#         'age': 22
#     }
#
#     def __init__(self):
#         self.__dict__ = self.__attr
#
# a = Data()
# b = Data()

#@property and @value.setter
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     # def __str__(self):
#     #     return self.__name, self.__age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__age = value
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
# a = Person('vad', 34)
# print(a.age)
# a.age = 99
# print(a.age)
# print(a.name)
# a.name = 'qwery'
# print(a.name)
# del a.name
# print(a.age, a.name)


# descriptor
# class Integer:
#
#     @classmethod
#     def varify(cls, cord):
#         if type(cord) != int:
#             raise TypeError('error type')
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.varify(value)
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
# p = Point3D(1, 2, 3)
#
# print(p.__dict__)
# print(p.x)


# dunder method __call_

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, step=1, *args, **kwargs):
#         print("__call__")
#         self.__counter += step
#         return self.__counter
#
# c = Counter() # dunder method __call_ вызывается
# # в момент вызова класса через скобки()(функтор)
# c()
# c(5)
# c()
# print(c.__dict__)


# # dunder method __str__, __repr__, __len__, __abs__
# class Points:
#     def __init__(self, *args):
#         self.coords = list(args)
#
#     def __str__(self):
#         return f"{type(self.coords)}"
#
#     def __len__(self):
#         return len(self.coords)
#
#     def __abs__(self):
#         return list(map(abs, self.coords))
#
# p = Points(-1, 2, -3, 5)
# print(len(p))
# print(p)
# print(abs(p))



# class Clock:
#     def __init__(self, *args):
#         self.coords = list(args)
#
#     def __str__(self):
#         return f"{type(self.coords)}"
#
#     def __len__(self):
#         return len(self.coords)
#
#     def __abs__(self):
#         return list(map(abs, self.coords))
#
#     def __abs__(self):
#         return list(map(abs, self.coords))
#
# p = Points(-1, 2, -3, 5)
# print(len(p))
# print(p)
# print(abs(p))

# __add__"+", __sub__"-", __mul__"*", __truediv__"/"
# class Clock:
#     __DAY = 86400  # quantity seconds in day
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('has been int')
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"
#
#     @classmethod
#     def __get_formated(self, x):
#         return str(x).rjust(2, '0')
#
#     def __add__(self, other: int):
#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds
#         return Clock(self.seconds + sc)
#
# c1 = Clock(1000)
# c2 = Clock(2000)
# c3 = Clock(3000)
# c3 = c1 + c2 + c3
# print(c3.get_time())

# __eq__"==", __ne__"!=", __lt__"<", __le__"<=", __gt__">", __ge__">="
# class Clock:
#     __DAY = 86400  # quantity seconds in day
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('has been int')
#         self.seconds = seconds % self.__DAY
#
#     @classmethod
#     def __verify_data(cls, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('int or Clock')
#
#         return other if isinstance(other, int) else other.seconds
#
#     def __eq__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds == sc  #==
#
#     def __lt__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds < sc  #<
#
# c1 = Clock(2000)
# c2 = Clock(3000)
#
# print(c1 < c2)

# class Foo:
#     def __init__(self, name):
#         self._bar = name
#
#     def __del__(self):
#         print(f'del {self._bar}')
#
# f1 = Foo('1')
# f2 = Foo('2')
#
# del f1


# import requests
# import os

# url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
# response = requests.get(url)
# data = response.json()
# for k, v in data[0].items():
#     print(f'{k}: {v}')


# url = "https://api.binance.com/api/v3/ticker/price?symbol=BNBBTC"
#
# while True:
#     response = requests.get(url)
#     if 200 < response.status_code < 299:
#         print('error')
#         break
#     data = response.json()
#     os.system('cls')
#     print(f"'{data['symbol']}: {data['price']}'")
#     time.sleep(1)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
# p1 = Point(1, 2)
# p2 = Point(1,2)
#
# print(hash(p1), hash(p2), sep='\n')
# print(id(p1), id(p2))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __len__(self):
#         print('__len__')
#         return self.x * self.x  +  self.y * self.y
#
#     def __bool__(self):
#         print('__bool__')
#         return self.x == self.y
#
# p1 = Point(0, 10)
#
# if p1:
#     print('True')
# else:
#     print('False')



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         return self.marks[item]
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('not value')
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('not value')
#         del self.marks[key]
#
# s1 = Student('vad', [3, 5, 4, 5])
# s1[6] = 7
# print(s1[2])
# print(s1.marks)


# class Frange:
#     def __init__(self, start=0.0, stop=0.0, step=1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
# fr = Frange(0, 2, 0.5)
# for x in fr:
#     print(x)



# class Geom:
#     name = 'Geom'
#
# class Line(Geom):
#     name = 'Line'
#
# print(issubclass(Line, Geom))


# class Geom:
#     name = 'Geom'
#
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#         print('init Geom')
#
# class Line(Geom):
#     name = 'Line'
#
#     def __init__(self, x, y, fill='red'):
#         super().__init__(x, y)
#         print('init Line')
#         self.__fill = fill
#
#     def get_coord(self):
#         return (self._x, self._y)
# l = Line(5,5)
# print(l.__dict__)
# l.get_coord()



# class Goods:
#     def __init__(self, name, price):
#         super().__init__()
#         print('init goods')
#         self.name = name
#         self.price = price
#
#     def info(self):
#         print(f'{self.name, self.price}')
#
# class MixinLog:
#     ID = 0
#     def __init__(self):
#         print('init Mixin')
#         self.ID += 1
#         self.id = self.ID
#
#     def save_log(self):
#         print(f'{self.id} sale')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
# t = NoteBook('aser', 2000)
# print(t.info())
# print(t.save_log())
# print(NoteBook.__mro__)


# import time
# import timeit
# class Point:
#     __slots__ = ('x', 'y') # install only local attributes x and y
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def calc(self):
#         return self.x ** self.y
#
# p = Point(10, 20)
#
# print(timeit.timeit(p.calc))

from dataclasses import dataclass, field


# class Thing:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __repr__(self):
#         return f'thing: {self.__dict__}'


# @dataclass()
# class Thing:
#     name: str = 'v'
#     price: int = 0
#     dims: list = field(default_factory=list)
#     res: int = field(init=False)
#
#     def __post_init__(self):
#         self.res = self.price * 2
#
#
# t = Thing('vad', 1200)
# t1 = Thing('vad', 1200)
# t.dims.append(10)
# print(t, t1)


# from typing import Any
#
# @dataclass
# class Goods:
#     name: Any = None
#     price: Any = None
#
# @dataclass
# class Books(Goods):
#     name: str = 0
#     price: int | float = 0
#     title: str = ''
#     author: str = ''
#
# b = Books('my', 12, 'fill', 'fg')
# print(b)



# class Mammal:
#     phrase = ''
#     def voice(self):
#         return self.phrase
#
#
# class Dog(Mammal):
#     phrase = 'Bark!'
#
#
#
# class Cat(Mammal):
#     phrase = 'Meow!'
#
#
# class Chupakabra:
#     def voice(self):
#         return 'Whooooo!!!'
#
#
# class Recorder:
#     def record_animal(self, animal):
#         voice = animal.voice()
#         print(f'Recorded "{voice}"')
#
#
# r = Recorder()
# cat = Cat()
# dog = Dog()
# strange_animal = Chupakabra()
#
# r.record_animal(cat)            # Recorded "Meow!"
# r.record_animal(dog)            # Recorded "Bark!"
# r.record_animal(strange_animal) # Recorded "Whooooo!!!"




















































