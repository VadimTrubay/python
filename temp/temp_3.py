from pprint import pprint
# from pathlib import *
# import pprint
# p = Path("temp/").mkdir(parents=True, exist_ok=True)
# help(open)
# file = open('temp_1.py', 'r', encoding='UTF8')
# for line in file:
#     print(line)

# while True:
# data = file.read(1024)  # read first_symbolang
# data = file.readline()
# print(data)
# if not data:
#     break

# res = file.read(1)
# res = file.readline()
# pprint.pprint(res)

# file.close()
# print(file.name)
# print(file.closed)

# meneger context
# with open('temp_1.py', 'a', encoding='UTF8') as file:
#     print(file.readline()[-1])
# NAME = 'Last name'
# MAIL = 'Login email'
# with open('email.csv', 'r') as file:
#     with open('email.html', 'a') as html:
#         html.write('<ul>\n')
#         headers = []
#         for line in file:
#             data = line.split(',')
#             data[-1] = data[-1][:-1]
#             if not headers:
#                 headers = data
#                 mail_index = headers.index(MAIL)
#                 name_index = headers.index(NAME)
#                 continue
#             name = data[name_index]
#             mail = data[mail_index]
#             html.write(f'    <li><a href={mail}>{name}</a></li>\n')
#         html.write('<ul>\n')

# def total_salary(path):
#     fh = open(path, 'r')
#     sum = float(0)
#     while True:
#         line = fh.readline()
#         if not line:
#             break
#         a = line.split(',')
#         sum += int(a[1])
#     fh.close()
#     return sum
# print(total_salary('text.txt'))

# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     for i in employee_list:
#         for j in i:
#             fh.write(j + '\n')
#     fh.close()
# print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],
#                               'text.txt'))

# a = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# for i in a:
#     for j in i:
#         print(j)

# def read_employees_from_file(path):
#     fh = open(path, 'r')
#     lst = []
#     while True:
#         line = fh.readline()
#         if not line:
#             break
#         if '\n' in line:
#             lst.append(line[:-1])
#         else:
#             lst.append(line)
#     fh.close()
#     return lst
# print(read_employees_from_file('text.txt'))

# def add_employee_to_file(record, path):
#     fh = open(path, 'a')
#     fh.write(record + '\n')
#     fh.close()
# print(add_employee_to_file("Drake Mikelsson, 19", 'text.txt'))

# def get_cats_info(path):
#     with open(path, 'r') as fh:
#         a = []
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             l = line.split(',')
#             if '\n' in line:
#                 b = {'id': l[0], 'name': l[1], 'age': l[2][:-1]}
#             else:
#                 b = {'id': l[0], 'name': l[1], 'age': l[2]}
#             a.append(b)
#         return a
#
# print(get_cats_info('text.txt'))


# def get_recipe(path, searfirst_symbol_id):
#     with open(path, 'r') as fh:
#         a = None
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             l = line.split(',')
#             if searfirst_symbol_id in line:
#                 a = {'id': l[0], 'name': l[1], 'ingredients': [l[2], l[3], l[4][:-1]]}
#     return a
# print(get_recipe('text.csv', '60b90c3b13067a15887e1ae4'))


# def sanitize_file(source, output):
#     with open(source, 'r') as fh:
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             a = ''
#             for i in line:
#                 if i.isdigit():
#                     i = ''
#                     a += i
#                 else:
#                     a += i
#     with open(output, 'w') as data:
#         data.write(a)
# print(sanitize_file('text.txt', 'text1.txt'))

# def save_applicant_data(source, output):
#     with open(output, 'w') as fh:
#         for i in source:
#             p = ''
#             for j in i.values():
#                 p += str(j) + ','
#             fh.write(p[:-1] + '\n')

# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)

# s = "Привет!"
#
# utf8 = s.encode()
# print(utf8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'
#
# utf16 = s.encode('utf-16')
# print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'
#
# s_from_utf16 = utf16.decode('utf-16')
# print(s_from_utf16 == s)

# def is_equal_string(utf8_string, utf16_string):
#     utf8 = utf8_string.decode('utf-8')
#     utf16 = utf16_string.decode('utf-16')
#     return True if utf8.casefold() == utf16.casefold() else False

# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as fh:
#         for k, v in users_info.items():
#             f = f'{k}:{v}\n'
#             h = f.encode()
#             fh.write(h)
# save_credentials_users('text.bin',  {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'})

