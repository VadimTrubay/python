# def is_palindrome(word):
#     return True if word[::-1] == word else False
# print(is_palindrome("abba"))

# a = {'F': 'Unsatisfactorily',
#      'FX': 'Unsatisfactorily',
#      'E': ['Enough', 'Unsatisfactorily'],
#      'D': 'Satisfactorily',
#      'C': 'Good',
#      'B': 'Very good',
#      'A': 'Perfectly',
# 'discount': 50
# }
# print(a.get('discount', False))
# print(a['E'][1])
# for i in a:
#      print(a[i])

# students = [
#     {
#         'name': 'Petr',
#         'mark': {
#             '19.09': {
#                 'value': 80,
#                 'description': '...'
#             },
#             '29.09': {
#                 'value': 100,
#                 'description': None
#             },
#             '05.10': {
#                 'value': 99,
#                 'description': '...'
#             }
#         },
#         'email': 'petr@gmail.com',
#         'visits': [True, False, True, True],
#     },
#     {
#         'name': 'Vasya',
#         'mark': {
#             '19.09': {
#                 'value': 100,
#                 'description': '...'
#             },
#             '29.09': {
#                 'value': 100,
#                 'description': None
#             },
#             '05.10': {
#                 'value': 99,
#                 'description': '...'
#             }
#         },
#         'email': 'vasya@gmail.com',
#         'visits': [True, True, True, True],
#     },
# ]
#
# for name in students:
#     print(name['name'])

# def volume_of_box(sizes):
#     a = sizes.values()
#     result = 1
#     for i in a:
#         result = result * i
#         print(i)
#     return result

# def volume_of_box(sizes):
#     w, l, h = sizes.values()
#     return w * l * h
# print(volume_of_box({ "ширина": 2, "длина": 5, "высота": 1 }))

# from counter_char import *
#
# text = 'Lorem ipsum dolor sit amet ' \
#        'consectetur adipiscing elit ' \
#        'sed do eiusmod'
# counter_char(text)
#
# from char_set import *
#
# text = 'Quis autem vel eum iure reprehenderit, ' \
#        'qui in ea \\ voluptate velit esse, ' \
#        'quam nihil molestiae! consequatur, ' \
#        'vel illum, qui dolorem eum fugiat, ' \
#        'quo voluptas nulla pariatur? 33 ' \
#        'At vero eos et accusamus et'
# char_set(text)
#
# from cast_split import *
#
# text = 'Lorem ipsum, dolor sit amet ' \
#        'consectetur adipiscing elit ' \
#        'sed do eiusmod!!!'
# cast_split(text)

# которая принимает список (целые числа), находит среднее значение
# балла в списке и делит его на два списка. В первый попадают значения
# меньше среднего, включая среднее значение, а во второй — строго
# больше среднего. Функция возвращает кортеж этих двух списков.
# Для пустого списка возвращаем два пустых списка.
# def split_list(grade):
#     low = []
#     high = []
#     result = (low, high)
#     try:
#         average_value = sum(grade) / len(grade)
#     except ZeroDivisionError:
#         return result
#     average_value = round(average_value)
#     print(average_value)
#     for i in grade:
#         if i <= average_value:
#             low.append(i)
#         else:
#             high.append(i)
#         result = (low, high)
#     return low, high
# print(split_list([1, 7, 3, 4, 5, 6, 8, 2, 9, 12]))


# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9
# }
# def calculate_distance(coordinates):
#     result = 0
#     while len(coordinates) > 1:
#         a, b = coordinates[0], coordinates[1]
#         c = (a, b)
#         del coordinates[0]
#         for key, val in points.items():
#             if c[0] > c[1]:
#                 c = (b, a)
#             elif c == key:
#                 result += val
#     return result
# print(calculate_distance([0, 1, 3, 2, 0]))

# user_1 = {"name": "Jane", "age": 21}
# user_2 = {"name": "Moris", "age": 23}
# user_3 = {"name": "Steve", "age": 24}
#
# persons = [user_1, user_2, user_3]
#
# for user in persons:
#     for field in user:
#         print(user.get(field))

