# Задание 1
# Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за расположение элемента в
# списке. Position всегда должен быть последовательным, например у нас есть список
# Придерживаясь такой логики, необходимо реализовать:
# Удаление элемента

from pprint import pprint

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4},
    {'name': 'Test 5', 'position': 5}
]


def delete_pos(lst, position_number):
    lst.pop(position_number - 1)
    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)
    return lst


pprint(delete_pos(data, 2))

# Задача 2
# Добавление элемента с любым position, например мы хотим в наш исходный список добавить
# элемент у которого position = 1, то должны получить:

from pprint import pprint

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
]


def add_pos(lst, position_number, arg_for_pos):
    new_dict = {'name': f'{arg_for_pos} {len(lst) + 1}', 'position': None}
    lst.insert(position_number - 1, new_dict)

    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)
    return lst


pprint(add_pos(data, 1, 'Test'))

# Задание 3
# Поменять элементы местами, например position 1 и position 3, то должны получить следующий список:

from pprint import pprint

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},

]


def change_pos(lst, pos_for_change_1, pos_for_change_2):
    lst.insert(pos_for_change_1 - 1, lst[pos_for_change_2 - 1])
    lst.pop(pos_for_change_2)
    lst.insert(pos_for_change_2, lst[pos_for_change_1])
    lst.pop(pos_for_change_1)

    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)

    return lst


pprint(change_pos(data, 1, 3))


# Задание 1
# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.


def change(lst: list) -> list:
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


a = [4, 8, 2, 'qwert', '@#$']
print(change(a))


# Задание 1
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут
# соответствовать правилам задания ключей в словарях.


def to_dict(lst):
    a = dict(zip(lst, lst))
    return a


lst = [4, 15, 254, 'qwer', '123@@']
print(to_dict(lst))


# Задание 3
# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start»
# до величины «end» включительно.Если пользователь задаст первое число большее чем второе,
# просто поменяйте их местами.

def sum_range(start: int, end: int):
    a = 0
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        a += i
    return a


print(sum_range(4, 9))


# Задание 4
# # Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# # и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# # что задано положительное целое число).


def read_last(lines, file):
    if lines > 0:
        a = open(file, 'r')
        strings = a.readlines()[-lines:]
        for i in strings:
            print(i)
        a.close()

    else:
        print("Неверно, должно быть задано положительное целое число ")


read_last(5, 'for 13.txt')

# Задание №1
# Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк


import pickle

job_title = [
    {
        'name': 'Alexandr',
        'position': 'engineer',
    },
    {
        'name': 'Maksim',
        'positione': 'director'
    }
]

file = open('omtp.com.ua', 'wb')
file.write(pickle.dumps(job_title))
file.close()
# Задание 2
# Дано два словаря
# Необходимо написать код который будет их объединять
# Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы
# не потерять значения нужно записать в один ключ список в котором будут находится значения
# Записать результат в файл result.json в формате JSON.

import json

fast_car = {
    'drift': 'nissan',
    'price': '32k'
}
comfort_car = {
    'drift': 'mazda',
    'starting price': '42000$'
}
same_keys = {}
for key, value in fast_car.items():
    for key1, value1 in comfort_car.items():
        if key == key1:
            same_keys[key1] = [value, value1]
        else:
            break

diff_keys = fast_car | comfort_car
result = diff_keys | same_keys

json_result = json.dumps(result)
with open('result.json', 'w') as file:
    file.write(json_result)

# Задание #1
# Дано два множества A и B
# В множестве А находятся имена должников за Сентябрь
# В множестве B находятся имена должников за Октябрь
# Найти:
# * Вывести имена людей которые должны за Сентябрь и Октябрь
# * Вывести должников за Октябрь у которых нет долга за Сентябрь

A = {'Вася ', 'Петя', 'Галя', 'Герасим', 'Коля'}
B = {'Артур', 'Коля', 'Герасим', 'Петя', 'Жанна'}

print(A | B)
print(B - A)

# Задание #2:
'''Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt
Пример вывода:
Access denied
OK
OK
OK
OK
'''

n = int(input('количество запросов к файлам: '))
keys = {'write': 'W', 'read': 'R', 'execute': 'X'}
A = {}

for i in range(n):
    a, b = input('введите имя файла и права доступа к файлу: ').split()
    A[a] = b

m = int(input('количество запросов к файлам: '))

for i in range(m):
    c, d = input('введите разрешение для файла и имя файла: ').split()
    if keys[c] in A[d]:
        print('ok')
    else:
        print('Access denied')

# 1 Дан многомерный список. Вывести на экран первый и последний столбцы.


A = [
    [1, 6, 8, 5, 4, 0, 3],

    [5, 7, 8, 9, 4, 2, 1],

    [6, 0, 7, 8, 1, 2, 5],

    [5, 7, 2, 7, 5, 2, 1]
]

for i in range(len(A)):
    F, *centr, L = A[i]

    print(F, L)

# 2 Дан многомерный список. Вывести на экран все четные столбцы, у которых первый элемент больше последнего.


A = [[1, 6, 8, 5, 4, 0, 3],

     [5, 7, 8, 9, 4, 2, 1],

     [6, 0, 7, 8, 1, 2, 5],

     [5, 7, 2, 7, 5, 2, 1]]

for i, a in enumerate(A):
    print(*[A[i][j] for j, b in enumerate(a) if j % 2 == 0 and A[0][j] > A[len(A) - 1][j]])