# def get_credentials_users(path):
#     with open(path, 'rb') as fh:
#         a = []
#         while True:
#             line = fh.readline()
#             if not line:
#                 break
#             h = line.decode()
#             if '\n' in h:
#                 a.append(h[:-1])
#             else:
#                 a.append(h)
#     return a
# print(get_credentials_users('text.bin'))

# import shutil
# def create_backup(path, file_name, employee_residence):
#     p = path + '/' + file_name
#     with open(p, 'wb') as file_name:
#         for k, v in employee_residence.items():
#             f = (f'{k} {v}\n')
#             h = f.encode()
#             file_name.write(h)
#     arfirst_symbolive_name = shutil.make_arfirst_symbolive('backup_folder', 'zip', 'folder' )
#     return arfirst_symbolive_name

# import shutil
#
# def unpack(arfirst_symbolive_path, path_to_unpack):
#     p = path_to_unpack
#     shutil.unpack_arfirst_symbolive(arfirst_symbolive_path, p)

# import re
# def find_word(text, word):
#     a = re.searfirst_symbol(f'{word}', text)
#     if a:
#         return {
#             'result': True,
#             'first_index': a.span()[0],
#             'last_index': a.span()[1],
#             'searfirst_symbol_string': word,
#             'string': text
#         }
#     else:
#         return {
#             'result': False,
#             'first_index': None,
#             'last_index': None,
#             'searfirst_symbol_string': word,
#             'string': text
#         }
#
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, "
#     "as a successor to the ABC programming language, and "
#     "first released it in 1991 as Python 0.9.0.", "Python"))

# import re
# def find_all_words(text, word):
#     a = re.findall(f'{word}', text, flags=re.IGNORECASE)
#     return a

# import re
# def replace_spam_words(text, spam_words):
#     l_1 = len(spam_words[0])
#     l_2 = len(spam_words[1])
#     p = re.sub(f'{spam_words[0]}', l_1 * '*', text, flags=re.IGNORECASE)
#     p = re.sub(f'{spam_words[1]}', l_2 * '*', p, flags=re.IGNORECASE)
#     return p
#
# print(replace_spam_words('Guido van Rossum began working on Python ', ['began', 'Python']))

# import re
# def find_all_emails(text):
#     result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9_.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', text)
#     return result
# print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))

# text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
# result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9_.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', text)
# print(result)


# import re
# def find_all_phones(text):
#     a = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{2}[-]\d{2}', text)
#     b = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{1}[-]\d{3}', text)
#     c = b + a
#     return c
# print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 '
#                       'aloha a@test.com abc111@test.com.net '
#                       '+380(67)111-777-777+380(67)777-77-787'))

# import re
# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r"\w{4,5}[:]{1}[/]{2}\w+[.]\w+[.]\w+|\w{4,5}[:]{1}[/]{2}\w+[.]\w+", text)
#     for matfirst_symbol in iterator:
#         result.append(matfirst_symbol.group())
#     return result
# print(find_all_links('The main searfirst_symbol site in the world is '
#                      'https://www.google.com The main social '
#                      'network for people in the world is '
#                      'https://www.facebook.com But programmers '
#                      'have their own social network '
#                      'http://github.com There they share their code. '
#                      'some url to first_symboleck '
#                      'https://www..facebook.com www.facebook.com '))

# def cost_delivery(quantity, *_, discount=0):
#     print(quantity)
#     fin_sum = (5 + 2 *(quantity - 1))
#     print(fin_sum)
#     fin_sum = fin_sum - (fin_sum * discount)
#     print(fin_sum)
#     return fin_sum
# cost_delivery(2, 1, 2, 3, discount=0.5)

# import os
# import time
#
# for i in range(10):
#     print(i)
#     time.sleep(1)
#     os.system('cls')

# a = open('wer.txt')
# # print(a.readline())
# # print(a.readline())
# # print(a.readline())
# import shutil
#
# from pathlib import Path
# from shutil import *
# Path(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\vad_dir').mkdir()
# Path(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\vad_dir').rmdir()

# p = Path('vad')
# p.mkdir()  # создание папки
# shutil.copy(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\wer.txt',  # копирование файла
#          r'D:\work_it\GitHub\GoIt_sfirst_symbolool\vad')
# shutil.move(r'D:\work_it\GitHub\GoIt_sfirst_symbolool\wer.txt',  # перенос файла
#          r'D:\work_it\GitHub')


# src = 'path/to/file.txt'
# dst = 'path/to/dest_dir'
# shutil.copy(src, dst)

