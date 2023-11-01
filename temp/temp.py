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



import random

num = random.randint(1, 16)
print('я умный комп я загадал число, нука отгадай кожаный мешок тупой')
while True:

    user_num = int(input('введите ваше число>: '))
    if num > user_num:
        print('бери больше')
    elif num < user_num:
        print('бери меньше')
    else:
        print('ты угадал кожаный мешок тупой')
        break


















