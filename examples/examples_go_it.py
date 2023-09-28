print('hello world', 1, 2, sep='\n')
print('* ' * 5)
print((5 * '# ' + '\n') * 5)

a = ('# ' * 5) + '\n'
for i in range(1, 5):
    i = a * 5
print(ord('q'))

num = int(input("Enter the integer (0 to 100): "))
sum = 1
i = 1
while i != num:
    i += 1
    sum += i
    print(sum)

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
gcd = None
if first < second:
    gcd = first
else:
    gcd = second
while first % gcd != 0 or second % gcd != 0:
    gcd -= 1
print(gcd)
data = '25'
print(data.isnumeric())

number = int(input('Enter the: '))
print(type(number))

num = None
sum = 0
while num != 0:
    num = int(input("Enter integer (0 for output): "))
    for i in range(num + 1):
        sum += i
        # print(i)
        print(sum)

message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for i in message:
    if i.isupper():
        c_unicode = ord(i)
        c_index = ord(i) - ord("A")
        new_index = (c_index + offset) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        encoded_message += new_character
    elif i.islower():
        c_unicode = ord(i)
        c_index = ord(i) - ord("a")
        new_index = (c_index + offset) % 26
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        encoded_message += new_character
    elif i.isspace():
        encoded_message += " "
    elif i == "!":
        encoded_message += "!"
print(encoded_message)
print(ord('A'))
print(chr(65))
try:
    pool = 1000
    quantity = int(input("Enter the number of mailings: "))
    chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')

result = None
operand = None
operator = None
wait_for_number = True

while True:
    if operator == '=':
        print(f"Result: {result}")
        break
    elif wait_for_number:
        while True:
            try:
                operand = float(input("Enter number: "))
            except ValueError:
                print("Oops! It is not a number. Try again.")
            else:
                if result is None:
                    result = operand
                else:
                    if operator == '+':
                        result += operand
                    elif operator == '-':
                        result -= operand
                    elif operator == '*':
                        result *= operand
                    elif operator == '/':
                        result /= operand
                break
        wait_for_number = False
    else:
        while True:
            operator = input("Enter one of operators +, -, *, /, =: ")
            if operator in ('+', '-', '*', '/', '='):
                break
            else:
                print("Oops! It is not a valid operator. Try again.")
        wait_for_number = True

n = int(input('enter n: '))
number = 0
while number < n:
    number += 3
    print(number)

a = int(input('enter a: '))
b = int(input('enter b: '))
n = a * '*'
h = 0
while h != b:
    h += 1
    print(n)

import math

print(math.ceil(2.1))
print(math.floor(2.7))
print(round(2.1))

print('ltrh' not in 'Hello')
operator = 4
if operator == 4:
    print('Hello')

import re

s = "I am 25 years old"
age = re.search('\d+', s)
print(age)

age = 9
if age % 2 == 0:
    print('hello')
    exit(4)
print('vasia')

number = int(input('Введите трехзначное число>: '))
new_number_1 = number % 10
print(new_number_1)
temp_number = number // 10
print(temp_number)
new_numbers_2 = temp_number % 10
print(new_numbers_2)
new_numbers_3 = temp_number // 10
print(new_numbers_3)

print(f'Новое перевернутое число: {new_number_1}{new_numbers_2}{new_numbers_3}')

first_haus = 3.5 * 50
second_haus = 4 * 60
count = 3 * 2 * 0.25
finally_1 = first_haus // count
finally_2 = second_haus // count
print(finally_1, finally_2)

a = float(input('enter a: '))
b = float(input('enter b: '))
print(- b / a)

from decimal import Decimal

sec = Decimal(input('enter the sec: '))
hours = sec // Decimal(3600)
hours_2 = hours * Decimal(3600)
minutes = (sec - hours) // Decimal(60)
seconds = sec - hours - (minutes * Decimal(60))
print(hours, ':', minutes, ':', seconds)

N = int(input('Enter N>: '))
h = 1
while N >= 1:
    print((N - 1) * ' ' + h * '*')
    h += 1
    N -= 1

num = int(input('enter num: '))
print('even' if num % 2 == 0 else 'odd')

arrr = [34, 15, 88, 2]


def sum_arrr(arrr):
    sum = 0
    for i in arr:
        sum += i
    print(sum)
sum_arrr(arrr)

def sum_arr(arr):
    arr = [78, 56, 232, 12, -11, 43]
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + find_smallest_int(arr[1:])




def find_smallest_int(arr):
    min_int = arr[0]
    for i in arr:
        if i < min_int:
            min_int = i
    return min_int


print(find_smallest_int(arr))

arr = [78, 56, 232, 12, -11, 43]
print(min(arr))

arr = [78, 56, 232, 12, -11, 43]
arr.sort()
print(arr[0])


def football_points(wins, draws, losses):
    sum = wins * 3 + draws * 1 + losses * 0
    return sum


print(football_points(3, 4, 2))


def are_numbers_equal(a, b):
    return True if a == b else False


def find_smallest_number(my_list):
    a = my_list[0]
    for i in my_list:
        if i < a:
            a = i
    return a


def less_than_100(a, b):
    return True if (a + b) < 100 else False


def difference(nums):
    return max(nums) - min(nums)


print(difference([10, 15, 20, 2, 10, 6]))


def hello_name(name):
    return f'Привет, {name}!'


print(0 / 100)


def divisible(num):
    return True if num / 100 == 0 or \
                   num // 100 > 0 or num / 100 <= - 1 else False


print(divisible(0))


def is_empty(string):
    return False if string else True


print(is_empty(' '))

while True:
    try:
        age = int(input('How old are you?: '))
        if age >= 18:
            print('Access allowed')
            break
        else:
            print('Access denied')
            break
    except ValueError:
        print(f'age is not a number, please enter a number')
    finally:
        print('-' * 30)


def divides_evenly(a, b):
    return True if a % b == 0 else False


print(divides_evenly(85, 4))


def isEvenOrOdd(number):
    return 'четное' if number % 2 == 0 else 'нечетное'


def greeting():
    print('Hello world')


greeting()

print(bool(1 and 1))


def flip_bool(boolean):
    return False if boolean == 1 else True


default_name = 'Unknown'
name = input('Please enter a name: ')
current_name = name or default_name
print(f'you name is {current_name}')

while True:
    name = input('Please enter a name: ')
    print(name)
    if not name:
        print('end')
        break  # break or continue

list_goods = ''
while True:
    goods = input('take a goods: ') + ',' + '\n'

    if goods == 's' + ',' + '\n':
        new_list = list_goods[:-2]
        break
    list_goods += goods

print(new_list)

a = input('Enter a>: ')
if a not in 'vadim':
    print('yes')
elif ...:
    pass
else:
    print('no')

a = 'abcdefghijklmnopqrstuvwxyz'
for latter in a:
    print(latter)
    if latter == 'b':
        break
print('end')


def google(number):
    for i in range(number):
        number -= 1
        print(f"G{'o' * number}gle")


google(3)

start = int(input('enter start>: '))
stop = int(input('enter stop>: '))
for i in range(start, stop + 1):
    print(i, end=', ')


def new_word(word):
    return word[::-1], word[1::]


print(new_word('apple'))

try:
    while True:
        print('end')
        int('asd')
except KeyboardInterrupt or TypeError:
    print('wtf')
except ValueError as error:
    print(error)

try:
    int('asd')
except (ValueError, TypeError, OverflowError):
    print('wtf')
except:
    print('wtf!!!!!')

while True:
    try:
        user_data = int(input('enter your old>: '))
    except ValueError as error:
        print(f'incorrect input, chould be {error}')
    else:
        break
current_year = 2022
year_of_birth = current_year - user_data
print(year_of_birth)

result = 0
first = 1
positions = 25

print(f"step 0 = 0")
for _ in range(first, positions):
    first, result = result, first + result
    print(f"step {i} = {result}")

result = 0
first = 1
positions = 25
for _ in range(0, 25):
    first, result = result, first + result
print(first, result)

while True:
    try:
        a = input('enter the numb>: ')
        int_a = int(a)
        if not int_a % 2:
            print("numb is even")
            continue
        else:
            print("numb is odd")
            continue
    except ValueError:
        print(f"{a} is not number")


def NOT(num):
    return 1 if not num else 0


print(NOT(0))


def AND(num, num2):
    return 1 if num and num2 else 0


print(AND(0, 0))


def OR(num, num2):
    return 1 if num or num2 else 0


print(OR(0, 1))


def distance_home(my_list):
    return abs(sum(my_list))


print(distance_home([-1, -4, -3, -2]))


def should_serve_drinks(age, on_break):
    return True if age >= 18 and not on_break else False


print(should_serve_drinks(3, False))


def flip(y):
    return 0 if y == 1 else 1


def how_many_stickers(n):
    return (n ** 2) * 6


print(how_many_stickers(4))


def inches_to_feet(inches):
    return inches / 12 if inches >= 12 else 0


def max_num(a, b):
    if a > b:
        print(f'max = a = {a}')
    elif a < b:
        print(f'max = b = {b}')
    else:
        print('a = b')


max_num(3, 2)


def total(*args):
    for i in args:
        print(i)


print(total(10, 1, 2, 3, 4))