# def game(terra, power):
#     for i in terra:
#         for j in i:
#             if power >= j:
#                 power += j
#             else:
#                 break
#     return power
# print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))

# Убедитесь в том, что среди этих пин-кодов в списке
# не будет дубликатов, все они хранятся в виде строк,
# их длина равна 4 символам и содержат они только цифры
# def is_valid_pin_codes(pin_codes):
#     if len(pin_codes) < 1:
#         return False
#     for i in pin_codes:
#         if not type(i) == str:
#             return False
#         if len(i) != 4:
#             return False
#         if not i.isnumeric():
#             return False
#         if pin_codes.count(i) > 1:
#             return False
#     else:
#         return True
# print(is_valid_pin_codes(['0090', '9034', '0000']))

# from random import randint
#
# def get_random_password():
#     string = ''
#     for i in range(8):
#         random_num = randint(40, 126)
#         symbol = chr(random_num)
#         string += symbol
#     return string
# print(get_random_password())
#
# def is_valid_password(password):
#     u = 0
#     l = 0
#     dig = 0
#     for i in password:
#         if i.isdigit():
#             dig += 1
#         elif i.isupper():
#             u += 1
#         elif i.islower():
#             l += 1
#     if len(password) == 8 and u != 0 and l != 0 and dig != 0:
#         return True
#     else:
#         return False
# # print(is_valid_password('cSfg5yhd'))
#
# from random import randint


# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result
#
#
# def is_valid_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# def get_password():
#     i = 0
#     while i <= 100:
#         password = get_random_password()
#         print(password)
#         if is_valid_password(password):
#             return password
#         else:
#             continue
#
# print(get_password())
# from pathlib import Path
# print(Path())
# my_path = Path('D:\\work_it\\Github\\GoIt_school\\temp_2.py')
# my_path = Path('D:\work_it\Github')
# my_path = my_path.parent
# my_path = my_path.name
# my_path = my_path.suffix
# my_path = my_path.exists()
# my_path = my_path.is_dir()
# my_path = my_path.is_file()
# my_path = my_path.iterdir()
# for i in my_path.iterdir():
#     if not i.is_file():
#         print(i)
# print(my_path)

# import sys
# print(sys.argv)

# from pathlib import Path
# import pprint
#
# def parse_folder(path):
#     files = []
#     folders = []
#     p = Path()
#     for i in p.iterdir():
#         if i.is_dir():
#             folders.append(i.name)
#         else:
#             files.append(i.name)
#     return f'files = {files}', f'folders = {folders}'
#
# pprint.pprint(parse_folder('D:\work_it\Github\GoIt_school'))

# import sys
# def parse_args():
#     result = sys.argv[1:]
#     ' '.join(result)
#     return result
# print(parse_args())

# import sys
# print(sys.argv)

# import re
#
# s = "I am 3456 years old"
# age = re.search('\d+', s)
# print(age.group())

# a = ['\n', '\f', '\r', '\t', '\v']
#
# def real_len(text):
#     string = ''
#     for i in text:
#         if i in a:
#             continue
#         string += i
#
#     return len(string)
#
# print(real_len('Alex\nKdfe23\t\f\v.\r'))

# width = 5
# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))

# jingle_bells = "Jingle bells, jingle bells\nJingle all the way\rOh, what fun it is to ride\v In a one horse open sleigh"
# print(jingle_bells)

# import re
# text = 'I bought 7 nuts for 6$ and 10 bolts for 3$.'
# a = re.search('\d+', text)
# print(a.group())
#
# b = re.findall('\d+', text)
# print(b)

# с = re.('\b\w{3}\b', text)
# print(с)

# match = re.findall(r'\d\d\D\d\d\D\d\d', r'Телефон 23-12-12')
# print(match)

# 096-567-86-67
# inp = input('enter tel: +38')
# pattern = re.search('^\(0?\d{2}\)?\d{3}-?\d{2}-?\d{2}$', inp)
# # print(pattern)
# try:
#     if inp == pattern.group():
#         print('OK! access allowed')
#     else:
#         print('STOP! access denied')
# except AttributeError:
#     print('STOP! access denied')