# Задача 3
# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то,что есть разные выигрышные варианты и программа должна их распознавать.


Doska = [
    ['o', 'o', 'x'],
    ['x', 'o', 'o'],
    ['x', 'x', 'o']
]

n = 0

for i, i_value in enumerate(Doska):
    V = 0  # hod vas
    P = 0  # hod pet

    for j, j_value in enumerate(i_value):
        if str(Doska[i][j]) == 'x':
            V += 1
        elif str(Doska[i][j]) == 'o':  #
            V -= 1
        if str(Doska[j][i]) == 'x':
            P += 1
        elif str(Doska[j][i]) == 'o':
            P -= 1

        if str(Doska[0][0]) == str(Doska[1][1]) == str(Doska[2][2]) == 'x' or str(Doska[0][2]) == str(
                Doska[2][0]) == str(Doska[1][1]) == 'x':
            n += 1
        if str(Doska[0][0]) == str(Doska[1][1]) == str(Doska[2][2]) == 'o' or str(Doska[0][2]) == str(
                Doska[2][0]) == str(Doska[1][1]) == 'o':
            n -= 1

        if V == 3 or P == 3 or n == 3:  #
            print("x win")
            exit()

        elif V == -3 or P == -3 or n == -3:  #
            print("o win")
            exit()


else:

    print("Ничья")


def transpose_list(list_of_lists):
    return [
        list(row)
        for row in zip(*list_of_lists)
    ]


print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список


list_num = []

for num in range(5):
    i = int(input('Введите число: '))
    list_num.append(i)

print(list_num)

# Задание 2:
# Дан список A = [1, 2, 3, 4, 5] Удалить последнее число из списка


A = [1, 2, 3, 4, 5]
del A[-1]

print(A)

# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N


my_list = []
rep = 0

for num in range(10):
    x = int(input(f'Введите число {num + 1}: '))
    my_list.append(x)

N = int(input('Число которое повторяется: '))

for num_2 in my_list:
    if num_2 == x:
        rep += 1

print(rep)

# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности


N = int(input('Число пользователя N:'))
number = []

for num in range(N):
    x = int(input('Введите число: '))
    number.append(x)
    number_rev = list(reversed(number))

print('Cписок A =', number)

print('Обратный список =', number_rev)

# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

# NO


A = []

for num in range(5):
    x = int(input(f'Введите число {num + 1}: '))
    A.append(x)
print('Список А ', A)
C = []
for num_2 in A:
    if num_2 > 5:
        C.append(num_2)

print('Список C ', C)

# адание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max).
# Вывести эти числа.


A = []
N = int(input('Число пользователя N:'))

for num in range(N):
    x = int(input('Введите число: '))
    A.append(x)
sorted(A)

print('Список А =', A)
a, *_, b = A

print(f'Min =', a)
print(f'Max =', b)

# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте


a = input('Введите строку; ')

num = [int(i) for i in a if i.isdigit()]
print('Количество цифр в тексте:', len(num))

#  Задание 1  Написать программу которая проверяет что в строке есть хотя бы один пробел,
# число, буква нижнего и верхнего регистра. Если это так, то вывести 'YES', иначе 'NO'


import string

test_string = input('Введите строку: ')

symbol_space = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0

for symbol in test_string:
    if symbol.isspace():
        symbol_space += 1
    elif symbol.islower():
        symbol_lower += 1
    elif symbol.isupper():
        symbol_upper += 1
    elif symbol.isdigit():
        symbol_digit += 1
if symbol_lower != 0 and symbol_upper != 0 and symbol_digit != 0 and symbol_space != 0:
    print('YES')
else:
    print('NO')

# Задание 2 Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.


count = int(input('Веди число: '))

f1 = f2 = 1
print(f1, f2, end=' ')
i = 2
while i < count:
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    i += 1
print()

# Задаине №3 Напишите программу где пользователь вводит пароль, а программа проверяет сложность
# пароля и выводит свой результат в оценочной шкале от 1 до 5.


lower_case = 0
upper_case = 0
special = 0
digits = 0
password = input('Введите пароль на проверку: ')

if password == 'qwerty' or password == 'admin' or password == '':
    print('Оценка сложности пароля -', 1)
    exit()

for i in range(len(password)):
    if str(password[i]).islower():
        lower_case += 1
    elif str(password[i]).isupper():
        upper_case += 1
    elif str(password[i]).isnumeric():
        digits += 1
    else:
        special += 1

if lower_case == len(password) or upper_case == len(password) or digits == len(password) or special == len(
        password):
    print('Оценка сложности пароля -', 2)

elif lower_case > 0 and digits > 0 and upper_case == 0 and special == 0:
    print('Оценка безопастности пароля -', 3)
elif lower_case > 0 and upper_case > 0 and digits == 0 and special == 0:
    print('Оценка сложности пароля -', 3)
elif lower_case > 0 and special > 0 and digits == 0 and upper_case == 0:
    print('Оценка сложности пароля -', 3)
elif upper_case > 0 and special > 0 and digits == 0 and lower_case == 0:
    print('Оценка сложности пароля -', 3)
elif upper_case > 0 and digits > 0 and special == 0 and lower_case == 0:
    print('Оценка сложности пароля -', 3)
elif special > 0 and digits > 0 and upper_case == 0 and lower_case == 0:
    print('Оценка сложности пароля -', 3)