def totall(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print(totall(Jack=1123, John=2231, Inge=1560))


def total(*tuples_1, **tuples_2):
    print(tuples_1, tuples_2)
    for it in tuples_1:
        print(it)


total(1, 2, 3, vad=12, add=23, vsub=24)

my_tuple = tuple()
another_tuple = ()

empty_dict = {}
another_empty_dict = dict()

some_dict = {
    "key": "value",
    1: "one",
}

not_empty = {"key": "value"}
not_empty["new_key"] = "new value"
not_empty['1'] = '2'
print(not_empty)


def factorial(n):
    if n <= 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


print(factorial(5))

import math

sin_pi = math.sin(math.pi)
print(sin_pi)

from math import sin, pi

sin_pi = sin(pi)
print(sin_pi)


def is_safe_bridge(s):
    space = 0
    for symbol in s:
        if symbol.isspace():
            space += 1
    if space != 0:
        return False
    else:
        return True


print(is_safe_bridge('# ####'))


def has_key(dictionary, key):
    return True if key in dictionary else False


print(has_key({"ночной": True, "дожор": True}, "дозор"))
print(has_key({"кот": 1, "коt": "код", "рот": 3}, "код"))


def how_many_potatoes(some_string):
    a = some_string.split()
    print(a)
    b = 0
    for i in range(len(a)):
        if a[i] == 'картошка' or a[i] == 'картошка,':
            b += 1
    return b


print(how_many_potatoes("лук, картошка, капуста, картошка, картошка"))


def is_empty(dictionary):
    return True if len(dictionary) == 0 else False


print(is_empty({}))  # True
print(is_empty({"a": 1}))  # False


def match(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return True if s1 == s2 else False


print(match("привет", "прИВеТ"))  # True
print(match("кот", "код"))  # False


def last_ind(lst):
    return lst[-1] if lst else None


print(last_ind([0, 4, 19, 34, 50, -9, 2]))  # 2
print(last_ind("Серая лисичка перепрыгнула ленивую собаку"))  # "у"
print(last_ind([]))  # None

string = 'agsa'
if string == string[:: -1]:
    print('yes')
else:
    print('no')

import random

help(random)

base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global total_trip
    total_trip += 1
    total = base_rate + price_per_km * path
    return float(total)


trip_price(11)
print(total_trip)


def discount_price(price, discount):
    price = int(price)
    discount = float(discount)

    def apply_discount():
        nonlocal price
        price = price - (price * discount)

    apply_discount()
    return price


print(discount_price(200, 0.07))


def get_fullname(first_name, last_name, middle_name=None):
    if first_name and middle_name and last_name:
        return f'{first_name} {middle_name} {last_name}'
    elif first_name and last_name:
        return f'{first_name} {last_name}'


print(get_fullname('vad', 'trub', 'valent'))


def format_string(string, length):
    if len(string) >= length:
        return string
    elif len(string) < length:
        space = (length - len(string)) // 2
        print(space)
        string = ' ' * space + string
        return string
        print(string)


print(format_string(length=15, string='abaa'))


def first(size, *poz_1):
    return size + len(poz_1)


def second(size, **poz_2):
    return size + len(poz_2)


first(5, "first", "second", "third")
first(1, "Alex", "Boris")
second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris")


def cost_delivery(quantity, *_, discount=0):
    result = (5 + 2 * (quantity - 1)) * (1 - discount)  # решение с сайта
    fin_sum = (5 + 2 * (quantity - 1))  # мое решение
    fin_sum = fin_sum - (fin_sum * discount)
    return fin_sum


print(cost_delivery(2, 1, 2, 3))  # == 7
print(cost_delivery(3, 3))  # == 9)
print(cost_delivery(1))  # == 5
print(cost_delivery(2, 1, 2, 3, discount=0.5))  # == 3.5


def factorial(a):
    if a < 2:
        return 1
    else:
        return a * factorial(a - 1)


def number_of_groups(n, k):
    res = factorial(n) / (factorial(n - k) * factorial(k))  # Cnk = n! / ((n - k)! · k!)
    return int(res)


print(number_of_groups(50, 7))


def fibonacci(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))


def amount_payment(payment):
    result = 0
    for i in payment:
        if i > 0:
            result += i
    return result


print(amount_payment([1, -2, 3, 4, -3, 8, -5, 9, -10, 11]))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in a:
    print(str(i))
b = list(map(str, a))

b = ','.join(a)
print(b)


def get_vote_count(votes):
    a = []
    for _ in votes.values():
        result = votes['лайки'] - votes['дизлайки']
        return result


print(get_vote_count({"лайки": 2, "дизлайки": 5}))


def calc_kinetic_energy(m, v):
    return round(0.5 * m * v ** 2)


print(calc_kinetic_energy(63.5, 7.35))

list_number = []
for i in range(0, 5):
    list_number.append(int(input(f'Enter number {i + 1} >: ')))
print(f'Your list = {list_number}')

the_board = []
for i in range(10):
    the_board.append(f'{i + 1}')
print(the_board)


def get_max_number(a: int, b: int) -> list[int | int]:
    if not isinstance(a, int) or not isinstance(b, int):  # анотации типов данных
        raise ValueError('a and b must be integers')
    return a + b


print(get_max_number(4, 2.4))


def count_true(my_list):
    count = 0
    for i in my_list:
        if i:
            count += 1
    return count


print(count_true([True, False, False, True, False]))  # 2
print(count_true([False, False, False, False]))  # 0
print(count_true([]))  # 0


def get_filename(path):
    for i in path:
        a = path.rfind('/')
        return path[a + 1::]


def get_filename(path):
    return path.split('/')


print(get_filename('C:/Windows/system32/secret/php_tutorials.avi'))
print(get_filename('virus.exe'))

''''' TODO: remove dfbfdfb'''''


def count_syllables(string):
    string = string.lower()
    string_mini = string[:2:]

    return len(string.split(string_mini)) - 1


def count_syllables(string):
    return len(string) // 2


print(count_syllables("Hehehehehehe"))

import string

string.punctuation()

n = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]
for i in range(len(n)):
    a, *args, b = n[i]
    print(a, b)

n = [1, 2, 3, 4, 5, 6]
a, *args, b = n
print(a, b)

a = [1, 2, 3, 4, 5, 6]
print(*a, sep='/')

n = [[1, 2, 3],
     [1, 5, 6],
     [7, 8, 9]
     ]
print(n[0][0] == n[1][0])
print(n[0][0] is n[1][1])

numbers = {
    "1": "one",
    2: "two",
    3: "three"
}
for key in numbers.keys():
    for value in numbers.values():
        for key, value in numbers.items():
            print(type(key), key, type(value), value)

a = set('hello')
b = set('world')
print(a and b, a ^ b)

points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
}
for i, j in points.items():
    print(i, j)

a = (1,)

user = {
    "name": "Bill",
    "surname": "Bosh",
    "age": 22
}

if "age" in user:
    print(f"User is {user['age']} years old.")

password = input("Password: ")
if len(password) < 8:
    print("Your password is too short")

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char)

from pathlib import Path

p = Path('/home/user/Downloads')
print(p)

from pathlib import Path

p = Path()  # p # Указывает на папку из которой был запущен Python

# p.parent указывает на родительскую папку;
# p.name возвращает только имя (строкой) папки или файла, на который указывает p;
# p.suffix возвращает строкой расширение файла, на который указывает p, начиная с точки;
p = Path('setup.py')
p.suffix  # '.py'
p.exists()  # возвращает True или False, в зависимости от того, существует ли такой файл или папка;
p.is_dir()  # возвращает True, если p указывает на папку, и False, если на файл, или такой путь не существует;
p.is_file()  # возвращает True, если p указывает на файл, и False, если на папку, или такой путь не существует;
p.iterdir()  # возвращает итератор по всем файлам и папкам внутри папки p;
from pathlib import Path

p = Path('/home/user/Downloads')  # p Указывает на папку /home/user/Downloads
for i in p.iterdir():
    print(i.name)  # Выведет в цикле имена всех папок и файлов в /home

import sys

for arg in sys.argv:
    print(arg)
# python echo.py test --user -hello some text

import sys


def main():
    print(sys.argv[1])


a = [5, 3, 4, 6, 7, 9]
b = a.sort()
print(a)
c = sorted(a)
print(c)

help(list)

a = {'a': 1,
     'b': 2,
     'c': 3
     }
print(a.keys())
print(a.values())
print(a.items())

a = [1, 4, 5, 6, 9, 2, 3]


def prepare_data(data):
    data.sort()
    return data[1:-1]


print(prepare_data(a))


def format_ingredients(items):
    if len(items) > 1:
        a = items.pop()
        a = ' and ' + a
        b = ', '.join(items) + a
        return b
    else:
        return ''.join(items)


print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))

a = 2
b = 3
print(hex(id(a)))
print(hex(id(b)))
a, b = b, a

print(hex(id(a)))
print(hex(id(b)))

import sys

a = 'hello world'
b = a
print(sys.getrefcount(True))

x = 3
y = 3
a = []
for i in range(x):
    b = []
    for j in range(y):
        number = int(input(f'enter number {i}, {j}: '))
        b.append(number)
    a.append(b)
print(a)


def nothing_is_nothing(*args):
    return all(args)
    for i in args:
        if not i:
            return False
    return True


print(nothing_is_nothing(0, False, [], {}))

list_1 = ['Hello', 'world', 'Petya']
for value in list_1:
    print(value)

for value in range(len(list_1)):
    print(list_1[value])
for index, value in enumerate(list_1):
    print(index, value)

a = [[i + 1 for i in range(3)]] * 3
a = [[i for i in range(3)] for j in range(3)]
print(a)
a = ''.join([i for i in "hello 123 wol456g" if i.isdigit()])
a = ''.join([i for i in "hello 123 wol456g" if i.islower()])
print(a)

typle = (1,)
typle1 = 1, 2, 4
print(type(typle), type(typle1))

import sys

l = [1, 2, 3, 4, 5, 6]
t = (1, 2, 4, 4, 4, 6)
a = t.count(4)
print(a)
print(sys.getsizeof(l))
print(sys.getsizeof(t))

a = {'F': 1,
     'FX': 2,
     'E': 3,
     'D': 3,
     'C': 4,
     'B': 5,
     'A': 5}


def get_grade(key):
    return a.get(key)


b = {'F': 'Unsatisfactorily',
     'FX': 'Unsatisfactorily',
     'E': 'Enough',
     'D': 'Satisfactorily',
     'C': 'Good',
     'B': 'Very good',
     'A': 'Perfectly'}


def get_description(key):
    return b.get(key)


def reverse_case(string):
    return string.swapcase()


print(reverse_case('Hello dfgFE'))

num_words = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
             6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: 'ноль'}


def convert_number_2_word(number):
    return num_words.get(number)


print(convert_number_2_word(8))


def get_case(string):
    if string.isupper():
        return 'верхний'
    elif string.islower():
        return 'нижний'
    else:
        return 'смешанный'


print(get_case('LKHOIH'))


def is_truthy(val):
    return 1 if val else 0


def lookup_key(data, value):
    a = []
    for k, v in data.items():
        if v == value:
            a.append(k)
    return a


print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))


def calculate_scores(string):
    A, B, C = 0, 0, 0
    for i in string:
        if i == 'А':
            A += 1
        elif i == 'Б':
            B += 1
        elif i == 'В':
            C += 1
    a = [A, B, C]
    return a


def calculate_scores(string):
    return [string.count(x) for x in 'АБВ']


print(calculate_scores("АБВБАВВ"))  # [2, 2, 3]


def reverse_capitalize(txt):
    if txt.islower():
        return txt[::-1].upper()
    else:
        return txt[::-1].lower()


print(reverse_capitalize("ghdth"))


def sort_word(word):
    word = list(word)
    word.sort()
    word = ''.join(word)
    # return word or  return ''.join(sorted(word))


print(sort_word("Unpredictable"))


def increment_items(my_list):
    a = []
    for i in my_list:
        i += 1
        a.append(i)
        my_list = a
    return a


def increment_items(lst):
    return [i + 1 for i in lst]


print(increment_items([0, 1, 2, 3]))


def is_palindrome(word):
    return True if word[::-1] == word else False


print(is_palindrome("abba"))

a = {'F': 'Unsatisfactorily',
     'FX': 'Unsatisfactorily',
     'E': ['Enough', 'Unsatisfactorily'],
     'D': 'Satisfactorily',
     'C': 'Good',
     'B': 'Very good',
     'A': 'Perfectly',
     'discount': 50
     }
