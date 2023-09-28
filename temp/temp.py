# count = 1
# summ = 0
#
# while count <= 1000:
#     summ += count
#     count += 1
# print(summ)


# def add(a, b, c):
#     print(f'Add slug equals {a + b + c}')


# user_input = int(input('enter n: '))
# res = 1
# for i in range(1, user_input + 1):
#     res *= i
# print(res)

# TRANSLATION = ("a", "b", "v", "g", "d", "e",
#                "j", "z", "i", "y", "k",
#                "l", "m", "n", "o", "p", "r",
#                "s", "t", "u", "f", "h", "c",
#                "ch", "sh", "sch", "", "i",
#                "", "e", "yu", "ya")

# start_index = ord('а')
# print(start_index)
# for i in range(1500):
#     print(f'{i}: {chr(i)}')

# string = 'Добрый, добрый Python - уроки для начинающих Ё ма ё'
# slug = ''
#
# for i in string:
#     if 1072 <= ord(i.lower()) <= 1103:
#         slug += TRANSLATION[(ord(i.lower()) - 1104)]
#     elif i == 'ё' or i == 'Ё':
#         slug += 'yo'
#     elif i in ' !?:;.,':
#         slug += '-'
#     else:
#         slug += i
#         # print(ord(i))
# slug = slug.replace('---', '-')
# slug = slug.replace('--', '-')
# print(slug)

# a = [i for i in range(7)]
# for i in iter(a):
#     print(i)

# m, n = list(map(int, input('>>>: ').split()))
# zero = []

# for i in range(m):
#     zero.append([0] * n)
# print(zero)
# for i in range(m):
#     for j in range(n):
#         zero[i][j] = 1
# print(zero)


# a = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16],
#      ]

# for i in a:
#     for j in i:
#         print(j, end='\t')
#     print()

# for i in range(len(a)):
#     for j in range (i + 1, len(a)):
#         a[i][j], a[j][i] = a[j][i], a[i][j]


# for i in a:
#     for j in i:
#         print(j, end='\t')
#     print()


# TRIANGLE PASCAL

# N = 7
# RES = []

# for i in range(N):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j !=i:
#             row[j] = RES[i-1][j-1] + RES[i-1][j]
#     RES.append(row)

# for i in RES:
#     print(i)


# d_inp = input('>>>: ')
#
# a = [int(i) for i in d_inp.rstrip().split(' ')]
# print(a)

# A = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# A = [[row[i] for row in A] for i in range(len(A[0]))]
#
# print(A)


# d = {'house': 'дом',
#      'car': 'машина',
#      'tree': 'дерево',
#      'river': 'река'}
#
# print(d['tree4'])

# dict_a = {1: '1', 2: '2', 3: '3'}
# print(type(dict_a), dict_a)

# set_a = {1, 2, 3, 4}
# set_a.add(5)
# set_a.update([6, 7])
# set_a.discard(7)
# set_a.remove(5)
# set_a.pop()
# set_a.clear()
# print(set_a)
# print(type(set_a), set_a)


# a = {1, 2, 3, 4}
# b = {5, 6, 7, 8}
#
# c = a | b
# print(c)


# a = {i: i ** 2 for i in range(7)}
#
# print(a)


# def my(a: str, b: list) -> list:
#     b.append(a)
#     return b
#
#
# print(my('i', ['q', 'w']))

# def send_mail(text: str) -> str:
#     print(text)
#
# send_mail('qwerty')

# def get_max(x, y):
#     return x if x > y else y
#
#
# x, y, z = 5, 7, 10
# print(get_max(x, get_max(y, z)))


# Algoritm Evclida(min delitel)


# def get_nod(a: int, b: int) -> int:
#     """
#     Эта функция вычисляет наибольший общий делитель (НОД) двух чисел.
#     :param a: Первое целое число.
#     :param b: Второе целое число.
#     :return: Наибольший общий делитель (НОД) двух чисел.
#     """
#     # while a != b:
#     #     if a > b:
#     #         a -= b
#     #     else:
#     #         b -= a
#     # return a
#
#     if a > b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#
#     return a
#
#
# # print(get_nod(18, 24))
# # help(get_nod)
#
# import time
# def test_nod(func):
#     # test 1
#     a = 28
#     b = 35
#     res = func(a, b)
#     if res == 7:
#         print('test 1 ok')
#     else:
#         print('test 1 fail')
#
#     # test 2
#     a = 100
#     b = 1
#     res = func(a, b)
#     if res == 1:
#         print('test 2 ok')
#     else:
#         print('test 2 fail')
#
#     # test 3
#     a = 2
#     b = 100000000
#     st = time.time()
#     res = func(a, b)
#     ft = time.time()
#     t = ft - st
#     print(t)
#     if res == 2 and t < 1:
#         print('test 3 ok')
#     else:
#         print('test 3 fail')
#
#
# test_nod(get_nod)

# def os_path(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# os_path('sdf', 46, 'dsg', s=2, w='sdv')

# a = (1, 2, 2, 2, 3, 4)
# print((*a,))

# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# p = fact(3)
# print(p)


# p = lambda a, b: a * b
#
# print(p(2, 3))

# def say_name(name):
#     def goodbye(age):
#         print(f'goodbye {name}, {age}')
#
#     return goodbye
#
#
# a = say_name('vad')
# a(23)


# decorator
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("перед вызовом что то делает")
#         res = func(*args, **kwargs)
#         print("после вызова что то делает")
#         return res
#
#     return wrapper
#
#
# @decorator
# def some_func(*args, **kwargs):
#     print(f'called func some_func {args}{kwargs}')
#
#
# some_func('vad', 12)


# import time
#
#
# def test_time(func):
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         res = func(*args, **kwargs)
#         ft = time.time()
#         t = ft - st
#         print(f'time: {t}')
#         return res
#
#     return wrapper
#
#
# @test_time
# def get_nod(a: int, b: int) -> int:
#     """
#     Эта функция вычисляет наибольший общий делитель (НОД) двух чисел.
#     :param a: Первое целое число.
#     :param b: Второе целое число.
#     :return: Наибольший общий делитель (НОД) двух чисел.
#     """
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# @test_time
# def get_nod2(a: int, b: int) -> int:
#     """
#     Эта функция вычисляет наибольший общий делитель (НОД) двух чисел.
#     :param a: Первое целое число.
#     :param b: Второе целое число.
#     :return: Наибольший общий делитель (НОД) двух чисел.
#     """
#     if a > b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#
#     return a
#
#
# get_nod(2, 10000000)
# get_nod2(2, 10000000)

# import math
# from functools import wraps
#
#
# def df_decorator(dx=0.001):
#     def func_decorator(func):
#         @wraps(func)  # use decorator wraps for save __name__ and __ doc__ func wrapper
#         def wrapper(x, *args, **kwargs):
#             res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#
#         return wrapper
#
#     return func_decorator
#
#
# @df_decorator(dx=0.0001)
# def sin_df(x):
#     """func for calculate sin number"""
#     return math.sin(x)
#
#
# df = sin_df(0.8)
# print(df)
# print(sin_df.__name__, sin_df.__doc__)












































































































































































































































































































































