elif lower_case > 0 and digits > 0 and upper_case > 0 and special == 0:
    print('Оценка сложности пароля -', 4)
elif special > 0 and digits > 0 and upper_case > 0 and lower_case == 0:
    print('Оценка сложности пароля -', 4)
elif lower_case > 0 and digits > 0 and special > 0 and upper_case == 0:
    print('Оценка сложности пароля -', 4)
elif lower_case > 0 and special > 0 and upper_case > 0 and digits == 0:
    print('Оценка сложности пароля -', 4)

elif lower_case > 0 and digits > 0 and upper_case > 0 and special > 0 and len(password) > 8:
    print('Оценка сложности пароля -', 5)

# Задание №4 Напишите программу где пользователь вводит число symbol_len, а программа генерирует
# пароль длинной symbol_len. Чем выше будет сложность пароля, тем лучше. Сложность пароля буду
# оценивать по шкале от 1 до 5 из задании #3
#


import random
import string

symbol_len = int(input('Длина пароля:'))

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '()[]{}@# %^&*_+-='
digits = '0123456789'

all = lower_case + upper_case + special + digits
passworld = ''.join(random.sample(all, symbol_len))

upper_case = any([1 if i in string.ascii_uppercase else 0 for i in passworld])
lower_case = any([1 if i in string.ascii_lowercase else 0 for i in passworld])
special = any([1 if i in string.punctuation else 0 for i in passworld])
digits = any([1 if i in string.digits else 0 for i in passworld])
length = symbol_len

if length >= 8:
    length = True
else:
    length = False

characters = [upper_case, lower_case, special, digits, length]

score = 0

for i in range(len(characters)):
    if characters[i]:
        score += 1

print('Надежность пароля: %s из 5' % score)

print('Ваш пaроль: ' + passworld)

# Задание 1:
#  Необходимо вывести на экран числа от 5 до 1 с помощью цикла for.

for i in range(5, 0, -1):
    print(i, end=' ')

# Задание 4:
# Вывести на экран таблицу умножения от 1 до 10 с помощью двух циклов for.

for i in range(1, 11):

    for n in range(1, 11):
        print(n, '*', i, '=', n * i, sep='', end='    ')
    print()

# Задание 2:
#  Вывести таблицу умножения на 3 с помощью цикла for.


for i in range(1, 11):
    print('3*', i, '=', 3 * i, sep='')

# Задание 3:
# Программа с помощью библиотеки random генерирует случайное число от 1 до 10,
# задача пользователя угадать это число за 3 попытки. В случае если пользователь
# указал больше загаданного числа, то нужно вывести "Бери меньше" и наоборот.


import random

n = 0
for i in range(1, 11):

    print(f'Попытка №', n + 1)
    a = int(input(':'))

    if a == i:
        print('Ты угадал!')
        break
    if a < i:
        print('Бери больше')
    else:
        print('Бери меньше')
    n += 1
    if n == 3:
        break

# Вывести треугольник #1 с шириной N с помощью цикла while

N = int(input("Please input number :"))

num_height = 1

while num_height <= N:
    num_width = N
    while num_width >= num_height:
        print("*", end='')
        num_width -= 1
    num_height += 1
    print()

# Вывести треугольник #2 с шириной N с помощью цикла while

N = int(input("Please input number :"))

h = 1

while h <= N:
    w = 1
    while w <= h:
        print("*", end="")
        w += 1
    h += 1
    print()

# Вывести треугольник #3 с шириной N с помощью цикла while

N = int(input("Please input number :"))
i = N

print(('*') * i)
while i != 1:
    i -= 1

    print((' ') * (N - i) + (('*') * i))

# Задание 1
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))

if min(a, b, c) > 10 and a % 3 == 0 and b % 3 == 0:
    print('Yes')
else:
    print('No')

# Задание 2

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

max = a
if b > max:
    max = b
if c > max:
    max = c

print(f'max: ', max)

# Задания со звездочкой:

number = int(input('Введите 3х значное число:'))
if not 100 <= number <= 999:
    print('Ошибка, число не входит в диапазон')
    exit()

first_num = number % 10
second_num = number % 100 // 10
third_num = number % 1000 // 100
final_num = first_num * 100 + second_num * 10 + third_num
print(final_num)
a = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
]
for i in range(len(a)):
    F, *centr, L = a[i]
    print(F, L)

from re import search

j = 'Oceans'
key = 'ocean'
reg = bool(search(f'{j.lower()}\-', key))
print(reg)

j = 'Oceans'
key = 'Ocean'
if key in j:
    print('Ok')

# 1 Вывести на экран строку "Hello world"
# 2 Вывести на экран пять звездочек (*)
# 3 Задание со звездочкой:
# Вывести на экран квадрат 5 на 5 заполненный символами '#'


print('Hello world\n')  # 1

print('*\n' * 5)  # 2

per = '#  ' * 5
print((per + '\n') * 5)  # 3

# 1) Вывести на экран букву "W" из символов "*" (звездочка). Пример:
# 2) Запросить у пользователя число N (Для этого можно использовать функцию input, либо же заранее создать переменную N = 5), вывести на экран прямоугольник, заполненный буквами А. Количество строк в прямоугольнике равно N, количество столбцов равно 8. Пример:

print(' ', '*', ' ' * 3, '*', ' ' * 3, '*')  # 1
print(' ' * 2, '*', ' ', '*', '*', ' ', '*')
print(' ' * 3, '*', '*', ' ', '*', '*')
print(' ' * 4, '*', ' ' * 3, '*')


N = input('Введите число строк: ')  # 2
a = 'A'
b = '\n'
W = 8
print((a * W + b) * int(N))

# Написать программу которая запрашивает у пользователя (с помощью функции input) 2 числа:
# Сторона А и Высота h
# Программа должна по формуле вычислить площадь треугольника и вывести ее пользователю.

print('Вычисление площади треугольника по стороне А и высоте h.')
A = float(input('Введите сторону А >: '))
h = float(input('Введите высоту h >: '))
result = A * h/2
print(f'Результат вычисления: {result}')

# Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

num_a = int(input('Enter a >: '))
num_b = int(input('Enter b >: '))
num_c = int(input('Enter c >: '))

if (num_a and num_b and num_c) > 10 and (num_a and num_b // 3):
    print('yes')
else:
    print('no')

    # Пользователь вводит с клавиатуры три числа в переменные a, b, c.
    # Найдите наибольшее число из них и запишите в переменную max.

    num_a = int(input('Enter a >: '))
    num_b = int(input('Enter b >: '))
    num_c = int(input('Enter c >: '))
    max = 0
    if num_a >= num_b and num_a >= num_c:
        max = num_a
    if num_b >= num_a and num_b >= num_c:
        max = num_b
    if num_c >= num_a and num_c >= num_b:
        max = num_c
    print(f'Наибольшее число равно: {max}')

# Пользователь с клавиатуры вводит трех значное число в переменную number.
# Переставьте первую и последнюю цифру переменной number,
# полученный результат запишите в переменную reversed_number.
# Важно, что переменная number обязательно должна быть типа данных int
# и для решения задачи можно использовать преобразование типов данных
# только при получении числа из функции input.

number = int(input('Введите трехзначное число>: '))
new_number_1 = number % 10
temp_number = number // 10
new_numbers_2 = temp_number % 10
new_numbers_3 = temp_number // 10

print(f'Новое перевернутое число: {new_number_1}{new_numbers_2}{new_numbers_3}')

#Вывести треугольник #1 с шириной N с помощью цикла while
# *****
# ****
# ***
# **
# *

N = int(input('Enter N>: '))
while N != 0:
    print(N * '*')
    N -= 1

#Вывести треугольник #1 с шириной N с помощью цикла while
# *
# **
# ***
# ****
# *****

N = int(input('Enter N>: '))
h = 1
while h <= N:
    print(h * '*')
    h += 1

#Вывести треугольник #1 с шириной N с помощью цикла while
# *****
#  ****
#   ***
#    **
#     *

N = int(input('Enter N>: '))
h = 0
while N != 0:
    print(h * ' ' + N * '*')
    h += 1
    N -= 1

#Вывести треугольник #1 с шириной N с помощью цикла while
#     *
#    **
#   ***
#  ****
# *****

N = int(input('Enter N>: '))
h = 1
while N >= 1:
    print((N - 1) * ' ' + h * '*')
    h += 1
    N -= 1


# Задание 1:
# Необходимо вывести на экран числа от 5 до 1 с помощью цикла for.
# На экране должно быть: 5 4 3 2 1

for num in range(5, 0, -1):
    print(num)

# Вывести таблицу умножения на 3 с помощью цикла for.

for num in range(1, 11):
    result = num * 3
    print(f'{3}*{num}={result}')

# Программа с помощью библиотеки random генерирует случайное число
# от 1 до 10, задача пользователя угадать это число за 3 попытки.
# В случае если пользователь указал больше загаданного числа,
# то нужно вывести "Бери меньше" и наоборот.

import random

print('Игра угадай число за три попытки.')
hidden_number = random.randint(1, 10)
question = input('Сыграем? y/n >: ')

if question == 'y':
    for n in range(1, 4):
        entered_number = int(input(f'Попытка #{n}>: '))
        n += 1
        if entered_number > hidden_number:
            print('Бери меньше')
        elif entered_number < hidden_number:
            print('Бери больше')
        elif entered_number == hidden_number:
            print('Ты угадал, ты красавчик!')
            break
    print('Игра окончена!')
elif question == 'n':
    print('Значит, сыграем в другой раз')


# Вывести на экран таблицу умножения от 1 до 10 с помощью двух циклов for.

for num_1 in range(1, 11):
    for num_2 in range(1, 11):
        result = num_2 * num_1
        print(f'{num_1}*{num_2}={result}')


# Задание 5:
"""Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре
со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. Нужно реализовать шифрование
с помощью Python.
Пользователь вводит строку которую хочет зашифровать и число (сдвиг), нужно с помощью шифра Цезаря ее
зашифровать и вывести на экран.
"""
import sys

alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' * 2  # русский алфавит
alphabet_eng = 'abcdefghijklmnopqrstuvwxyz' * 2  # английский алфавит
result = ''

text = input('Шифр-машина Цезаря готова к работе\nВведите текст: ').lower()  # ввод текста и перевод в нижний регистр

language = input('Укажите язык рус/eng: ')  # ввод языка и проверка на правильность
alphabet = alphabet_eng if language == 'eng' else alphabet_ru

if language != 'eng' and language != 'рус':
    print('Вы ввели неверный язык ввода, начните игру заново!')
    sys.exit()

number = input('Введите количество символов сдвига(цифра): ')  # ввод сдвига
if not number.isdigit():
    print('Вы ввели неверный формат, начните игру заново!')
    sys.exit()
else:
    number = int(number)
for n in text:
    position = alphabet.find(n)  # вхождение в строку(позиция в цифре)
    new_position = position + number
    if n in alphabet:
        result += alphabet[new_position]
    else:
        result += n

print(f'Результат шифрования: {result}')


"""
Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
1. isspace
2. islower
3. isupper
4. isdigit
"""

test_string = input('Enter test string >: ')
symbol_space = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0

for symbol in test_string:
    if symbol.isspace():
        symbol_space += 1
    elif symbol.islower():
        symbol_lower += 1
    elif symbol.isupper():
        symbol_upper += 1
    elif symbol.isdigit():
        symbol_digit += 1
if symbol_lower != 0 and symbol_upper != 0 \
        and symbol_digit != 0 and symbol_space != 0:
    print('YES')
else:
    print('NO')


# Напишите программу где пользователь вводит число - count,
# а программа выводит count чисел фибоначчи.

count = int(input('Enter number >: '))
fib_num_1 = 0
fib_num_2 = 1

if count == 0:
    print(0)
    exit(4)
else:
    print(fib_num_1)
for i in range(count + 1):
    fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2
    print(fib_num_1)


# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
# 3- у пользователя в пароле соблюдается два условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
# у пользователя в пароле соблюдается три условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

enter_password = input('Enter password to verify >: ')
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
symbol_punctuation = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0

# 1 сложность
if enter_password == 'qwerty' or \
        enter_password == 'admin' or \
        enter_password == '':
    print('Password complexity is 1')
    exit()

# 5 сложность
for symbol in enter_password:
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
    if symbol.islower():
        symbol_lower += 1
    elif symbol.isupper():
        symbol_upper += 1
    elif symbol.isdigit():
        symbol_digit += 1
all_symbols = symbol_punctuation + symbol_lower + symbol_upper + symbol_digit
if symbol_upper != 0 and symbol_lower != 0 \
        and symbol_digit != 0 and symbol_punctuation != 0 \
        and all_symbols >= 8:
    print('Password complexity is 5')
    exit()

# 4 сложность
for symbol in enter_password:
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
    if symbol.islower():
        symbol_lower += 1
    elif symbol.isdigit():
        symbol_digit += 1
    elif symbol.isupper():
        symbol_upper += 1
if symbol_lower != 0 and symbol_digit != 0 and symbol_upper or \
        symbol_lower != 0 and symbol_upper != 0 and symbol_punctuation or \
        symbol_lower != 0 and symbol_digit != 0 and symbol_punctuation or \
        symbol_digit != 0 and symbol_upper != 0 and symbol_punctuation:
    print('Password complexity is 4')
    exit()

# 3 сложность
for symbol in enter_password:
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
    if symbol.islower():
        symbol_lower += 1
    elif symbol.isdigit():
        symbol_digit += 1
    elif symbol.isupper():
        symbol_upper += 1
if symbol_lower != 0 and symbol_digit != 0 or \
        symbol_lower != 0 and symbol_upper != 0 or \
        symbol_lower != 0 and symbol_punctuation != 0 or \
        symbol_digit != 0 and symbol_upper != 0 or \
        symbol_digit != 0 and symbol_punctuation != 0 or \
        symbol_upper != 0 and symbol_punctuation != 0:
    print('Password complexity is 3')
    exit()

# 2 сложность
for symbol in enter_password:
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
if enter_password.islower() or \
        enter_password.isupper() or \
        enter_password.isdigit() or \
        symbol_punctuation != 0:
    print('Password complexity is 2')
    exit()

# Напишите программу где пользователь вводит число symbol_len,
# а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше.
# Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789' * 2
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

symbol_len = 0
password = ''

while True:
    symbol_len = int(input('Enter the symbols to generate a password >: '))
    if symbol_len < 4:
        print('Error: invalid digit, repeat input', end='\n\n')

    else:
        for i in range(symbol_len):
            password += random.choice(lower_case + upper_case + digits + punctuation)
        print(f'Your {symbol_len} digit password is >: {password}')
        break

# Задание 1:
# Пользователь вводит слово, если это слово является
# полиндромом, то вывести '+', иначе '-'

enter_text = input('Enter text >: ')

if enter_text == enter_text[::-1]:
    print('+')
else:
    print('-')

# Задание 2:
# Пользователь вводит текст и слово которое нужно найти,
# если это слово есть в тексте, вывести 'YES', иначе 'NO'

enter_text = input('Enter text >: ')
wd = input('Enter a search term >: ')

new_text = enter_text.split()
if wd not in new_text:
    print('NO')
    exit(4)
if new_text.index(wd) != -1:
    print('YES')

# Задание 3:
# Пользователь вводит строку. Если она начинается на 'abc',
# то заменить их на 'www', иначе добавить в конец строки 'zzz'.

enter_text = input('Enter text >: ')
end_str = 'zzz'

if enter_text.startswith('abc'):
    print(enter_text.replace('abc', 'www'))
else:
    enter_text += end_str
    print(enter_text)


# Пользователь вводит текст, удалить в
# тексте все цифры и вывести строку пользователю.

test_string = input('Enter test string >: ')
new_string = ''
list_number = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

for symbol in test_string:
    if symbol not in list_number:
        new_string += symbol
print(new_string)


# Задание 5:
# Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
# что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

test_string = input('Enter test string >: ')

if test_string.find('@') != -1 and \
        test_string.find('.') != -1:
    print('YES')
else:
    print('NO')


# Задание 6:
# Пользователь вводит строку в котором есть буквы и цифры,
# необходимо из этой строки спарсить целое число.

test_string = input('Enter test string >: ')
new_string = ''
list_number = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

for symbol in test_string:
    if symbol in list_number:
        new_string += symbol
print(new_string)

# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список


list_number = []
for i in range(0, 5):
    list_number.append(int(input(f'Enter number {i + 1} >: ')))
print(f'Your list = {list_number}')

# Задание 2:
# Дан список A = [1, 2, 3, 4, 5]
# Удалить последнее число из списка

A = [1, 2, 3, 4, 5]
A.pop()
print(A)

# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N


A = []
for i in range(0, 10):
    A.append(int(input(f'Enter number {i + 1} >: ')))
B = int(input('Enter number N >: '))
amount_N = 0
for j in A:
    if j == B:
        amount_N += 1

print(f'In the list A the number N is repeated {amount_N} times')

# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности

A = []
B = int(input('Enter number N >: '))
for i in range(0, B):
    A.append(int(input(f'Enter number {i + 1} >: ')))

A.reverse()
print(f'revers A = {A}')

# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

A = []
C = []

for i in range(0, 5):
    A.append(int(input(f'Enter number {i + 1} >: ')))
for j in A:
    if j > 5:
        C.append(j)
print(f'C (number > 5) = {C}')

# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла
# (запрещено использовать функцию min и max).
# Вывести эти числа.

A = []
B = int(input('Enter number N >: '))

for i in range(0, B):
    A.append(int(input(f'Enter number {i + 1} >: ')))

min_value = A[0]
max_value = 0

for j in A:
    if j > max_value:
        max_value = j
    elif j < min_value:
        min_value = j

print(f'min_value = {min_value}, max_value = {max_value}')

# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Количество цифр: 3

amount_digits = 0
new_string = ''
text = input('Enter text >: ')
text = text.split(' ')

for i in text:
    if i.isdigit():
        amount_digits += 1

print(f'amount_digits = {amount_digits}')

# 1 Дан многомерный список. Вывести на экран первый и последний столбцы.
# Пример
# исходный список
# [1 6 8 5 4 0 3]
# [5 7 8 9 4 2 1]
# [6 0 7 8 1 2 5]
# [5 7 2 7 5 2 1]
# результат работы кода с задания 1
# 1 3
# 5 1
# 6 5
# 5 1

a = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
]