print(a.get('discount', False))
print(a['E'][1])
for i in a:
    print(a[i])

students = [
    {
        'name': 'Petr',
        'mark': {
            '19.09': {
                'value': 80,
                'description': '...'
            },
            '29.09': {
                'value': 100,
                'description': None
            },
            '05.10': {
                'value': 99,
                'description': '...'
            }
        },
        'email': 'petr@gmail.com',
        'visits': [True, False, True, True],
    },
    {
        'name': 'Vasya',
        'mark': {
            '19.09': {
                'value': 100,
                'description': '...'
            },
            '29.09': {
                'value': 100,
                'description': None
            },
            '05.10': {
                'value': 99,
                'description': '...'
            }
        },
        'email': 'vasya@gmail.com',
        'visits': [True, True, True, True],
    },
]

for name in students:
    print(name['name'])


def volume_of_box(sizes):
    a = sizes.values()
    result = 1
    for i in a:
        result = result * i
        print(i)
    return result


def volume_of_box(sizes):
    w, l, h = sizes.values()
    return w * l * h


print(volume_of_box({"ширина": 2, "длина": 5, "высота": 1}))

from counter_char import *

text = 'Lorem ipsum dolor sit amet ' \
       'consectetur adipiscing elit ' \
       'sed do eiusmod'
counter_char(text)

from char_set import *

text = 'Quis autem vel eum iure reprehenderit, ' \
       'qui in ea \\ voluptate velit esse, ' \
       'quam nihil molestiae! consequatur, ' \
       'vel illum, qui dolorem eum fugiat, ' \
       'quo voluptas nulla pariatur? 33 ' \
       'At vero eos et accusamus et'
char_set(text)

from cast_split import *

text = 'Lorem ipsum, dolor sit amet ' \
       'consectetur adipiscing elit ' \
       'sed do eiusmod!!!'
cast_split(text)

def split_list(grade):
    low = []
    high = []
    result = (low, high)
    try:
        average_value = sum(grade) / len(grade)
    except ZeroDivisionError:
        return result
    average_value = round(average_value)
    print(average_value)
    for i in grade:
        if i <= average_value:
            low.append(i)
        else:
            high.append(i)
        result = (low, high)
    return low, high


print(split_list([1, 7, 3, 4, 5, 6, 8, 2, 9, 12]))

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9
}


def calculate_distance(coordinates):
    result = 0
    while len(coordinates) > 1:
        a, b = coordinates[0], coordinates[1]
        c = (a, b)
        del coordinates[0]
        for key, val in points.items():
            if c[0] > c[1]:
                c = (b, a)
            elif c == key:
                result += val
    return result


print(calculate_distance([0, 1, 3, 2, 0]))

user_1 = {"name": "Jane", "age": 21}
user_2 = {"name": "Moris", "age": 23}
user_3 = {"name": "Steve", "age": 24}

persons = [user_1, user_2, user_3]

for user in persons:
    for field in user:
        print(user.get(field))


def game(terra, power):
    for i in terra:
        for j in i:
            if power >= j:
                power += j
            else:
                break
    return power


print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))


def is_valid_pin_codes(pin_codes):
    if len(pin_codes) < 1:
        return False
    for i in pin_codes:
        if not type(i) == str:
            return False
        if len(i) != 4:
            return False
        if not i.isnumeric():
            return False
        if pin_codes.count(i) > 1:
            return False
    else:
        return True


print(is_valid_pin_codes(['0090', '9034', '0000']))

from random import randint


def get_random_password():
    string = ''
    for i in range(8):
        random_num = randint(40, 126)
        symbol = chr(random_num)
        string += symbol
    return string


print(get_random_password())


def is_valid_password(password):
    u = 0
    l = 0
    dig = 0
    for i in password:
        if i.isdigit():
            dig += 1
        elif i.isupper():
            u += 1
        elif i.islower():
            l += 1
    if len(password) == 8 and u != 0 and l != 0 and dig != 0:
        return True
    else:
        return False


# print(is_valid_password('cSfg5yhd'))

from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    i = 0
    while i <= 100:
        password = get_random_password()
        print(password)
        if is_valid_password(password):
            return password
        else:
            continue


print(get_password())
from pathlib import Path

print(Path())
my_path = Path('D:\\work_it\\Github\\GoIt_school\\temp_2.py')
my_path = Path('D:\work_it\Github')
my_path = my_path.parent
my_path = my_path.name
my_path = my_path.suffix
my_path = my_path.exists()
my_path = my_path.is_dir()
my_path = my_path.is_file()
my_path = my_path.iterdir()
for i in my_path.iterdir():
    if not i.is_file():
        print(i)
print(my_path)

import sys

print(sys.argv)

from pathlib import Path
import pprint


def parse_folder(path):
    files = []
    folders = []
    p = Path()
    for i in p.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)
    return f'files = {files}', f'folders = {folders}'


pprint.pprint(parse_folder('D:\work_it\Github\GoIt_school'))

import sys


def parse_args():
    result = sys.argv[1:]
    ' '.join(result)
    return result


print(parse_args())

import sys

print(sys.argv)

import re

s = "I am 3456 years old"
age = re.search('\d+', s)
print(age.group())

a = ['\n', '\f', '\r', '\t', '\v']


def real_len(text):
    string = ''
    for i in text:
        if i in a:
            continue
        string += i

    return len(string)


print(real_len('Alex\nKdfe23\t\f\v.\r'))

width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))

jingle_bells = "Jingle bells, jingle bells\nJingle all the way\rOh, what fun it is to ride\v In a one horse open sleigh"
print(jingle_bells)

import re

text = 'I bought 7 nuts for 6$ and 10 bolts for 3$.'
a = re.search('\d+', text)
print(a.group())

b = re.findall('\d+', text)
print(b)

сc = re.findall('\b\w{3}\b', text)
print(сc)

match = re.findall(r'\d\d\D\d\d\D\d\d', r'Телефон 23-12-12')
print(match)

0
96 - 567 - 86 - 67
inp = input('enter tel: +38')
pattern = re.search('^\(0?\d{2}\)?\d{3}-?\d{2}-?\d{2}$', inp)
# print(pattern)
try:
    if inp == pattern.group():
        print('OK! access allowed')
    else:
        print('STOP! access denied')
except AttributeError:
    print('STOP! access denied')

inp = input('enter email: ')
pattern = re.search('^\w+[@]\w+[.]\w{2,3}$', inp)
# print(pattern)
try:
    if inp == pattern.group():
        print('OK! access allowed')
    else:
        print('STOP! access denied')
except AttributeError:
    print('STOP! access denied')

log = 'fdgdgr145.34.56.67fdhfg34.34.56.67fdxn211.35.768.78ghn'
logs = 'POSTgdgr145.34.56.67fdhfg7fdxngrggdmalware.comhn'
0.0
.0
.0
255.255
.255
.255

ip_address = re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', log)
print(ip_address)
ip_addres = re.findall('^POST\w*\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\w*malware.com\w*', logs)
print(ip_addres)
print(re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', ip_addres[0]))

logs = '10.01.2023 10:18.43 fddgdgdfgv' \
       '10.01.2023 11:18.43 fddgdgdfgv' \
       '10.01.2023 12:18.43 fddgdgdfgv' \
       '10.01.2023 13:18.43 fddgdgdfgv' \
       '10.01.2023 14:18.43 fddgdgdfgv'
print(re.findall('\d{2}\.\d{2}.\d{2,4}\s1[10-12]', logs))

log = 'first_name: fdggfr, last_name: sfvdv, adress: feferg, tel: 437666574'
user_input = input('fild name: ')
result = re.findall(f'{user_input}:\s\w+\s?', log)
print(result)

user_pattern = '\d{10}'
string = '123443567890'


def findall(pattern, string):
    patterns = {'\d': lambda x: x.isdigit()}
    for key in patterns:
        if pattern.startswith(key):
            pattern_key = key
            n_times = int(pattern[pattern.find('{') + 1:pattern.find('}')])
    result_string = ''
    for char in string:
        if patterns[pattern_key](char):
            result_string += char
        else:
            result_string = ''
        if len(result_string) == n_times:
            return result_string


print(findall(user_pattern, string))

from re import fullmatch

LOGIN_RE = '[a-zA-Z0-9._]{3,10}'
PWD_RE = '[a-zA-Z0-9._!@#$%&]{8,15}'
user_db = {}


def check_input(reg_exp, user):
    if not fullmatch(reg_exp, user):
        raise ValueError(f'Input must be {reg_exp}')
    return True


def check_if_login_exist(login):
    global user_db
    return False if login in user_db else True


def register():
    global user_db, user_pwd, user_login
    login_check_result = False
    psw_check_result = False

    while True:
        if not login_check_result:
            user_login = input('New login>: ')
            login_check_result = check_if_login_exist(user_login)
            continue
        try:
            login_check_result = check_input(LOGIN_RE, user_login)
        except ValueError as error:
            print(error)

        if not psw_check_result:
            user_pwd = input('New password>: ')
        try:
            pwd_check_result = check_input(PWD_RE, user_pwd)
        except ValueError as error:
            print(error)
        return user_login, user_pwd


def login():
    global user_db

    user_login = input('login>: ')
    user_pwd = input('password>: ')
    try:
        return True if user_db[user_login]['pwd'] == user_pwd else False
    except KeyError:
        return False


while True:
    action = input('register or login(r or l)?: ')
    if action == 'r':
        user_login, user_pwd = register()
        user_db[user_login] = {'psw': user_pwd}
        print(user_db)
    elif action == 'l':
        if login():
            print('Welcome')
        else:
            print('Try again ...')

TODO
поиск
расширения
файла
files = ['video.avi', 'audio.mp3', 'document.html', 'folder', 'backup.tar.gz']
for file in files:
    try:
        index = file.rindex('.')
        sufix = file[index + 1:]
        print(f'File: ({file}), sufix: ({sufix})')
    except ValueError:
        print(f'File: ({file}), sufix: (not found)')

import re

text = 'first sentence, second sentence. ' \
       'third sentence! fourth sentence?'
sentences = re.split('[\.\,\!\?]', text)
print(sentences)

text = 'first sentence\n second sentence\n ' \
       'third sentence'
print(text)
sentences = text.split('\n')
new_text = '*'.join(sentences)
print(sentences)
print(new_text)

import pprint

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_dict = []
    for i in articles_dict:
        for k, v in i.items():
            if type(v) == str:
                r = v.split(' ')
                for j in r:
                    if key.lower() in j.lower() and letter_case is False:
                        new_dict.append(i)
                        break
                    if key in j and letter_case is True:
                        new_dict.append(i)
                        break
    return new_dict


pprint.pprint(find_articles('stark', letter_case=False))


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    return_phones = {
        'UA': [],
        'JP': [],
        'TW': [],
        'SG': []
    }
    for i in list_phones:
        b = sanitize_phone_number(i)
        if b.startswith('81'):
            return_phones['JP'].append(b)
            continue
        elif b.startswith('65'):
            return_phones['SG'].append(b)
            continue
        elif b.startswith('886'):
            return_phones['TW'].append(b)
            continue
        elif b.startswith('380'):
            return_phones['UA'].append(b)
            continue
        else:
            return_phones['UA'].append(b)
    return return_phones


print(get_phone_numbers_for_countries(['065-875-94-11', '(81)8765347', '8867658976', '657658976', '(65)765-89-77']))
{'UA': ['0658759411'], 'JP': ['818765347'], 'TW': ['8867658976'], 'SG': ['657658976', '657658977']}


def is_spam_words(text, spam_words, space_around=False):
    if space_around is True:
        for i in text.lower().split():
            for j in spam_words:
                if j + '.' == i:
                    return True
        return False

    if space_around is False:
        for i in text.lower().split():
            for j in spam_words:
                if j in i:
                    return True
        return False


print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))  # True))