# inp = input('enter email: ')
# pattern = re.search('^\w+[@]\w+[.]\w{2,3}$', inp)
# # print(pattern)
# try:
#     if inp == pattern.group():
#         print('OK! access allowed')
#     else:
#         print('STOP! access denied')
# except AttributeError:
#     print('STOP! access denied')

# log = 'fdgdgr145.34.56.67fdhfg34.34.56.67fdxn211.35.768.78ghn'
# logs = 'POSTgdgr145.34.56.67fdhfg7fdxngrggdmalware.comhn'
# 0.0.0.0
# 255.255.255.255

# ip_address = re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', log)
# print(ip_address)
# ip_addres = re.findall('^POST\w*\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\w*malware.com\w*', logs)
# print(ip_addres)
# print(re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', ip_addres[0]))

# logs = '10.01.2023 10:18.43 fddgdgdfgv' \
#        '10.01.2023 11:18.43 fddgdgdfgv' \
#        '10.01.2023 12:18.43 fddgdgdfgv' \
#        '10.01.2023 13:18.43 fddgdgdfgv' \
#        '10.01.2023 14:18.43 fddgdgdfgv'
# print(re.findall('\d{2}\.\d{2}.\d{2,4}\s1[10-12]', logs))

# log = 'first_name: fdggfr, last_name: sfvdv, adress: feferg, tel: 437666574'
# user_input = input('fild name: ')
# result = re.findall(f'{user_input}:\s\w+\s?', log)
# print(result)

# user_pattern = '\d{10}'
# string = '123443567890'
# def findall(pattern, string):
#     patterns = {'\d':lambda x: x.isdigit()}
#     for key in patterns:
#         if pattern.startswith(key):
#             pattern_key = key
#             n_times = int(pattern[pattern.find('{') + 1:pattern.find('}')])
#     result_string = ''
#     for char in string:
#         if patterns[pattern_key](char):
#             result_string += char
#         else:
#             result_string = ''
#         if len(result_string) == n_times:
#             return result_string
#
# print(findall(user_pattern, string))

# from re import fullmatch
#
# LOGIN_RE = '[a-zA-Z0-9._]{3,10}'
# PWD_RE = '[a-zA-Z0-9._!@#$%&]{8,15}'
# user_db = {}
#
#
# def check_input(reg_exp, user):
#     if not fullmatch(reg_exp, user):
#         raise ValueError(f'Input must be {reg_exp}')
#     return True
#
#
# def check_if_login_exist(login):
#     global user_db
#     return False if login in user_db else True
#
#
# def register():
#     global user_db, user_pwd, user_login
#     login_check_result = False
#     psw_check_result = False
#
#     while True:
#         if not login_check_result:
#             user_login = input('New login>: ')
#             login_check_result = check_if_login_exist(user_login)
#             continue
#         try:
#             login_check_result = check_input(LOGIN_RE, user_login)
#         except ValueError as error:
#             print(error)
#
#         if not psw_check_result:
#             user_pwd = input('New password>: ')
#         try:
#             pwd_check_result = check_input(PWD_RE, user_pwd)
#         except ValueError as error:
#             print(error)
#         return user_login, user_pwd
#
#
# def login():
#     global user_db
#
#     user_login = input('login>: ')
#     user_pwd = input('password>: ')
#     try:
#         return True if user_db[user_login]['pwd'] == user_pwd else False
#     except KeyError:
#         return False
#
#
# while True:
#     action = input('register or login(r or l)?: ')
#     if action == 'r':
#         user_login, user_pwd = register()
#         user_db[user_login] = {'psw': user_pwd}
#         print(user_db)
#     elif action == 'l':
#         if login():
#             print('Welcome')
#         else:
#             print('Try again ...')