for i in range(len(a)):
    print(a[i][0], a[i][-1])

# 2 Дан многомерный список. Вывести на экран все четные столбцы,
# у которых первый элемент больше последнего.
# исходный список
# [1 6 8 5 4 0 3]
# [5 7 8 9 4 2 1],
# [6 0 7 8 1 2 5],
# [5 7 2 7 5 2 1]

# результат работы кода с задания 2
# 8 3
# 8 1
# 7 5
# 2 1

a = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
    ]

for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        if j % 2 == 0 and a[0][j] > a[-1][j]:
            print(a[i][j], end=' ')

# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.


print('Is this game X or 0!')
print('Enter symbols X or 0 according to the scheme\n'
      '1 | 2 | 3 \n'
      '---------\n'
      '4 | 5 | 6 \n'
      '---------\n'
      '7 | 8 | 9 \n')

a = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def my_print():
    print(a[0])
    print(a[1])
    print(a[2])
    print()


my_print()

for i in range(0, 9):
    value = input(f'Move #{i + 1} - enter symbol(only x or 0)>: ')
    cell_number = int(input(f'Move #{i + 1} - enter cell number(only digit)>: '))
    if cell_number > 9 or cell_number < 1:
        print('Error: you entered an invalid character, restart the game!')
        exit()
    if cell_number == 1:
        a[0][0] = value
        my_print()
    elif cell_number == 2:
        a[0][1] = value
        my_print()
    elif cell_number == 3:
        a[0][2] = value
        my_print()
    elif cell_number == 4:
        a[1][0] = value
        my_print()
    elif cell_number == 5:
        a[1][1] = value
        my_print()
    elif cell_number == 6:
        a[1][2] = value
        my_print()
    elif cell_number == 7:
        a[2][0] = value
        my_print()
    elif cell_number == 8:
        a[2][1] = value
        my_print()
    elif cell_number == 9:
        a[2][2] = value
        my_print()

    zero = a[0][0] == a[0][1] == a[0][2] == '0' or \
           a[1][0] == a[1][1] == a[1][2] == '0' or \
           a[2][0] == a[2][1] == a[2][2] == '0' or \
           a[0][0] == a[1][0] == a[2][0] == '0' or \
           a[0][1] == a[1][1] == a[2][1] == '0' or \
           a[0][2] == a[1][2] == a[2][2] == '0' or \
           a[0][0] == a[1][1] == a[2][2] == '0' or \
           a[0][2] == a[1][1] == a[2][0] == '0'
    if zero:
        print('VICTORY PLAYER "0"!')
        exit()

    xero = a[0][0] == a[0][1] == a[0][2] == 'x' or \
           a[1][0] == a[1][1] == a[1][2] == 'x' or \
           a[2][0] == a[2][1] == a[2][2] == 'x' or \
           a[0][0] == a[1][0] == a[2][0] == 'x' or \
           a[0][1] == a[1][1] == a[2][1] == 'x' or \
           a[0][2] == a[1][2] == a[2][2] == 'x' or \
           a[0][0] == a[1][1] == a[2][2] == 'x' or \
           a[0][2] == a[1][1] == a[2][0] == 'x'
    if xero:
        print('VICTORY PLAYER "X"!')
        exit()

    if i >= 8:
        print('DRAW!')


# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.

print('Is this game X or 0!')
print('Enter symbols X or 0 according to the scheme\n\n'
      'num_1|num_2|num_3\n'
      '-----------------\n'
      'num_4|num_5|num_6\n'
      '-----------------\n'
      'num_7|num_8|num_9\n\n')

a = []
h = 1
for _ in range(3):
    b = []
    for n in range(3):
        number = str(input(f'num_{h}: '))
        h += 1
        b.append(number)
        if number != '0' and number != 'x':
            print('Error: invalid symbol, restart the game!', end='\n\n')
            exit(4)
    a.append(b)
print(a[0], end='\n')
print(a[1], end='\n')
print(a[2], end='\n')

for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        if a[0][0] == a[0][1] == a[0][2] == '0' or \
                a[1][0] == a[1][1] == a[1][2] == '0' or \
                a[2][0] == a[2][1] == a[2][2] == '0' or \
                a[0][0] == a[1][0] == a[2][0] == '0' or \
                a[0][1] == a[1][1] == a[2][1] == '0' or \
                a[0][2] == a[1][2] == a[2][2] == '0' or \
                a[0][0] == a[1][1] == a[2][2] == '0' or \
                a[0][2] == a[1][1] == a[2][0] == '0':
            print('Victory player 0!')
            exit()
        elif a[0][0] == a[0][1] == a[0][2] == 'x' or \
                a[1][0] == a[1][1] == a[1][2] == 'x' or \
                a[2][0] == a[2][1] == a[2][2] == 'x' or \
                a[0][0] == a[1][0] == a[2][0] == 'x' or \
                a[0][1] == a[1][1] == a[2][1] == 'x' or \
                a[0][2] == a[1][2] == a[2][2] == 'x' or \
                a[0][0] == a[1][1] == a[2][2] == 'x' or \
                a[0][2] == a[1][1] == a[2][0] == 'x':
            print('Victory player x!')
            exit()
        else:
            print('Draw!')
        exit()