spam_words = ['ло.']  # j
text = 'Мо ло. х'  # i
space_around = True

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    new_char = name.translate(TRANS)
    return new_char


print(translate('Вадим Валентиович'))

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    a = 0
    d = []
    for k, v in students.items():
        a += 1
        for key, val in grades.items():
            if v == key:
                d.append("{:>4}|{:<10}|{:^5}|{:^5}".format(a, k, v, val))
    return d


for el in formatted_grades(students):
    print(el)


def formatted_numbers():
    a = ["|{0:^10}|{1:^10}|{2:^10}|".format('decimal', 'hex', 'binary')]
    for i in range(16):
        s = "|{0:<10d}|{0:^10x}|{0:>10b}|".format(i)
        a.append(s)
    return a


for el in formatted_numbers():
    print(el)

for i in range(16):
    s = "|{0:<10d}|{0:^10x}|{0:>10b}|".format(i)
    print(s)


def free_shipping(order):
    sum = 0
    for i in order.values():
        sum += i
        if sum > 50:
            return True
    return False


print(free_shipping({"Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99}))


def get_extension(lst):
    a = []
    for i in lst:
        b = i.find('.')
        a.append(i[b + 1:])
    return a


print(get_extension(["проект1.jpg", "проект1.pdf", "проект1.mp3"]))

from pprint import pprint
from pathlib import *
import pprint

p = Path("temp/").mkdir(parents=True, exist_ok=True)
help(open)
file = open('temp_1.py', 'r', encoding='UTF8')
for line in file:
    print(line)

while True:
    data = file.read(1024)  # read first_symbolang
    data = file.readline()
    print(data)
    if not data:
        break

res = file.read(1)
res = file.readline()
pprint.pprint(res)

file.close()
print(file.name)
print(file.closed)

meneger
context
with open('temp_1.py', 'a', encoding='UTF8') as file:
    print(file.readline()[-1])
NAME = 'Last name'
MAIL = 'Login email'
with open('email.csv', 'r') as file:
    with open('email.html', 'a') as html:
        html.write('<ul>\n')
        headers = []
        for line in file:
            data = line.split(',')
            data[-1] = data[-1][:-1]
            if not headers:
                headers = data
                mail_index = headers.index(MAIL)
                name_index = headers.index(NAME)
                continue
            name = data[name_index]
            mail = data[mail_index]
            html.write(f'    <li><a href={mail}>{name}</a></li>\n')
        html.write('<ul>\n')


def total_salary(path):
    fh = open(path, 'r')
    sum = float(0)
    while True:
        line = fh.readline()
        if not line:
            break
        a = line.split(',')
        sum += int(a[1])
    fh.close()
    return sum


print(total_salary('text.txt'))


def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for i in employee_list:
        for j in i:
            fh.write(j + '\n')
    fh.close()


print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],
                              'text.txt'))

a = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
for i in a:
    for j in i:
        print(j)


def read_employees_from_file(path):
    fh = open(path, 'r')
    lst = []
    while True:
        line = fh.readline()
        if not line:
            break
        if '\n' in line:
            lst.append(line[:-1])
        else:
            lst.append(line)
    fh.close()
    return lst


print(read_employees_from_file('text.txt'))


def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write(record + '\n')
    fh.close()


print(add_employee_to_file("Drake Mikelsson, 19", 'text.txt'))


def get_cats_info(path):
    with open(path, 'r') as fh:
        a = []
        while True:
            line = fh.readline()
            if not line:
                break
            l = line.split(',')
            if '\n' in line:
                b = {'id': l[0], 'name': l[1], 'age': l[2][:-1]}
            else:
                b = {'id': l[0], 'name': l[1], 'age': l[2]}
            a.append(b)
        return a


print(get_cats_info('text.txt'))


def get_recipe(path, searfirst_symbol_id):
    with open(path, 'r') as fh:
        a = None
        while True:
            line = fh.readline()
            if not line:
                break
            l = line.split(',')
            if searfirst_symbol_id in line:
                a = {'id': l[0], 'name': l[1], 'ingredients': [l[2], l[3], l[4][:-1]]}
    return a


print(get_recipe('text.csv', '60b90c3b13067a15887e1ae4'))


def sanitize_file(source, output):
    with open(source, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            a = ''
            for i in line:
                if i.isdigit():
                    i = ''
                    a += i
                else:
                    a += i
    with open(output, 'w') as data:
        data.write(a)


print(sanitize_file('text.txt', 'text1.txt'))


def save_applicant_data(source, output):
    with open(output, 'w') as fh:
        for i in source:
            p = ''
            for j in i.values():
                p += str(j) + ','
            fh.write(p[:-1] + '\n')


numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)

s = "Привет!"

utf8 = s.encode()
print(utf8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

utf16 = s.encode('utf-16')
print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

s_from_utf16 = utf16.decode('utf-16')
print(s_from_utf16 == s)


def is_equal_string(utf8_string, utf16_string):
    utf8 = utf8_string.decode('utf-8')
    utf16 = utf16_string.decode('utf-16')
    return True if utf8.casefold() == utf16.casefold() else False


def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for k, v in users_info.items():
            f = f'{k}:{v}\n'
            h = f.encode()
            fh.write(h)


save_credentials_users('text.bin', {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'})


def get_credentials_users(path):
    with open(path, 'rb') as fh:
        a = []
        while True:
            line = fh.readline()
            if not line:
                break
            h = line.decode()
            if '\n' in h:
                a.append(h[:-1])
            else:
                a.append(h)
    return a


print(get_credentials_users('text.bin'))

import shutil


def create_backup(path, file_name, employee_residence):
    p = path + '/' + file_name
    with open(p, 'wb') as file_name:
        for k, v in employee_residence.items():
            f = (f'{k} {v}\n')
            h = f.encode()
            file_name.write(h)
    arfirst_symbolive_name = shutil.make_arfirst_symbolive('backup_folder', 'zip', 'folder')
    return arfirst_symbolive_name


import shutil


def unpack(arfirst_symbolive_path, path_to_unpack):
    p = path_to_unpack
    shutil.unpack_arfirst_symbolive(arfirst_symbolive_path, p)


import re


def find_word(text, word):
    a = re.searfirst_symbol(f'{word}', text)
    if a:
        return {
            'result': True,
            'first_index': a.span()[0],
            'last_index': a.span()[1],
            'searfirst_symbol_string': word,
            'string': text
        }
    else:
        return {
            'result': False,
            'first_index': None,
            'last_index': None,
            'searfirst_symbol_string': word,
            'string': text
        }


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, "
    "as a successor to the ABC programming language, and "
    "first released it in 1991 as Python 0.9.0.", "Python"))

import re


def find_all_words(text, word):
    a = re.findall(f'{word}', text, flags=re.IGNORECASE)
    return a


import re


def replace_spam_words(text, spam_words):
    l_1 = len(spam_words[0])
    l_2 = len(spam_words[1])
    p = re.sub(f'{spam_words[0]}', l_1 * '*', text, flags=re.IGNORECASE)
    p = re.sub(f'{spam_words[1]}', l_2 * '*', p, flags=re.IGNORECASE)
    return p


print(replace_spam_words('Guido van Rossum began working on Python ', ['began', 'Python']))

import re


def find_all_emails(text):
    result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9_.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', text)
    return result


print(find_all_emails(
    'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))

text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9_.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', text)
print(result)

import re


def find_all_phones(text):
    a = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{2}[-]\d{2}', text)
    b = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{1}[-]\d{3}', text)
    c = b + a
    return c


print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 '
                      'aloha a@test.com abc111@test.com.net '
                      '+380(67)111-777-777+380(67)777-77-787'))

import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"\w{4,5}[:]{1}[/]{2}\w+[.]\w+[.]\w+|\w{4,5}[:]{1}[/]{2}\w+[.]\w+", text)
    for matfirst_symbol in iterator:
        result.append(matfirst_symbol.group())
    return result


print(find_all_links('The main searfirst_symbol site in the world is '
                     'https://www.google.com The main social '
                     'network for people in the world is '
                     'https://www.facebook.com But programmers '
                     'have their own social network '
                     'http://github.com There they share their code. '
                     'some url to first_symboleck '
                     'https://www..facebook.com www.facebook.com '))


def cost_delivery(quantity, *_, discount=0):
    print(quantity)
    fin_sum = (5 + 2 * (quantity - 1))
    print(fin_sum)
    fin_sum = fin_sum - (fin_sum * discount)
    print(fin_sum)
    return fin_sum


cost_delivery(2, 1, 2, 3, discount=0.5)

import os
import time

for i in range(10):
    print(i)
    time.sleep(1)
    os.system('cls')

a = open('wer.txt')
# print(a.readline())
# print(a.readline())
# print(a.readline())
import shutil

from pathlib import Path
from shutil import *

Path(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\vad_dir').mkdir()
Path(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\vad_dir').rmdir()

p = Path('vad')
p.mkdir()  # создание папки
shutil.copy(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\wer.txt',  # копирование файла
            r'D:\work_it\GitHub\GoIt_sfirst_symbolool\vad')
shutil.move(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\wer.txt',  # перенос файла
            r'D:\work_it\GitHub')

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)


def alphabet_soup(txt):
    return ''.join(sorted(txt))


print(alphabet_soup("привет"))  # "веипрт"


def alphabet_soup(txt):
    a = []
    b = ''
    for i in txt:
        a.append(ord(i))
    a.sort()
    for j in a:
        b += first_symbolr(j)
    return b


print(alphabet_soup("привет"))  # "веипрт"

b = ''.join(sorted("привет"))
print(b)

import re

name = 'длтамвыдз4837е()?57432!нр99'
cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
translation = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "first_symbol", "sh", "sfirst_symbol", "", "y", "", "e", "yu", "u", "ja")

trans = {}
for c, l in zip(cyrillic, translation):
    trans[ord(c)] = l
    trans[ord(c.upper())] = l.upper()