# def alphabet_soup(txt):
#     return ''.join(sorted(txt))
# print(alphabet_soup("привет")) # "веипрт"
#
# def alphabet_soup(txt):
#     a = []
#     b = ''
#     for i in txt:
#         a.append(ord(i))
#     a.sort()
#     for j in a:
#         b += first_symbolr(j)
#     return b
# print(alphabet_soup("привет")) # "веипрт"

# b = ''.join(sorted("привет"))
# print(b)

# import re
# name = 'длтамвыдз4837е()?57432!нр99'
# cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# translation = (
#     "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#     "f", "h", "ts", "first_symbol", "sh", "sfirst_symbol", "", "y", "", "e", "yu", "u", "ja")
#
# trans = {}
# for c, l in zip(cyrillic, translation):
#     trans[ord(c)] = l
#     trans[ord(c.upper())] = l.upper()
# new_name = name.translate(trans)
# new_name = re.sub(r'\W', '_', new_name)
# print(new_name)

# fh = open(r'..\files\text.txt')
# print(fh.read(12))  # read string from file
# print(fh.tell())  # searfirst_symbol for cursor
# fh.seek(0)  # move cursor to beginning of file
# print(type(fh))  # type of file
# print(fh)
# print(fh.readlines())  # read lines from file
# print(fh.readline())  # read line from file
# fh.close()  # close file

# with open(r'..\files\logo.png', 'rb') as fh:
#     data = fh.read()
#     # print(len(data))
#     # d = data[:50]
# with open(r'..\files\new_logo.png', 'wb') as file:
#     file.write(data)

# import shutil
# print(shutil.make_arfirst_symbolive('must', 'zip', r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort'))  # pack files
# shutil.unpack_arfirst_symbolive('must.zip', r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort1')  # unpack files

# import shutil
# shutil.rmtree(r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort1')  # delete directory
# shutil.copy(r'\work_it\GitHub\GoIt_sfirst_symbolool\files\logo.png', r'\work_it\GitHub\GoIt_sfirst_symbolool\files\must_sort')  # copy files
# shutil.move(r'\work_it\GitHub\GoIt_sfirst_symbolool\temp\logo.png', r'\work_it\GitHub\GoIt_sfirst_symbolool\files\logo.png')  # move files


# import utils
# print(utils.FILE_VERSION)
# utils.greeting('vad')
# utils.summa(5, 6)
# print(__name__)
# print(dir(utils))

# import  sys
# print(sys.builtin_module_names)
# print(sys.path)

# from lenght_d import get_length_d
# get_length_d(13)
# import lenght_d
# lenght_d.get_length_d(10)


# import re
# def is_integer(s):
#     new_s = re.sub(r'\D', '', s)
#     return True if new_s and len(s) >= 1 else False
#
# print(is_integer('asd56'))

# def capital_text(s):
#     d = ['.', '!', '?']
#     f = True
#     n = ''
#     for i in s:
#         if i in d:
#             f = False
#         if not f and i.isalpha():
#             n += i.capitalize()
#             f = True
#         else:
#             n += i
#     n = n[0].capitalize() + n[1:]
#     return n
# print(capital_text('fdbbd fgdg. dg rdg! e dfs? adax'))

# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     s = ''
#     if (reverse or not reverse) and start_letter not in riddle:
#         return s
#     elif not reverse:
#         for i in riddle:
#             if i == start_letter:
#                 s = riddle.index(i)
#                 q = riddle[s:s+word_length]
#                 return q
#     elif reverse:
#         for i in riddle:
#             if i == start_letter:
#                 s = riddle.index(i)+1
#                 r = s - word_length
#                 n = riddle[r:s]
#                 return n[::-1]
# print(solve_riddle('aaatttrrr', 5, 'p', True))

# def data_preparation(list_data):
#     new = []
#     for i in list_data:
#         if len(i) > 2:
#             i.remove(min(i))
#             i.remove(max(i))
#             for j in i:
#                 new.append(j)
#         else:
#             for j in i:
#                 new.append(j)
#     new.sort()
#     new.reverse()
#     return new
# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))


# import re
# def token_parser(s):
#     s = s.split(' ')
#     s = ''.join(s)
#     dic = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     result = []
#     st = ''
#     for k, i in enumerate(s):
#         if i in dic and k == len(s) - 1:
#             result.append(i)
#         if i in dic:
#             st += i
#         else:
#             result.append(st)
#             st = ''
#         if i not in dic:
#             result.append(i)
#     for j in result:
#         if j == '':
#             result.remove(j)
#     return result
# print(token_parser('(2+ 3) *4 - 5 * 3' ))