# Задание #1:
# Дано два множества A и B
# В множестве А находятся имена должников за Сентябрь
# В множестве B находятся имена должников за Октябрь
# Найти:
# * Вывести имена людей которые должны за Сентябрь и Октябрь
# * Вывести должников за Октябрь у которых нет долга за Сентябрь

A_debtors_sept = {"vasia", "petia", "kolia", "sasha", "vadim", "misha"}
B_debtors_okt = {"vasia", "tima", "kolia", "galia", "fedia", "platon", "misha"}

print(f'debtors september and oktober = {A_debtors_sept.intersection(B_debtors_okt)}')
print(f'debtors only for october = {B_debtors_okt.difference(A_debtors_sept)}')


# Задание #2:
# Права доступа
# Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
# запись – W;
# чтение – R;
# запуск – X.
# На вход программе подается:
# число n – количество файлов;
# n строк с именами файлов и допустимыми операциями;
# число m – количество запросов к файлам;
# m запросов вида «операция файл».
# Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
# Пример ввода:
# 3
# python.exe X
# book.txt R W
# notebook.exe R W X
# 5
# read python.exe
# read book.txt
# write notebook.exe
# execute notebook.exe
# write book.txt
# Пример вывода:
# Access denied
# OK
# OK
# OK
# OK

action = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file = {}
for i in range(int(input('Enter number of files(digit) >: '))):
    name, *operations = input(f'Enter a string with the file name and allowed operations {i+1}>: ').split()
    file[name] = set(operations)

for j in range(int(input('Enter number of file requests(digit) >: '))):
    request, name = input(f'Enter request {j+1}>: ').split()
    if action[request] in file[name]:
        print('OK')
    else:
        print('Access denied')


# Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк

import pickle

data = [{
    'age': '30',
    'sex': 'Man',
    'city': 'Kiev'
    },
    {
     'age': '40',
     'sex': 'Woman',
     'city': 'Dnipro'
    },
    {
     'age': '50',
     'sex': 'Man',
     'city': 'Odessa'
    },
]

with open('my_file.bin', 'wb') as f:
    pickle.dump(data, f)

# with open('my_file.bin', 'rb') as f:
#     print(pickle.load(f))

# Дано два словаря
# A = {'key': 1}
# B = {'key1: 2}
# Необходимо написать код который будет их объединять
# C = {'key': 1, 'key1': 2}
# Но нужно так-же учитывать коллизии,
# например ситуация когда у нас два одинаковых ключа и
# чтобы не потерять значения нужно записать в один ключ список
# в котором будут находится значения
# Например:
# A = {'key': 1, 'key2': True}
# B = {'key': 'Hello'}
# C = {'key': [1, 'Hello'], 'key2': True}
# Записать результат в файл result.json в формате JSON.

import json