new_name = name.translate(trans)
new_name = re.sub(r'\W', '_', new_name)
print(new_name)

fh = open(r'..\files\text.txt')
print(fh.read(12))  # read string from file
print(fh.tell())  # searfirst_symbol for cursor
fh.seek(0)  # move cursor to beginning of file
print(type(fh))  # type of file
print(fh)
print(fh.readlines())  # read lines from file
print(fh.readline())  # read line from file
fh.close()  # close file

with open(r'..\files\logo.png', 'rb') as fh:
    data = fh.read()
    # print(len(data))
    # d = data[:50]
with open(r'..\files\new_logo.png', 'wb') as file:
    file.write(data)

import shutil

print(shutil.make_arfirst_symbolive('must', 'zip',
                                    r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort'))  # pack files
shutil.unpack_arfirst_symbolive('must.zip', r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort1')  # unpack files

import shutil

shutil.rmtree(r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort1')  # delete directory
shutil.copy(r'\work_it\GitHub\GoIt_sfirst_symbolool\files\logo.png',
            r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort')  # copy files
shutil.move(r'\work_it\GitHub\GoIt_sfirst_symbolool\temp\logo.png',
            r'\work_it\GitHub\GoIt_sfirst_symbolool\files\logo.png')  # move files

import utils

print(utils.FILE_VERSION)
utils.greeting('vad')
utils.summa(5, 6)
print(__name__)
print(dir(utils))

import sys

print(sys.builtin_module_names)
print(sys.path)

from lenght_d import get_length_d

get_length_d(13)
import lenght_d

lenght_d.get_length_d(10)

import re


def is_integer(s):
    new_s = re.sub(r'\D', '', s)
    return True if new_s and len(s) >= 1 else False


print(is_integer('asd56'))


def capital_text(s):
    d = ['.', '!', '?']
    f = True
    n = ''
    for i in s:
        if i in d:
            f = False
        if not f and i.isalpha():
            n += i.capitalize()
            f = True
        else:
            n += i
    n = n[0].capitalize() + n[1:]
    return n


print(capital_text('fdbbd fgdg. dg rdg! e dfs? adax'))


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    s = ''
    if (reverse or not reverse) and start_letter not in riddle:
        return s
    elif not reverse:
        for i in riddle:
            if i == start_letter:
                s = riddle.index(i)
                q = riddle[s:s + word_length]
                return q
    elif reverse:
        for i in riddle:
            if i == start_letter:
                s = riddle.index(i) + 1
                r = s - word_length
                n = riddle[r:s]
                return n[::-1]


print(solve_riddle('aaatttrrr', 5, 'p', True))


def data_preparation(list_data):
    new = []
    for i in list_data:
        if len(i) > 2:
            i.remove(min(i))
            i.remove(max(i))
            for j in i:
                new.append(j)
        else:
            for j in i:
                new.append(j)
    new.sort()
    new.reverse()
    return new


print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))

import re


def token_parser(s):
    s = s.split(' ')
    s = ''.join(s)
    dic = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    result = []
    st = ''
    for k, i in enumerate(s):
        if i in dic and k == len(s) - 1:
            result.append(i)
        if i in dic:
            st += i
        else:
            result.append(st)
            st = ''
        if i not in dic:
            result.append(i)
    for j in result:
        if j == '':
            result.remove(j)
    return result


print(token_parser('(2+ 3) *4 - 5 * 3'))


def all_sub_lists(data):
    result = []
    array = []
    step = len(data)

    for i in range(step, -1, -1):
        for j in range(step, -1, -1):
            result = data[j:i + j + 1]
            if len(result) == i + 1:
                array.append(result)

    r = [[]] + array[::-1]
    return r


print(all_sub_lists([4, 6, 1, 3]))


def make_request(keys, values):
    if len(keys) == len(values):
        a = dict(zip(keys, values))
        return a
    else:
        return {}


print(make_request([1, 2, 3], [4, 5, 6, ]))

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]
for name, number in zip(employee_names, employee_numbers):
    print(name, number)

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]
zipped_values = zip(employee_names, employee_numbers)
print(list(zipped_values))

import re


def sequence_buttons(string):
    symbol = ('.', ',', '?', '!', ':', 'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
    button = ('1', '11', '111', '1111', '11111', '2', '22', '222',
              '3', '33', '333', '4', '44', '444', '5', '55', '555',
              '6', '66', '666', '7', '77', '777', '7777', '8', '88',
              '888', '9', '99', '999', '9999', '0')

    trans = {}
    print(list(zip(symbol, button)))
    for c, l in zip(symbol, button):
        trans[ord(c)] = l
        trans[ord(c.upper())] = l.upper()
    new_name = string.translate(trans)
    return new_name


print(sequence_buttons("Hello, World!"))


def file_operations(path, additional_info, start_pos, count_first_symbolars):
    with open(path, 'a') as f:
        f.write(additional_info)
    with open(path, 'r') as f:
        f.seek(start_pos)
        return f.read(count_first_symbolars)


def get_employees_by_profession(path, profession):
    with open(path, 'r') as f:
        new = []
        s = f.readlines()
        for i in s:
            n = i.find(profession)
            if n != -1:
                new.append(i)
        m = ''.join(new)
        w = m.replace(profession, '')
        r = w.replace('\n', '')
        return r[:-1]


print(get_employees_by_profession('text.txt', 'courier'))


def to_indexed(source_file, output_file):
    with open(source_file, 'r') as f:
        st = ''
        for i, v in enumerate(f):
            st += f'{i}: {v}'
            print(st)
    with open(output_file, 'w') as fh:
        fh.write(st)


print(to_indexed('text.txt', 'text1.txt'))
import pprint
import random
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.year)  # 2020
print(current_datetime.month)  # 10
print(current_datetime.day)  # 09
print(current_datetime.hour)  # 22
print(current_datetime.minute)  # 32
print(current_datetime.second)  # 22
print(current_datetime.microsecond)
print(current_datetime.date())
print(current_datetime.time())

seventh_day_2022 = datetime(year=2023, month=1, day=12, hour=14)
print(seventh_day_2020.weekday())

current_datetime = datetime.now()
future_month = (current_datetime.month % 12) + 1
print(future_month)


def flatten(data):
    if data == []:
        return data
    if isinstance(data[0], list):
        return (flatten(data[0]) + flatten(data[1:]))
    return (data[:1] + flatten(data[1:]))


print(flatten([1, 2, [3, 4, [5, 6]], 7]))


def decode(data):
    uncode_list = []
    a = ''
    for i in data:
        if isinstance(i, str):
            a += i
        elif isinstance(i, int):
            for _ in range(i):
                uncode_list.append(a)
            a = ''
    return uncode_list


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))


def decode(data):
    uncode_list = []
    a = []
    b = []
    for i in data:
        if isinstance(i, str):
            a.append(i)
        else:
            b.append(i)
    res = list(zip(a, b))
    return res


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))


def decode(data):
    if len(data) == 0:
        return []
    return [data[0]] * data[1] + decode(data[2:])


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

data = ["X", 3]
a = [data[0]] * data[1]  # !!!!!!!!!!
print(a)


def encode(data):
    data = ''.join(data)
    if len(data) == 0:
        return []
    a = []
    count = 1
    first_symbol = data[0]
    for cur_symbol in data[1:]:
        if cur_symbol != first_symbol:
            a.append(first_symbol)
            if count >= 1:
                a.append(count)
            return a + encode(data[count:])
        else:
            count += 1
            if len(data) == 2:
                a.append(first_symbol)
                a.append(count)
    return a


print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))


def encode(data):
    if len(data) == 0:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index += 1
    current = [data[0], index]
    return current + encode(data[index:len(data)])


print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))

from datetime import datetime


def get_days_from_today(date):
    current_datetime = datetime.now()
    y, m, d = date.split('-')
    b = datetime(year=int(y), month=int(m), day=int(d), hour=int(0), minute=int(2), second=int(00))
    a = current_datetime - b
    return a.days


print(get_days_from_today('2021-10-09'))

from datetime import date

dict_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def get_days_in_month(month, year):
    for m, d in dict_month.items():
        if year % 4 != 0:
            if month == m:
                return d
        else:
            return 29


print(get_days_in_month(2, 2001))

s = '10 January 2020'
print(datetime.strptime(s, '%d %B %Y'))

from datetime import datetime


def get_str_date(date):
    date = date[0:10]
    b = datetime.strptime(date, "%Y-%m-%d")
    print(b)
    return b.strftime("%A %d %B %Y")


print(get_str_date("2021-05-27 17:08:34.149Z"))

from random import randrange


def get_numbers_ticket(min, max, quantity):
    a = []
    for _ in range(0, quantity):
        b = random.randrange(min, max)
        if b not in a:
            a.append(b)
        else:
            b = random.randrange(min, max)
            a.append(b)
    return a


print(get_numbers_ticket(1, 52, 6))

from random import sample, randrange


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and (min < quantity < max):
        b = sample(range(min, max), k=quantity)
        b.sort()
        return b
    else:
        return []


print(get_numbers_ticket(1, 52, 6))

import random


def get_random_winners(quantity, participants):
    if quantity <= len(participants):
        keys_list = list(participants.keys())
        random.shuffle(keys_list)
        return random.sample(keys_list, k=quantity)
    else:
        return []


print(get_random_winners(2, participants={
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}))

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    a = 0
    for i in number_list:
        print(type(i))
        getcontext().prec = signs_count
        i = Decimal(i) + Decimal(0)
        a += i
    return a / len(number_list)


print(decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))

getcontext().prec = 2
print(Decimal(1) / Decimal(7))

print(convert_list({"nickname": "Mick", "age": 5, "owner": "Sara"}))

A = [{'Wednesday': 'torvalds'},
     {'Thursday': 'bardeen'},
     {'Thursday': 'bell'},
     {'Friday': 'ritchie'},
     {'Friday': 'villani'},
     {'Friday': 'curie'},
     {'Saturday': 'elbakyan'},
     {'Wednesday': 'vad'}]

new = {}

for i in A:
    for k, v in i.items():
        new.setdefault(k, []).append(v)
for k, v in new.items():
    print(f'{k}: {", ".join(v)}')

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    a = []
    for i in cats:
        if isinstance(i, tuple):
            a.append({"nickname": i.nickname, "age": i.age, "owner": i.owner})
        else:
            a.append(Cat(i["nickname"], i["age"], i["owner"]))
    return a


pprint.pprint(convert_list([
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"}
]))

pprint.pprint(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))

from collections import Counter

IP = [
    "85.157.172.253",
    "45.157.255.365",
    "24.157.865.890",
    "85.157.172.253",
    "24.157.865.890",
    "85.157.172.253",
    "85.157.172.253"
]


def get_count_visits_from_ip(ips):
    count = Counter(ips)
    return {k: v for k, v in count.items()}