# TODO поиск расширения файла
# files = ['video.avi', 'audio.mp3', 'document.html', 'folder', 'backup.tar.gz']
# for file in files:
#     try:
#         index = file.rindex('.')
#         sufix = file[index+1:]
#         print(f'File: ({file}), sufix: ({sufix})')
#     except ValueError:
#         print(f'File: ({file}), sufix: (not found)')

# import re
# text = 'first sentence, second sentence. ' \
#        'third sentence! fourth sentence?'
# sentences = re.split('[\.\,\!\?]', text)
# print(sentences)


# text = 'first sentence\n second sentence\n ' \
#        'third sentence'
# print(text)
# sentences = text.split('\n')
# new_text = '*'.join(sentences)
# print(sentences)
# print(new_text)

# import pprint
# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]
#
# def find_articles(key, letter_case=False):
#     new_dict = []
#     for i in articles_dict:
#         for k, v in i.items():
#             if type(v) == str:
#                 r = v.split(' ')
#                 for j in r:
#                     if key.lower() in j.lower() and letter_case is False:
#                         new_dict.append(i)
#                         break
#                     if key in j and letter_case is True:
#                         new_dict.append(i)
#                         break
#     return new_dict
#
# pprint.pprint(find_articles('stark', letter_case=False))


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
#
#
# def get_phone_numbers_for_countries(list_phones):
#     return_phones = {
#         'UA': [],
#         'JP': [],
#         'TW': [],
#         'SG': []
#     }
#     for i in list_phones:
#         b = sanitize_phone_number(i)
#         if b.startswith('81'):
#             return_phones['JP'].append(b)
#             continue
#         elif b.startswith('65'):
#             return_phones['SG'].append(b)
#             continue
#         elif b.startswith('886'):
#             return_phones['TW'].append(b)
#             continue
#         elif b.startswith('380'):
#             return_phones['UA'].append(b)
#             continue
#         else:
#             return_phones['UA'].append(b)
#     return return_phones
#
# print(get_phone_numbers_for_countries(['065-875-94-11', '(81)8765347', '8867658976', '657658976', '(65)765-89-77']))
#{'UA': ['0658759411'], 'JP': ['818765347'], 'TW': ['8867658976'], 'SG': ['657658976', '657658977']}

# def is_spam_words(text, spam_words, space_around=False):
#     if space_around is True:
#         for i in text.lower().split():
#             for j in spam_words:
#                 if j + '.' == i:
#                     return True
#         return False
#
#     if space_around is False:
#         for i in text.lower().split():
#             for j in spam_words:
#                 if j in i:
#                     return True
#         return False
#
# print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))  # True))

# spam_words = ['ло.']  # j
# text = 'Мо ло. х'  # i
# space_around = True


# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
# TRANS = {}
#
# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()
#
# def translate(name):
#     new_char = name.translate(TRANS)
#     return new_char
#
# print(translate('Вадим Валентиович'))


# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
# def formatted_grades(students):
#     a = 0
#     d = []
#     for k, v in students.items():
#         a += 1
#         for key, val in grades.items():
#             if v == key:
#                 d.append("{:>4}|{:<10}|{:^5}|{:^5}".format(a, k, v, val))
#     return d
# for el in formatted_grades(students):
#     print(el)

# def formatted_numbers():
#     a = ["|{0:^10}|{1:^10}|{2:^10}|".format('decimal', 'hex', 'binary')]
#     for i in range(16):
#         s = "|{0:<10d}|{0:^10x}|{0:>10b}|".format(i)
#         a.append(s)
#     return a
#
# for el in formatted_numbers():
#     print(el)
#
# for i in range(16):
#     s = "|{0:<10d}|{0:^10x}|{0:>10b}|".format(i)
#     print(s)

# def free_shipping(order):
#     sum = 0
#     for i in order.values():
#         sum += i
#         if sum > 50:
#             return True
#     return False
#
# print(free_shipping({ "Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99 }))


# def get_extension(lst):
#     a = []
#     for i in lst:
#         b = i.find('.')
#         a.append(i[b+1:])
#     return a
# print(get_extension(["проект1.jpg", "проект1.pdf", "проект1.mp3"]))