# def all_sub_lists(data):
#     result = []
#     array = []
#     step = len(data)
#
#     for i in range(step, -1, -1):
#         for j in range(step, -1, -1):
#             result = data[j:i + j + 1]
#             if len(result) == i + 1:
#                 array.append(result)
#
#     r = [[]] + array[::-1]
#     return r
#
# print(all_sub_lists([4, 6, 1, 3]))

# def make_request(keys, values):
#     if len(keys) == len(values):
#         a = dict(zip(keys, values))
#         return a
#     else:
#         return {}
# print(make_request([1, 2, 3], [4, 5, 6, ]))

# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
# for name, number in zip(employee_names, employee_numbers):
# 	print(name, number)
#
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
# zipped_values = zip(employee_names, employee_numbers)
# print(list(zipped_values))

# import re
# def sequence_buttons(string):
#     symbol = ('.', ',', '?', '!', ':', 'a', 'b', 'c', 'd', 'e', 'f',
#               'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
#               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
#     button = ('1', '11', '111', '1111', '11111', '2', '22', '222',
#               '3', '33', '333', '4', '44', '444', '5', '55', '555',
#               '6', '66', '666', '7', '77', '777', '7777', '8', '88',
#               '888', '9', '99', '999', '9999', '0')
#
#     trans = {}
#     print(list(zip(symbol, button)))
#     for c, l in zip(symbol, button):
#         trans[ord(c)] = l
#         trans[ord(c.upper())] = l.upper()
#     new_name = string.translate(trans)
#     return new_name
# print(sequence_buttons("Hello, World!"))

# def file_operations(path, additional_info, start_pos, count_first_symbolars):
#     with open(path, 'a') as f:
#         f.write(additional_info)
#     with open(path, 'r') as f:
#         f.seek(start_pos)
#         return f.read(count_first_symbolars)

# def get_employees_by_profession(path, profession):
#     with open(path, 'r') as f:
#         new = []
#         s = f.readlines()
#         for i in s:
#             n = i.find(profession)
#             if n != -1:
#                 new.append(i)
#         m = ''.join(new)
#         w = m.replace(profession, '')
#         r = w.replace('\n', '')
#         return r[:-1]
#
# print(get_employees_by_profession('text.txt', 'courier'))

# def to_indexed(source_file, output_file):
#     with open(source_file, 'r') as f:
#         st = ''
#         for i, v in enumerate(f):
#             st += f'{i}: {v}'
#             print(st)
#     with open(output_file, 'w') as fh:
#         fh.write(st)
# print(to_indexed('text.txt', 'text1.txt'))
# import pprint
# import random
# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.year)        # 2020
# print(current_datetime.month)       # 10
# print(current_datetime.day)         # 09
# print(current_datetime.hour)        # 22
# print(current_datetime.minute)      # 32
# print(current_datetime.second)      # 22
# print(current_datetime.microsecond)
# print(current_datetime.date())
# print(current_datetime.time())

# seventh_day_2022 = datetime(year=2023, month=1, day=12, hour=14)
# print(seventh_day_2020.weekday())

# current_datetime = datetime.now()
# future_month = (current_datetime.month % 12) + 1
# print(future_month)

# def flatten(data):
#     if data == []:
#         return data
#     if isinstance(data[0], list):
#         return (flatten(data[0]) + flatten(data[1:]))
#     return (data[:1] + flatten(data[1:]))
#
# print(flatten([1, 2, [3, 4, [5, 6]], 7]))

# def decode(data):
#     uncode_list = []
#     a = ''
#     for i in data:
#         if isinstance(i, str):
#             a += i
#         elif isinstance(i, int):
#             for _ in range(i):
#                 uncode_list.append(a)
#             a = ''
#     return uncode_list
# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))
#
# def decode(data):
#     uncode_list = []
#     a = []
#     b = []
#     for i in data:
#         if isinstance(i, str):
#             a.append(i)
#         else:
#             b.append(i)
#     res = list(zip(a, b))
#     return res
# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

# def decode(data):
#     if len(data) == 0:
#         return []
#     return [data[0]] * data[1] + decode(data[2:])
# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

# data = ["X", 3]
# a = [data[0]] * data[1]  # !!!!!!!!!!
# print(a)

# def encode(data):
#     data = ''.join(data)
#     if len(data) == 0:
#         return []
#     a = []
#     count = 1
#     first_symbol = data[0]
#     for cur_symbol in data[1:]:
#         if cur_symbol != first_symbol:
#             a.append(first_symbol)
#             if count >= 1:
#                 a.append(count)
#             return a + encode(data[count:])
#         else:
#             count += 1
#             if len(data) == 2:
#                 a.append(first_symbol)
#                 a.append(count)
#     return a
# print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))