def get_frequent_visit_from_ip(ips):
    count = Counter(ips).most_common(1)
    for i in count:
        return i


print(get_count_visits_from_ip(IP))
print(get_frequent_visit_from_ip(IP))

from collections import deque

MAX_LEN = 5
lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()


from collections import Counter, defaultdict

text = "There are many variations of passages of Lorem Ipsum available, " \
       "but the majority have suffered alteration in some form, " \
       "by injected humour, or randomised words which don't look even " \
       "slightly believable"


def get_chars_in_text(text):
    dict_chars = {}
    for i in text:
        num = dict_chars.get(i)
        if num:
            dict_chars[i] = num + 1
        else:
            dict_chars[i] = 1
    return dict_chars


print(get_chars_in_text(text))
counter = Counter(text)
print(counter.most_common())


def get_word_list(text):
    word_list = text.split(" ")
    word_dict = {}
    for i in word_list:
        word = word_dict.get(i[0])
        if word:
            word.append(i)
        else:
            word_dict[i[0]] = [i]
    return word_dict


print(get_word_list(text))


def get_word_list(text):
    word_list = text.split(" ")
    word_dict = defaultdict(list)
    for i in word_list:
        word_dict[i[0]] = i
    return word_dict


print(get_word_list(text))

from collections import deque


def main():
    d = deque(maxlen=5)
    for i in range(10):
        d.appendleft(i)
    print(d)
    start = d.popleft()
    end = d.pop()
    print(start, end)


main()

TODO
really
important
code

from collections import deque


def main():
    user_inputs = deque(maxlen=20)
    while True:
        user_input = input('>>>>>: ')
        user_inputs.append(user_input)
        if user_input == 'exit':
            break
    print('good bye')
    print(f'steps: {user_inputs}')


main()


def get_numbers(x):


    num = []
for i in range(x):
    n = i ** 2
    if not n % 2:
        num.append(n)
print(num)
get_numbers(12)


def get_numbers(x):
    print([i ** 2 for i in range(x) if not i % 2])


get_numbers(12)

a = 'vad 0965678667'
print(a.split(' '))


def add_contact(contact: str) -> str:


    dict_contact = {}
while True:
    contact = input('>>>>>').split(' ')
    print(len(dict_contact))
    dict_contact[contact[0]] = contact[1]

    print(dict_contact)
print(add_contact(input('>>>>>')))

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if "discount" in customer.keys():
        result_price = price * (1 - customer["discount"])
        return result_price
    else:
        finally_price = price * (1 - DEFAULT_DISCOUNT)
        return finally_price


print(get_discount_price_customer(10, {"name": "Boris", "discount": 0.15}))


def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n not in cache:
            if n == 0:
                result = 0
            elif n == 1:
                result = 1
            else:
                result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result
        return cache[n]

    return fibonacci


def discount_price(discount):
    return A[discount]


def cost_25(price):
    return price * (1 - 0.25)


def cost_20(price):
    return price * (1 - 0.20)


def cost_15(price):
    return price * (1 - 0.15)


def cost_10(price):
    return price * (1 - 0.10)


def cost_05(price):
    return price * (1 - 0.05)


def cost_0(price):
    return price


A = {
    0.25: cost_25,
    0.20: cost_20,
    0.15: cost_15,
    0.10: cost_10,
    0.05: cost_05,
    0: cost_0
}
price = 100

cost_25 = discount_price(0.25)
cost_20 = discount_price(0.20)
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)
cost_0 = discount_price(0)

print(cost_15(price))
print(cost_10(price))
print(cost_05(price))


def format_phone_number(func):
    def inner(*args):
        result = func(*args)
        if len(result) == 10:
            return '+38' + result
        elif len(result) == 12:
            return '+' + result

    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number("38050-111-22-22"))


def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


a = interval_generator(5, 7)
print(next(a))
print(next(a))
print(next(a))

import re


def generator_numbers(string):
    for i in re.findall(r'\d+', string):
        yield i


def sum_profit(string):
    result = 0
    for i in generator_numbers(string):
        result += int(i)
    print(result)
    return result


def normal_name(list_name):
    a = []
    for i in map(lambda x: x.capitalize(), list_name):
        a.append(i)
    return a


def get_emails(list_contacts):
    mail_list = []
    for i in map(lambda x: x["email"], list_contacts):
        mail_list.append(i)
    return mail_list


def positive_values(list_payment):
    result = [i for i in filter(lambda x: x >= 0, list_payment)]
    print(result)
    return result


some_str = 'aaAbbB C F DDd EEe'
for i in filter(lambda x: x.islower(), some_str):
    print(i)


def get_favorites(contacts):
    a = [i for i in filter(lambda x: x["favorite"] is True, contacts)]
    return a


from functools import reduce


def sum_numbers(numbers):
    result = reduce((lambda x, y: x + y), numbers)
    return resul


from functools import reduce


def amount_payment(payment):
    result = [i for i in payment if i > 0]
    a = reduce((lambda x, y: x + y), result)
    return a


def calculator(number1, operator, number2):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '/':
        if number2 == 0:
            return "Нельзя делить на 0!"
        else:
            return number1 / number2
    elif operator == '*':
        return number1 * number2


def calculator(number1, operator, number2):
    try:
        return eval(str(number1) + operator + str(number2))
    except ZeroDivisionError:
        return "Нельзя делить на 0!"


print(calculator(2, '/', 0))


class Person:
    l = []

    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies
        self.l.append(self.name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_hobbies(self):
        return self.hobbies


vad = Person('vad', 40, 'it')
nik = Person('nik', 13, 'it')
print(vad.name)
print(Person.l)
print(nik.name, nik.age)

from datetime import datetime


class Animals:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_birthday_year(self) -> int:
        return datetime.now().year - self.age

    def make_sound(self):
        pass

    def eat(self):
        print('Eating')


class Dog(Animals):

    def get_birthday_year(self) -> int:
        return datetime.now().year - self.age

    def make_sound(self):
        print('woof')

    def jamp(self):
        print('jamp')

    def play(self):
        print('play with animation')


class Cat(Animals):
    def __init__(self, name: str, age: int, color: int):
        super().__init__(name, age)
        self.color = color

    def get_birthday_year(self) -> int:
        return datetime.now().year - self.age

    def make_sound(self):
        print('meow')


class Bird(Animals):

    def get_birthday_year(self) -> int:
        return datetime.now().year - self.age

    def make_sound(self):
        print('chirp')


dog = Dog('rex', 5)
cat = Cat('gil', 8, 'red')
bird = Bird('rich', 3)

print(cat.color)


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self, owner):
        return self.owner


owner = Owner('vad', 34, 'vvvvvvvvv')
dog = Dog('rex', 4, 'drgdrg', owner)
print(dog.who_is_owner(owner))


class Character:
    hp = 100
    mp = 100

    def __init__(self, name, x, y):
        self.left_hand = None
        self.right_hand = None
        self.name = name
        self.x = x
        self.y = y

    def pick_weapon(self, weapon):
        if self.left_hand is None:
            self.left_hand = weapon
        elif self.right_hand is None:
            self.right_hand = weapon
        else:
            print('full weapon')

    def show_weapon(self):
        return self.left_hand, self.right_hand

    def moving(self, name):
        print('im moving')

    def identify(self):
        print(self.name)

    def die(self):
        return self.left_hand, self.right_hand

    def damage_left(self):
        self.left_hand.kick_ass()

    def damage_right(self):
        self.right_hand.kick_ass()


class Weapon:
    def __init__(self):
        self.damage = 10

    def kick_ass(self):
        return self.damage


class Knife(Weapon):
    def __init__(self):
        self.damage = 5

    def thow(self):
        return self.damage - 2

    def kick_ass(self):
        print('chick')
        return self.damage


class Sword(Weapon):
    def __init__(self):
        self.damage = 15

    def kick_ass(self):
        print('bik')
        return self.damage


class Axe(Weapon):
    def __init__(self):
        self.damage = 20

    def kick_ass(self):
        print('trick')
        return self.damage


class Gun(Weapon):
    def __init__(self):
        self.damage = 20

    def kick_ass(self):
        print('Baam')
        return self.damage


char1 = Character('vad', 0, 0)
char2 = Character('nik', 0, 0)
knife = Knife()
sword = Sword()
print(knife.kick_ass())
print(sword.kick_ass())
char1.pick_weapon(knife)
char1.pick_weapon(sword)
print(char1.left_hand)
print(char1.damage_left())
print(char1.damage_right())
left_hand, right_hand = char1.die()


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"


def is_subset(list1, list2):
    return True if set(list1) <= set(list2) else False


print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))  # ➞ True


class Record:
    def __init__(self, name):
        self.name = name


class Name:
    value = 'vad'


record = Record(Name())
print(record.name.value)

from collections import UserDict


class ValueSearchableDict(UserDict):
    def has_in_values(self):
        return self.data


as_dict = ValueSearchableDict()
as_dict['a'] = 1
print(as_dict.has_in_values())  # True
print(as_dict.has_in_values(2))  # False

from collections import UserList


class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
countable.sum()  # 15

from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys


TODO: проверка
на
ввод
числа


def input_number():
    while True:
        try:
            num = input("Enter integer number: ")
            return int(num)
        except Exception:
            print(f'"{num}" is not a number. Try again')


num = input_number()
print(num)

TODO: проверка
на
ввод
имени
с
большой
буквы
не
менее
3
символа
import string


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('Name is too short, need more than 3 symbols. Try again.')
    except NameStartsFromLowError:
        print('Name should start from capital letter. Try again.')

l = [int(input(f'Enter number {i + 1} >: ')) for i in range(5)]
print(l)


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for i in self.list_contacts():
            if i['id'] == id:
                return i
        return None


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for i in self.contacts:
            if i['id'] == id:
                self.contacts.remove(i)


contact = Contacts()
contact.add_contacts('vad', '34534', 'fs@43', True)
contact.add_contacts('ret', '67u435', 'ewr@4ewr', True)
contact.add_contacts('435', 'fbcb', 'egnwr@hjmr', True)
contact.add_contacts('rfgbt', '6,', 'ewr@4ewr', True)
print(contact.list_contacts())
print(contact.get_contact_by_id(1))
print(contact.get_contact_by_id(2))
print(contact.get_contact_by_id(3))
print(contact.get_contact_by_id(4))
contact.remove_contacts(2)
print(contact.list_contacts())

user_input = input('>Enter_command: ')
a = user_input.split(' ')
print(a)

a = {'q': ['1', '2']}
for i in a.items():
    print(i)


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y


vector = Vector(Point(1, 10))
print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10
print(vector.coordinates)  # 10
vector[0] = 16  # Устанавливаем координату x вектора в 10
print(vector[0])  # 10
print(vector[1])  # 10


def decor(func):
    def wrapper(x, y):
        try:
            func(x, y)
        except ValueError:
            return print('Error')

    return wrapper


