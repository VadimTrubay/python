# КОД ЦЕЗАРЯ
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
        encoded_message = encoded_message + new_character
    elif i.islower():
        c_unicode = ord(i)
        c_index = ord(i) - ord("a")
        new_index = (c_index + offset) % 26
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        encoded_message = encoded_message + new_character
    elif i.isspace():
        encoded_message = encoded_message + " "
    elif i == "!":
        encoded_message = encoded_message + "!"
print(encoded_message)

# calculate
result = None
operand = None
operator = None
wait_for_number = True

while True:
    if operator == '=':
        print(f"Result: {result}")
        break
    elif wait_for_number == True:
        while True:
            try:
                operand = float(input("Enter number: "))
            except ValueError:
                print("Oops! It is not a number. Try again.")
            else:
                if result == None:
                    result = operand
                else:
                    if operator == '+':
                        result = result + operand
                    elif operator == '-':
                        result = result - operand
                    elif operator == '*':
                        result = result * operand
                    elif operator == '/':
                        result = result / operand
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

# get fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci((7)))

# calculate_distance(coordinates)
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
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

from random import randint
def get_random_password():
    string = ''
    for i in range(8):
        random_num = randint(40, 126)
        symbol = chr(random_num)
        string += symbol
    return string

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

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)
    return files, folders

import sys
def parse_args():
    result = sys.argv[1:]
    result = ' '.join(result)
    return result

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

def sanitize_phone_number(phone):
    a = '1, 2, 3, 4, 5, 6, 7, 8, 9, 0'
    new_phone = ''
    for i in phone:
        if not i in a:
            continue
        else:
            new_phone += i
    return ''.join(new_phone.split())

def is_check_name(fullname, first_name):
    return True if fullname.startswith(first_name) else False

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
        print(b)
        if b.startswith('81'):
            return_phones['JP'].append(b)
            continue
        if b.startswith('65'):
            return_phones['SG'].append(b)
            continue
        if b.startswith('886'):
            return_phones['TW'].append(b)
            continue
        if b.startswith('380'):
            return_phones['UA'].append(b)
            continue
        else:
            return_phones['UA'].append(b)
    return return_phones

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

import re
def find_word(text, word):
    a = re.search(f'{word}', text)
    if a:
        return {
            'result': True,
            'first_index': a.span()[0],
            'last_index': a.span()[1],
            'search_string': word,
            'string': text
        }
    else:
        return {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }

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

import re
def find_all_emails(text):
    result = re.findall(r'[a-zA-Z]{1}[a-zA-Z0-9_.]+[@][a-zA-Z]+[.][a-zA-Z]{2,}', text)
    return result

import re
def find_all_phones(text):
    a = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{2}[-]\d{2}', text)
    b = re.findall(r'[+]\d{3}[(]\d{2}[)]\d{3}[-]\d{1}[-]\d{3}', text)
    c = b + a
    return c

a = ['\n', '\f', '\r', '\t', '\v']
def real_len(text):
    string = ''
    for i in text:
        if i in a:
            continue
        string += i

    return len(string)

import re
def find_all_links(text):
    result = []
    iterator = re.finditer(r"\w{4,5}[:]{1}[/]{2}\w+[.]\w+[.]\w+|\w{4,5}[:]{1}[/]{2}\w+[.]\w+", text)
    for match in iterator:
        result.append(match.group())
    return result

def total_salary(path):
    fh = open(path, 'r')
    sum = float(0)
    while True:
        line = fh.readline()
        if not line:
            break
        a = line.split(',')
        s = a[1]
        sum += int(s)
    fh.close()
    return sum