with open('result.json') as f:
    print(json.load(f))
A = {'key': 2, 'key1': True}
B = {'key': 'Hello4', 'key1': False, 'key2': 'World'}
C = dict.copy(A)


for key, value in B.items():
    if C.get(key):
        C[key] = [C[key], value]
    else:
        C[key] = value

with open('result.json', 'w') as f:
    json.dump(C, f)


# Напишите функцию change(lst), которая принимает список и меняет местами его первый
# и последний элемент.
# В исходном списке минимум 2 элемента.

def change(lst: list) -> list:
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


a = [4, 8, 2, 'qwert', '@#$']
print(change(a))

# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

def to_dict(lst):
    # return {lst[i]: lst[i] for i in range(0, len(lst))}
    return dict(zip(lst, lst))


lst = [4, 15, 254, 'qwer', '123@@']

print(to_dict(lst))


# Напишите функцию sum_range(start, end), которая суммирует все
# целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sun_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


print(sun_range(1, 3))


# Напишите функцию read_last(lines, file), которая будет открывать определенный
# файл file и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).

def read_last(lines, file):
    if lines > 0:
        with open(file) as f:
            file_lines = f.readlines()[-lines:]
        for i in file_lines:
            print(i.strip())
    else:
        print('Error is not a positive integer')


read_last(3, 'text.txt')


# Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за
# расположение элемента в списке.
# Position всегда должен быть последовательным, например у нас есть список
# data = [
# {'name': 'Test 1', 'position': 1},
# {'name': 'Test 2', 'position': 2},
# {'name': 'Test 3', 'position': 3},
# ]
# И мы хотим удалить элемент у которого position = 2,
# то на выходе мы должны получить следующий список:
# data = [
# {'name': 'Test 1', 'position': 1},
# {'name': 'Test 3', 'position': 2},  # -1
# ]
# Придерживаясь такой логики, необходимо реализовать:
# 1. Удаление элемента
# Функционал необходимо реализовать с помощью функций!
import pprint

data = [
    {
        'name': 'Test 1',
        'position': 1
    },
    {
        'name': 'Test 2',
        'position': 2
    },
    {
        'name': 'Test 3',
        'position': 3
    },
    {
        'name': 'Test 4',
        'position': 4
    },
    {
        'name': 'Test 5',
        'position': 5
    }
]


def del_pos(lst, pos_num):
    lst.pop(pos_num - 1)
    for key, value in enumerate(lst):
        value['position'] = (key + 1)
    return lst


pprint.pprint(del_pos(data, 3))

# Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за
# расположение элемента в списке.
# Position всегда должен быть последовательным, например у нас есть список
# 2. Добавление элемента с любым position, например мы хотим в наш исходный список добавить элемент
# у которого position = 1, то должны получить:
# data = [
# {'name': 'Test 4', 'position': 1}
# {'name': 'Test 1', 'position': 2},  # +1
# {'name': 'Test 2', 'position': 3},  # +1
# {'name': 'Test 3', 'position': 4},  # +1
# ]
# Функционал необходимо реализовать с помощью функций!
import pprint

data = [
    {
        'name': 'Test 1',
        'position': 1
    },
    {
        'name': 'Test 2',
        'position': 2
    },
    {
        'name': 'Test 3',
        'position': 3
    }
]


def add_pos(lst, pos_num, pos):
    new_dict = {'name': f'{pos} {len(lst) + 1}', 'position': None}
    lst.insert(pos_num - 1, new_dict)

    for key, value in enumerate(lst):
        value['position'] = (key + 1)
    return lst


pprint.pprint(add_pos(data, 2, 'Test'))

# 3. Поменять элементы местами, например position 1 и position 3,
# то должны получить следующий список:
# data = [
# {'name': 'Test 3', 'position': 1},
# {'name': 'Test 2', 'position': 2},
# {'name': 'Test 1', 'position': 3},
# ]
# Функционал необходимо реализовать с помощью функций!
import pprint

data = [
    {
        'name': 'Test 1',
        'position': 1
    },
    {
        'name': 'Test 2',
        'position': 2
    },
    {
        'name': 'Test 3',
        'position': 3
    }
]


def change_pos(lst, pos_1, pos_2):
    lst.insert(pos_1 - 1, lst[pos_2 - 1])
    lst.pop(pos_2)
    lst.insert(pos_2, lst[pos_1])
    lst.pop(pos_1)

    for key, value in enumerate(lst):
        value['position'] = (key + 1)
    return lst


pprint.pprint(change_pos(data, 1, 3))

# Необходимо создать класс Human с атрибутами:
# name
# surname
# age
# phone
# address
# Атрибуты должны заполняться в методе __init__
# Так-же нужно написать методы:
# get_info() - который возвращает словарь в котором находится информация о человеке
# call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
# Нужно создать 3 обьекта класса Human и вызвать у них метод get_info

class Human:

    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return [self.name, self.surname, self.age, self.phone, self.address]

    def call(self, phone_number):
        print(f"{self.phone} вызывает абонента {phone_number}")


vasia = Human('vasia', 'pupkin', 20, 380991111111, 'kiev')
petia = Human('petia', 'mupkin', 21, 380992222222, 'lviv')
kolia = Human('kolia', 'tupkin', 22, 380993333333, 'odessa')

print(vasia.get_info())
print(petia.get_info())
print(kolia.get_info())
vasia.call(380663332211)