@decor
def main(x, y):
    return x / y


print(main(12, 0))


class Person:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


person = Person('123')
print(person.name)  # None


def get_input():
    a = input('dsg: ')
    return a


def a():
    print('a')


def b():
    print('b')


dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs
dispatch[get_input()]()

import csv

with open('eg56s.csv', 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
with open('egg45s.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))

import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as fh:
        c = {'contacts': [contacts] for i in contacts}
        json.dump(c, fh)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = list(json.load(fh))
    return unpacked


print(write_contacts_to_file('qq54.json', {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False}))


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello i am {self.name} and {self.age} years old'


bill = Human('bill', 12)
print(bill)


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x


@property
def y(self):
    return self.__y


@y.setter
def y(self, y):
    if (type(y) == int) or (type(y) == float):
        self.__y = y


def __str__(self):
    return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        vector = vector2 + vector1
        return vector


def __sub__(self, vector):
    return


def __str__(self):
    return f"Vector({self.coordinates.x},{self.coordinates.y})"


vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)


class A:
    def __str__(self):
        return f"{a}"


a = A()
print(a)

a = [{"name": "John", "age": 35, "city": ["San Francisco"]},
     {"name": "Zoe", "age": 34, "city": ["Los Angeles"]}]

for i in a:
    for j in i:
        b = j.replace("'", '"')
        print(b)
from collections import UserDict


class Iterable(UserDict):
    def __init__(self):
        super().__init__()
        self.current_value = self.data
        self.data = {"1": "1", "2": "3", 4: 5, 6: 7, 8: 9}

    def __next__(self):
        if self.current_value < len(self.data):
            self.current_value += 1
            return self.current_value
        raise StopIteration

    def __iter__(self):
        return self


c = Iterable()
for i in c:
    print(i)

Функции - генераторы
Функция
iter()


class Phone:
    def __init__(self, p):
        self.__private_phone = None
        self.p = p

    @property
    def p(self):
        return self.__private_phone

    @p.setter
    def p(self, value: str):
        if value.isdigit():
            self.__private_phone = value
        else:
            raise ValueError('Invalid value')


p = Phone(input('enter:   '))
print(p.p)

import re

match = re.fullmatch(r'[+][3][8][0]\d{9}', '+380965678667')
res = True if match else False
print(res)

alist = ['Python', 'Java', 'C', 'C++', 'CSharp']


def list_items():
    count = 0
    a = []
    for item in alist:
        a.append(item)
        count += 1
        if count == 2:
            yield a
            list_items()


print(next(list_items()))
print(next(list_items()))
a = {"vad": ["+380(96)567-86-67", "06.08.1982"], "vika": ["+380(96)266-50-09", "09.07.1984"],
     "nik": ["+380(99)987-85-96", "15.03.2010"], "ret": ["+380(96)266-50-09", "09.07.1984"],
     "hjk": ["+380(96)266-50-09", "09.07.1984"], "rgf": ["+380(96)266-50-09", "09.07.1984"],
     "kjl": ["+380(96)266-50-09", "09.07.1984"], "iiu": ["+380(96)266-50-09", "09.07.1984"]}


def test():
    while True:
        count = 0
        for k, v in a.items():
            print(k, v)
            count += 1
            if count == 3:
                yield


print(next(test()))
print(next(test()))
print(next(test()))


class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__class__.__name__


cat = Cat('vasia')
print(cat)


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)


p = Point(1, 2, 4, 5, 6, 7, 8, 9)
print(len(p))

import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as fh:
        c['contacts'] = [contacts]
        json.dump(c, fh)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = list(json.load(fh))
    return unpacked


print(write_contacts_to_file('filename.txt', {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}))

from random import randrange

from random import randrange


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        for _ in range(max_vectors):
            self.vectors.append(Vector(Point(randrange(0, max_points), randrange(0, max_points))))

    def __next__(self):
        try:
            result = self.vectors[self.current_index]
            self.current_index += 1
            return result
        except IndexError:
            raise StopIteration


class RandomVectors:
    def __init__(self, max_vectors, max_points):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


vectors = RandomVectors(5, 10)
for vector in vectors:
    print(vector)

import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ["name", "email", "phone", "favorite"]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for i in contacts:
            writer.writerow({'name': i['name'], 'email': i['email'], 'phone': i['phone'], 'favorite': i['favorite']})


def read_contacts_from_file(filename):
    with open(filename, newline='') as fh:
        reader = csv.DictReader(fh)
        a = []
        for row in reader:
            a.append(
                {'name': row['name'], 'email': row['email'], 'phone': row['phone'], 'favorite': bool(row['favorite'])})
        return a


write_contacts_to_file()
read_contacts_from_file()


def decorator(func):
    def inner():
        try:
            func()
        except Exception as e:
            print(f"Error {e}")

    return inner


@decorator
def my_func():
    while True:
        a = int(input("Enter int: "))
        if a:
            print('ok')
        else:
            raise Exception


my_func()
x = int(input("Enter x: "))

f = lambda x, y: x + y
print(f(4, 4))

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        self.contacts = contacts
        if self.contacts is None:
            self.contacts = []

    def save_to_file(self):
        with open(self.filename, "wb", ) as fh:
            pickle.dump(persons, fh)

    def read_from_file(self):
        with open(self.filename, "rb") as fh:
            unpacked = pickle.load(fh)
        return unpacked


class Char:
    def move(self):
        print("Move")

    def speed(self):
        print("Speed")


class Enemy(Char):
    pass


enemy = Enemy()
enemy.move()


class A:
    a = 5


class B(A):
    b = 9


class C:
    a = 100


class D(B, C):
    b = 1


asd = D()
print(asd.a)


def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


print(total(10, 1, 2, 3, extra_number=50))


def printMax(x, y):
    """Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами."""
    x = int(x)  # конвертируем в целые, если возможно
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


printMax(3, 5)
print(printMax.__doc__)

# pagination
a = ['1', '2', '3', '4', '5', '6', '7', '8']


def func():
    count = 0
    temp = []
    for i in a:
        count += 1
        temp.append(i)
        if count == 3:
            yield temp
            count = 0
            temp = []
            print(input("enter"))
    else:
        yield temp


def generat(func):
    for i in func:
        print(i)


generat(func())

from collections import UserDict


class Char(UserDict):
    def __init__(self, name):
        super().__init__()
        self.__name = name


self.data = {'1': ['1!', 4], '2': ['2!', 5], '3': '3!'}


def __getitem__(self, key):
    return self.data[key]


def __setitem__(self, key, value):
    self.data[key] = value


def __call__(self, a, b):
    print(f'calling {a}{b}')


def __enter__(self):
    print('context')
    return self


def __exit__(self, exc_type, exc_value, trace):
    if not exc_type is None:
        print('ok')
    else:
        print('error')
        print('{} {} {}'.format(exc_type, exc_value, trace))


char = Char('vad')
char['2'] = 'vad'
print(char['2'])
print(char('vad', 'vika'))
with Char('vad') as file:
    print(file)


class Char:
    def __init__(self, name):
        self.__name = name


@property
def name(self):
    return self.__name


@name.setter
def name(self, new_value):
    self.__name += '_' + new_value


c = Char('vad')
print(c.name)


class Char:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def __add__(self, other):
        return self.hp + other.hp


c = Char('vad')
c_1 = Char('vd')
print(c + c_1)

print(dir(int))

a = 5
print(id(a))
b = a
print(id(a))
print(id(b))
a = 3
print(id(a))
print(id(b))
import csv

with open('Monefy.Data.04.03.2023.csv', encoding="utf-8") as fh:
    reader = csv.DictReader(fh)
    for i in reader:
        print(i)


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b


rect = Rectangle(5, 6)
print(rect.area)

from datetime import datetime, timedelta, date


def __get_current_week():
    now = datetime.now()
    current_weekday = now.weekday()
    if current_weekday < 5:
        week_start = now - timedelta(days=2 + current_weekday)
    else:
        week_start = now - timedelta(days=current_weekday - 5)
    return [week_start.date(), week_start.date() + timedelta(days=7)]


def congratulate():
    data = {'name': 'vad', 'birthday': '25.03.1984'}
    result = []
    WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # current_year = datetime.now().year
    congratulate = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': []}
    # print(data)
    # for key in data:
    if data['birthday']:
        birthday = data['birthday']
        birth_day = datetime.strptime(birthday, '%d.%m.%Y')
        birth_day = date(birth_day.year, birth_day.month, birth_day.day)
        current_date = date.today()
        new_birthday = birth_day.replace(year=current_date.year)
        birthday_weekday = new_birthday.weekday()
        if __get_current_week()[0] <= new_birthday < __get_current_week()[1]:
            if birthday_weekday < 5:
                congratulate[WEEKDAYS[birthday_weekday]].append(data['name'])
            else:
                congratulate['monday'].append(data['name'])
    for k, v in congratulate.items():
        if len(v):
            result.append(f"{k}: {' '.join(v)}")
    return '_' * 50 + '\n' + '\n'.join(result) + '\n' + '_' * 50


print(congratulate())

import os
import re
from pathlib import Path

dir_suff_dict = {"Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
                 "Documents": [".md", ".epub", ".txt", ".docx", ".doc", ".ods", ".odt", ".dotx", ".docm", ".dox",
                               ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".xml"],
                 "Archives": [".iso", ".tar", ".gz", ".7z", ".dmg", ".rar", ".zip"],
                 "Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"],
                 "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mpg", ".mpeg", ".3gp"],
                 "PDF": [".pdf"],
                 "HTML": [".html", ".htm", ".xhtml"],
                 "EXE_MSI": [".exe", ".msi"],
                 "PYTHON": [".py", ".pyw"]}


def normalize(name: str) -> str:
    CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja")

    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name


def sort_func(path_dir):
    cur_dir = Path(path_dir)
    dir_path = []

    for root, dirs, files in os.walk(path_dir):
        for d in dirs:
            dir_path.append(os.path.join(root, d))
        for file in files:
            p_file = Path(root) / file
            name_normalize = f"{normalize(p_file.name[0:-len(p_file.suffix)])}{p_file.suffix}"
            p_file.rename(Path(root) / name_normalize)
            p_file = Path(root) / name_normalize
            for suff in dir_suff_dict:
                if p_file.suffix.lower() in dir_suff_dict[suff]:
                    dir_img = cur_dir / suff
                    dir_img.mkdir(exist_ok=True)
                    try:
                        p_file.rename(dir_img.joinpath(p_file.name))
                    except FileExistsError:
                        p_file.rename(dir_img.joinpath(f'{p_file.name.split(".")[0]}_c{p_file.suffix}'))
                        print(f"Возможно дубликат: {p_file.name}")

    for dir_p in reversed(dir_path):
        if os.path.split(dir_p)[1] in dir_suff_dict or os.stat(dir_p).st_size != 0:
            continue
        else:
            os.rmdir(dir_p)


