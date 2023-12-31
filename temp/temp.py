# class Human:
#     default_name = "no name"
#     default_age = 0
#
#     @staticmethod
#     def default_info():
#         print(f'default_name: {Human.default_name}' + '\n'
#                 f'default_age: {Human.default_age}' + '\n')
#
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = None
#
#
#     def info(self):
#         print('========================')
#         print(f"name: {self.name}")
#         print(f"age: {self.age}")
#         print(f"money: {self.__money}")
#         print(f"house: {self.__house}")
#         print('========================')
#
#
#     def __make_deal(self, house, price):
#         if house:
#             self.__house = house
#             self.__money -= price
#
#     def earn_money(self, money):
#         self.__money += money
#         print(f'you are have {self.__money} money')
#
#     def buy_house(self, house, discount):
#         price = house.final_price(discount)
#         if self.__money < price:
#             print('dont have any money')
#         else:
#             self.__make_deal(house, price)
#             print(f'congratulate, house been to buy!!! {price}')
#
#
#
# class House:
#     def __init__(self, area, price):
#         self.__area = area
#         self.__price = price
#
#
#     def final_price(self, discount):
#         # print(f'final price: {self.__price * (100 - discount) / 100}')
#         return self.__price * (100 - discount) / 100
#
# class SmallHouse(House):
#     def __init__(self, area = 40, price=10_000):
#         super().__init__(area, price)
#
# if __name__ == '__main__':
#
#     Human.default_info()
#     h = Human('vad', 44)
#     h.info()
#     sh = SmallHouse()
#     print(sh.final_price(20))
#     h.buy_house(sh, 20)
#     h.earn_money(8_000)
#     h.info()
#     print(sh.final_price(20))
#     h.buy_house(sh, 20)
#     h.info()
import pathlib


# import string
#
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def print(self):
#         print(', '.join(self.letters))
#
#     def letters_sum(self):
#         return len(self.letters)
#
# class EngAlphabet(Alphabet):
#     __letters_num = len(string.ascii_uppercase)
#
#     def __init__(self):
#         lang = 'En'
#         letters = list(string.ascii_uppercase)
#         super().__init__(lang, letters)
#
#     def is_en_letter(self, letter):
#         return letter in self.letters
#
#     def letters_num(self):
#         return self.__letters_num
#
#     @staticmethod
#     def example():
#         return "This is an example text in English."
#
#
#
#
# a = EngAlphabet()
# a.print()
# print(a.letters_num())
# print(a.is_en_letter('F'))
# print(a.is_en_letter('Щ'))
# print(a.example())

# class Tomato:
#     states = {
#         1: "Отсутствует",
#         2: "Цветение",
#         3: "Зеленый",
#         4: "Красный"
#     }
#
#     def __init__(self, index):
#         self._index = index
#         self._state = 1
#
#     def grow(self):
#         if self._state < len(self.states):
#             self._state += 1
#
#     def is_ripe(self):
#         return self._state == len(self.states)
#
# class TomatoBush:
#     def __init__(self, num_tomatoes):
#         self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes)]
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def all_are_ripe(self):
#         return all(tomato.is_ripe() for tomato in self.tomatoes)
#
#     def give_away_all(self):
#         self.tomatoes = []
#
# class Gardener:
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         self._plant.grow_all()
#
#     def harvest(self):
#         if self._plant.all_are_ripe():
#             print(f"{self.name} собрал урожай!")
#             self._plant.give_away_all()
#         else:
#             print("Томаты еще не дозрели. Продолжайте ухаживать за ними.")
#
#     @staticmethod
#     def knowledge_base():
#         print("Справка по садоводству:")
#         print("1. Создайте объект класса TomatoBush, указав количество томатов.")
#         print("2. Создайте объект класса Gardener, указав свое имя и объект TomatoBush.")
#         print("3. Используйте метод work(), чтобы ухаживать за растением.")
#         print("4. Проверьте зрелость томатов с помощью метода all_are_ripe() у TomatoBush.")
#         print("5. Если все томаты созрели, соберите урожай с помощью метода harvest() у Gardener.")
#
# # Тесты
# # Gardener.knowledge_base()
# bush = TomatoBush(5)
# gardener = Gardener("vad", bush)
#
# while True:
#     print(f"Состояние: {', '.join(Tomato.states[tomato._state] for tomato in bush.tomatoes)}")
#     print('====================================')
#     if bush.all_are_ripe():
#         print("Все томаты готовы к сбору урожая.")
#         gardener.harvest()
#         break
#     else:
#         print(f"Томаты еще не дозрели. \n"
#               f"Продолжайте ухаживать за ними.\n")
#         gardener.work()


# def wrapper(func):
#     def inner(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             return res
#         except ZeroDivisionError:
#             return "The command don't need division zero"
#         except TypeError:
#             return "The command don't need args"
#         except IndexError:
#             return "The command need more args"
#         except KeyError:
#             return "The command is unknown"
#         except ValueError:
#             return "Something goes wrong. Input 'help' for manual"
#         except FileNotFoundError:
#             return "Entered folder does not exists. Please provide correct path to folder"
#
#     return inner
#
#
# @wrapper
# def func():
#     x, y = map(int, input('>>: ').split())
#     res = x / y
#     return res
#
#
# print(func())


# def wrap(func):
#     def inn(*args):
#         res = func(*args)
#         return print(f'res; {res*9}')
#     return inn
#
# @wrap
# def f(x):
#     return x
#
# f(3)