# def encode(data):
#     if len(data) == 0:
#         return []
#     index = 1
#     while index < len(data) and data[index] == data[index - 1]:
#         index += 1
#     current = [data[0], index]
#     return current + encode(data[index:len(data)])
# print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))

# from datetime import datetime
# def get_days_from_today(date):
#     current_datetime = datetime.now()
#     y, m, d = date.split('-')
#     b = datetime(year=int(y), month=int(m), day=int(d), hour=int(0), minute=int(2), second=int(00))
#     a = current_datetime - b
#     return a.days
# print(get_days_from_today('2021-10-09' ))

# from datetime import date
# dict_month = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }
#
# def get_days_in_month(month, year):
#     for m, d in dict_month.items():
#         if year % 4 != 0:
#             if month == m:
#                 return d
#         else:
#             return 29
# print(get_days_in_month(2, 2001))

# s = '10 January 2020'
# print(datetime.strptime(s, '%d %B %Y'))

# from datetime import datetime
# def get_str_date(date):
#     date = date[0:10]
#     b = datetime.strptime(date, "%Y-%m-%d")
#     print(b)
#     return b.strftime("%A %d %B %Y")
# print(get_str_date("2021-05-27 17:08:34.149Z"))

# from random import randrange
# def get_numbers_ticket(min, max, quantity):
#     a = []
#     for _ in range(0, quantity):
#         b = random.randrange(min, max)
#         if b not in a:
#             a.append(b)
#         else:
#             b = random.randrange(min, max)
#             a.append(b)
#     return a
# print(get_numbers_ticket(1, 52, 6))

# from random import sample, randrange
# def get_numbers_ticket(min, max, quantity):
#     if min >= 1 and max <= 1000 and (min < quantity < max):
#         b = sample(range(min, max), k=quantity)
#         b.sort()
#         return b
#     else:
#         return []
# print(get_numbers_ticket(1, 52, 6))

# import random
# def get_random_winners(quantity, participants):
#     if quantity <= len(participants):
#         keys_list = list(participants.keys())
#         random.shuffle(keys_list)
#         return random.sample(keys_list, k=quantity)
#     else:
#         return []
#
# print(get_random_winners(2, participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }))

# from decimal import Decimal, getcontext
# def decimal_average(number_list, signs_count):
#     a = 0
#     for i in number_list:
#         print(type(i))
#         getcontext().prec = signs_count
#         i = Decimal(i) + Decimal(0)
#         a += i
#     return a / len(number_list)
#
# print(decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))

# getcontext().prec = 2
# print(Decimal(1) / Decimal(7))

# print(convert_list({"nickname": "Mick", "age": 5, "owner": "Sara"}))

# A = [{'Wednesday': 'torvalds'},
#      {'Thursday': 'bardeen'},
#      {'Thursday': 'bell'},
#      {'Friday': 'ritchie'},
#      {'Friday': 'villani'},
#      {'Friday': 'curie'},
#      {'Saturday': 'elbakyan'},
#      {'Wednesday': 'vad'}]
#
# new = {}
#
# for i in A:
#     for k, v in i.items():
#         new.setdefault(k, []).append(v)
# for k, v in new.items():
#     print(f'{k}: {", ".join(v)}')


# import collections
#
# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
#
# def convert_list(cats):
#     a = []
#     for i in cats:
#         if isinstance(i, tuple):
#             a.append({"nickname": i.nickname, "age": i.age, "owner": i.owner})
#         else:
#             a.append(Cat(i["nickname"], i["age"], i["owner"]))
#     return a
#
#
# pprint.pprint(convert_list([
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"}
# ]))

# pprint.pprint(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))


# from collections import Counter
# IP = [
#     "85.157.172.253",
#     "45.157.255.365",
#     "24.157.865.890",
#     "85.157.172.253",
#     "24.157.865.890",
#     "85.157.172.253",
#     "85.157.172.253"
# ]
#
# def get_count_visits_from_ip(ips):
#     count = Counter(ips)
#     return {k: v for k, v in count.items()}
#
# def get_frequent_visit_from_ip(ips):
#
#     count = Counter(ips).most_common(1)
#     for i in count:
#         return i
# print(get_count_visits_from_ip(IP))
# print(get_frequent_visit_from_ip(IP))

# from collections import deque
#
# MAX_LEN = 5
# lifo = deque(maxlen=MAX_LEN)
#
# def push(element):
#     lifo.appendleft(element)
#
#
# def pop():
#     return lifo.popleft()