if __name__ == "__main__":
    path_d = input('[+] Введите путь к директории для сортировки: ')
    if not Path(path_d).exists():
        print('[-] Директории не существует')
    else:
        sort_func(path_d)
    print('[!] Сортировка завершена')

from datetime import datetime

dict_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def get_days_in_month(month: datetime, year: datetime) -> int:
    """The function takes the month and date from the datetime
    format and rotates the number of days in this month and in
    rotation, including leap years"""

    for m, d in dict_month.items():
        if year % 4 != 0:
            if month == m:
                return d
        else:
            return 29


def get_current_day() -> str:
    """Returns the current day and month"""

    today = datetime.now()
    current_day_month = f'{today.day}.{today.month}'
    return current_day_month


def get_days_next_week() -> list:
    """The function returns a list of 7 days following the current date today"""

    list_days_next_week = []
    today = datetime.now()
    day = datetime.now().day
    days_in_month = get_days_in_month(datetime.now().month, datetime.now().year)

    if days_in_month == 28 and day > 21:
        count = 0
        for i in range(0, 7):
            i += 1
            if day < 28:
                day += 1
                date_datetime = f'{datetime.now().year}, {datetime.now().month}, {day}'
                app = datetime.strptime(date_datetime, "%d, %m, %Y")
                list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})
            else:
                while len(list_days_next_week) < 7:
                    count += 1
                    date_datetime = f'{datetime.now().year}, {datetime.now().month + 1}, {count}'
                    app = datetime.strptime(date_datetime, "%Y, %m, %d")
                    list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})

        return list_days_next_week

    elif days_in_month == 29 and day > 22:
        count = 0
        for i in range(0, 7):
            i += 1
            if day < 29:
                day += 1
                date_datetime = f'{datetime.now().year}, {datetime.now().month}, {day}'
                app = datetime.strptime(date_datetime, "%Y, %m, %d")
                list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})
            else:
                while len(list_days_next_week) < 7:
                    count += 1
                    date_datetime = f'{datetime.now().year}, {datetime.now().month + 1}, {count}'
                    app = datetime.strptime(date_datetime, "%Y, %m, %d")
                    list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})

        return list_days_next_week

    elif days_in_month == 30 and day > 23:
        count = 0
        for i in range(0, 7):
            i += 1
            if day < 30:
                day += 1
                date_datetime = f'{datetime.now().year}, {datetime.now().month}, {day}'
                app = datetime.strptime(date_datetime, "%Y, %m, %d")
                list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})
            else:
                while len(list_days_next_week) < 7:
                    count += 1
                    date_datetime = f'{datetime.now().year}, {datetime.now().month + 1}, {count}'
                    app = datetime.strptime(date_datetime, "%Y, %m, %d")
                    list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})

        return list_days_next_week

    elif days_in_month == 31 and day > 24:
        count = 0
        for i in range(0, 7):
            i += 1
            if day < 31:
                day += 1
                date_datetime = f'{datetime.now().year}, {datetime.now().month}, {day}'
                # print(date_datetime)
                app = datetime.strptime(date_datetime, "%Y, %m, %d")
                # print(app)
                list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})
                # print(list_days_next_week)

            else:
                while len(list_days_next_week) < 7:
                    count += 1
                    date_datetime = f'0{count}.0{datetime.now().month + 1}.{datetime.now().year}'
                    # print(date_datetime)
                    # app = datetime.strptime(date_datetime, r"%d, %m, %Y")
                    # print(app)
                    list_days_next_week.append({app.strftime("%A"): f'{date_datetime}'})
        # print(list_days_next_week)

        return list_days_next_week

    else:
        for _ in range(0, 7):
            day += 1
            date_datetime = f'{datetime.now().year}, {datetime.now().month}, {day}'
            app = datetime.strptime(date_datetime, "%Y, %m, %d")
            list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})

        return list_days_next_week


def concatenation_of_key_values(result: list) -> list:
    """The function combines the values of the same keys in the dictionary"""

    new = {}

    for i in result:
        for k, v in i.items():
            new.setdefault(k, []).append(v)
    for k, v in new.items():
        if k == 'Saturday':
            print(f'Monday(Saturday): {", ".join(v)}')
        elif k == 'Sunday':
            print(f'Monday(Sunday): {", ".join(v)}')
        else:
            print(f'{k}: {", ".join(v)}')


def get_birthdays_on_week(users: list) -> list:
    """The function generates a list according to the dates of birthdays and the current date"""

    list_days_next_week = get_days_next_week()
    result = []

    for day in list_days_next_week:
        for i in day:
            for elem in users:
                if elem['birthday'] == day[i]:
                    result.append({i: elem['name']})

    return result


if __name__ == '__main__':
    random_birthday = [
        {'name': 'vad', 'birthday': '2023-03-31'},
        {'name': 'nik', 'birthday': '2023-04-02'},
        {'name': 'vika', 'birthday': '2023-04-04'}
    ]
    concatenation_of_key_values(get_birthdays_on_week(random_birthday))
    print("\nHappy birthday coworkers!!!")

import logging

logging.info('Hello')

from threading import Thread, RLock
from time import sleep

lock = RLock()


def run_tr(lock, n):
    lock.acquire()
    print(f'start{n}')
    sleep(1)
    lock.release()
    print(f'finish {n}')


if __name__ == '__main__':
    threads = []
    thread1 = Thread(target=run_tr, args=(lock, 1))
    thread2 = Thread(target=run_tr, args=(lock, 2))
    thread1.start()
    thread2.start()

from threading import Thread, RLock, Semaphore
from time import sleep


def run_tr(n, pool):
    with pool:
        print(f'start{n}')
        sleep(1)
        print(f'finish {n}')


if __name__ == '__main__':
    pool = Semaphore(3)
    for i in range(10):
        thread1 = Thread(target=run_tr, args=(i, pool))
        thread1.start()
    print('game over')

from threading import Thread, RLock, Semaphore, Condition
from time import sleep


def main(condition):
    with condition:
        print('start main')
        sleep(2)
        condition.notify_all()


def worker(condition):
    with condition:
        condition.wait()
        print('start work')


if __name__ == '__main__':
    condition = Condition()
    main = Thread(target=main, args=(condition,))
    worker = Thread(target=worker, args=(condition,))
    worker.start()
    main.start()
    print('game over')

s = '1234567789'
print(s[1:6:1])

from jinja2 import Template

name = 'vad'
age = 29
tm = Template("my name is {{name}} and my age is {{age}}")
msg = tm.render(name=name, age=age)
print(msg)

persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

rows_tmp = Template("""{% for person in persons -%}
    {{ person.name }} {{ person.age }}
{% endfor %}""")

print(rows_tmp.render(persons=persons))

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from time import sleep


class Test(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello vad")

    def do_POST(self):
        pass


server = HTTPServer(('127.0.0.1', 8000), Test)
server_thread = threading.Thread(target=server.serve_forever())
server_thread.start()
sleep(1)

from http import client

c = client.HTTPConnection('localhost', 8000)
c.request('GET', '/')
res = c.getresponse()
print(res.status, res.reason)
data = res.read()
print(data)
httpd.shutdown()

from datetime import datetime

d = datetime.now()

print(d)

import threading
import socket
import pickle

data_response = {'2023-04-20, 10:14:10': {'username': 'vad', 'message': '1'}}


def send_response():
    host = '127.0.0.1'
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((host, port))
    sock.send(bytes(f"{data_response.keys()}", encoding='UTF-8'))
    sock.close()


def run_socket():
    host = '127.0.0.1'
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    try:
        while True:
            data = sock.recv(1024)
            with open('example_socket_server_client/data.json', 'ab') as f:
                pickle.dump(data, f)
            if not data:
                break
    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


if __name__ == '__main__':
    send_response()
    run_socket()
    server = threading.Thread(target=send_response, )
    client = threading.Thread(target=run_socket, )
    server.start()
    server.join()
    client.start()
    client.join()


def my_sort(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] == arr[-1]:
            break
        if arr[i] > arr[-1]:
            temp.insert(0, arr[i])
        else:
            temp.insert(-1, arr[i])

    return temp


a = [5, 8, 4, 7, 4, 1, 3, 9]
print(my_sort(a))
print(sorted(a))

import asyncio


async def baz():
    print("Preparation")
    await asyncio.sleep(3)
    return True


async def main():
    result = baz()
    print(result)
    result = await result
    return result


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)

from time import sleep, time
from faker import Faker

fake = Faker()


def get_user_sync(uid: int) -> dict:
    sleep(1)
    return {"id": uid, "name": fake.name(), "email": fake.email()}


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(1)
    return {"id": uid, "name": fake.name(), "email": fake.email()}


async def main():
    r = await asyncio.gather(get_user_async(1),
                             get_user_async(2),
                             get_user_async(3))
    return r


if __name__ == "__main__":
    start = time()
    r = asyncio.run(main())
    print(r)
    print(time() - start)
    print("_______________________")
    start = time()
    u4 = get_user_sync(4)
    u5 = get_user_sync(5)
    u6 = get_user_sync(6)
    print(u4, u5, u6)
    print(time() - start)

import aiohttp
import asyncio
from time import time
import platform

data = ["13.04.2023", "15.04.2023", "21.04.2023", "22.04.2023", "23.04.2023", "24.04.2023"]


async def get_exchange_rate():
    async with aiohttp.ClientSession() as session:
        for date in data:
            async with session.get(f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}") as response:
                response_json = await response.json()
                return response_json


async def main():
    a = []
    exchange_rate = await get_exchange_rate()
    for currency in exchange_rate:
        a.append(currency)
    return a
    print(f"{currency['ccy']} to UAH: buy-{currency['buy']}, sale-{currency['sale']}")


if __name__ == "__main__":
    st = time()
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print(asyncio.run(main()))
    print(time() - st)

from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(3)
    return message


pool = ThreadPoolExecutor(3)

future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
sleep(3)
print(future.done())
print(future.result())

import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()

from time import time
import asyncio
import aiohttp
import platform
from pprint import pprint

data = ["13.04.2023", "15.04.2023", "21.04.2023",
        "22.04.2023", "23.04.2023", "24.04.2023"]


async def async_gather_http_get():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for date in data:
            tasks.append(
                asyncio.create_task(session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')))
        responses = await asyncio.gather(*tasks)
        return [await r.json() for r in responses]


if __name__ == '__main__':
    st = time()
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    pprint(asyncio.run(async_gather_http_get()))

    print(time() - st)

import aiohttp
import asyncio


async def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    timeout = aiohttp.ClientTimeout(total=0.5)
    async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
        try:
            async with session.get('http://httpbin.org/get') as response:
                print(response.status, response.headers)
                body = await response.text()
                print(body)

                if response.status >= 300:
                    print("HTTP error")
        except TimeoutError as error:
            print("timeout")


if __name__ == '__main__':
    asyncio.run(main())