# def intersection(*args):
#     a, b = set(args[0]), set(args[1])
#     c = a & b
#     return list(c)
#
# i = intersection([4,9,5], [9,4,9,8,4]) # [9, 4]
# print(i)


#
# import random
#
# num = random.randint(1, 16)
# print('я умный комп я загадал число, нука отгадай кожаный мешок тупой')
# while True:
#
#     user_num = int(input('введите ваше число>: '))
#     if num > user_num:
#         print('бери больше')
#     elif num < user_num:
#         print('бери меньше')
#     else:
#         print('ты угадал кожаный мешок тупой')
#         break

# from datetime import datetime, timedelta
# def __get_current_week():
#     now = datetime.now()
#     current_weekday = now.weekday()
#     print(current_weekday)
#     if current_weekday <= 5:
#         week_start = now - timedelta(days=0 + current_weekday)
#     else:
#         week_start = now - timedelta(days=current_weekday - 4)
#
#     return [week_start.date(), week_start.date() + timedelta(days=7)]
#
#
# print(__get_current_week())

# named typle

# from collections import namedtuple
# movies = namedtuple('movies', ['title', 'year', 'season'])
# m1 = movies("qwerty", "1982", "2")
#
# print(m1)

# from collections import Counter
# text = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
# "Нет никого, кто любил бы боль саму по себе, кто искал бы её и кто хотел бы иметь её просто потому, что это боль.."
#
# c = Counter(text)
#
# print(c)

# from time import time
# from tqdm import tqdm
# def decor(func):
#     def inner( *args, **kwargs):
#         s = time()
#
#         res = func(*args, **kwargs)
#         e = time() - s
#         print(e)
#         return res
#     return inner
#
#
# @decor
# def add(x, y):
#     a = []
#     for i in tqdm(range(15050000)):
#         a.append(x ** y)
#     return a
#
# add(2, 45)

# def func():
#     i = 0
#     while i < 6:
#         yield i
#         i += 1
#
#
# for j in func():
#     input(">>")
#     print(j)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# b = list(map(lambda x: x * 2, a))
#
# print(b)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# c = dict(zip(a, b))
#
# print(c)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# b = list(filter(lambda x: x > 5, a))
#
# print(b)


# import collections
#
# a = collections.UserDict()
# a.data['1'] = 1
# print(a)

# help(super)

# class User:
#     def __init__(self):
#         self.__hp = 100
#
#
#     @property
#     def hp(self):
#         return self.__hp
#
#     @hp.setter
#     def hp(self, new_value):
#         self.__hp = new_value
#
#
#
# user = User()
#
# print(user.hp)
#
# user.hp = 150
#
# print(user.hp)


# class Foo:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         return self.x + other
#
# class Bazz:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         return self.x + other
#
# a = Foo(2)
# b = Bazz(2)
# print(a + 3)


# from enum import Enum
#
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#
# print(Color.RED)  # Выведет: Color.RED
# print(Color.RED.value)


# import requests
#
#
# class RequestConnection:
#     def __init__(self, request):
#         self.request = request
#
#     def get_json_from_url(self, url):
#         return self.request.get(url).json()
#
#
# class ApiClient:
#     def __init__(self, fetch: RequestConnection):
#         self.fetch = fetch
#
#     def get_data(self, url):
#         response = self.fetch.get_json_from_url(url)
#         return response
#
#
# def data_adapter(data: dict):
#     return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]
#
#
# def pretty_view(data):
#     pattern = '|{:^10}|{:^10}|{:^10}|'
#     print(pattern.format('currency', 'sale', 'buy'))
#     for el in data:
#         currency, *_ = el.keys()
#         buy = el.get(currency).get('buy')
#         sale = el.get(currency).get('sale')
#         print(pattern.format(currency, sale, buy))
#
#
# if __name__ == '__main__':
#     api_client = ApiClient(RequestConnection(requests))
#
#     data = api_client.get_data('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
#     pretty_view(data_adapter(data))

# from enum import Enum
#
# class Some(Enum):
#     name = 'name'
#     age = 'age'
#
#
#
# if __name__ == '__main__':
#     for i in Some:
#         print(f'Name: {i.value}')

# from abc import ABC, abstractmethod
#
# class My(ABC):
#
#     @abstractmethod
#     def method_1(self):
#         return NotImplementedError
#
#
#
# class MyM(My):
#
#     def foo(self):
#         pass
#
#     def method_1(self):
#         print('foo')
#
# m = MyM()
# m.method_1()

# import logging
#
# logging.basicConfig(
#     format='%(asctime)s %(message)s',
#     level=logging.DEBUG,
#         handlers=[
#         logging.FileHandler("program.log"),
#         logging.StreamHandler()
#     ])
# logging.warning('An example message.')
# logging.warning('Another message')


# def foo(a: int, b: float) -> int:
#     return a * b
#
# print(foo(2, 2.2))


# from threading import Thread
#
# def foo(par):
#     return par
#
# if __name__ == '__main__':
#     for j in range(5):
#         th = Thread(target=foo, args=(f'Count thread - {j}',))
#         th.start()

# from  pathlib import Path
# path = pathlib.Path(__file__)
# print(path.suffix)


def foo():
    while True:
        i = input('>> ')
        match i:
            case '1':
                print(i)
            case '2':
                print(i)
            case _:
                print('end')
                break

