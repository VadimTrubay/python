# from collections import UserDict
# class Char(UserDict):
#     def __init__(self, name):
#         super().__init__()
#         self.__name = name

# self.data = {'1': ['1!', 4], '2': ['2!', 5], '3': '3!'}

# def __getitem__(self, key):
#     return self.data[key]
#
# def __setitem__(self, key, value):
#     self.data[key] = value
#
# def __call__(self, a, b):
#     print(f'calling {a}{b}')

# def __enter__(self):
#     print('context')
#     return self

# def __exit__(self, exc_type, exc_value, trace):
#     if not exc_type is  None:
#         print('ok')
#     else:
#         print('error')
#         print('{} {} {}'.format(exc_type, exc_value, trace))


# char = Char('vad')
# char['2'] = 'vad'
# print(char['2'])
# print(char('vad', 'vika'))
# with Char('vad') as file:
#     print(file)

# class Char:
#     def __init__(self, name):
#         self.__name = name

# @property
# def name(self):
#     return self.__name
#
# @name.setter
# def name(self, new_value):
#     self.__name += '_' + new_value

# c = Char('vad')
# print(c.name)

# class Char:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
#
#     def __add__(self, other):
#         return self.hp + other.hp
#
# c = Char('vad')
# c_1 = Char('vd')
# print(c + c_1)

# print(dir(int))

# a = 5
# print(id(a))
# b = a
# print(id(a))
# print(id(b))
# a = 3
# print(id(a))
# print(id(b))
# import csv
#
# with open('Monefy.Data.04.03.2023.csv', encoding="utf-8") as fh:
#     reader = csv.DictReader(fh)
#     for i in reader:
#         print(i)

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
# rect = Rectangle(5, 6)
# print(rect.area)

# from datetime import datetime, timedelta, date
#
# def __get_current_week():
#     now = datetime.now()
#     current_weekday = now.weekday()
#     if current_weekday < 5:
#         week_start = now - timedelta(days=2 + current_weekday)
#     else:
#         week_start = now - timedelta(days=current_weekday - 5)
#     return [week_start.date(), week_start.date() + timedelta(days=7)]
#
#
# def congratulate():
#     data = {'name': 'vad', 'birthday': '25.03.1984'}
#     result = []
#     WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#     # current_year = datetime.now().year
#     congratulate = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': []}
#     # print(data)
#     # for key in data:
#     if data['birthday']:
#         birthday = data['birthday']
#         birth_day = datetime.strptime(birthday, '%d.%m.%Y')
#         birth_day = date(birth_day.year, birth_day.month, birth_day.day)
#         current_date = date.today()
#         new_birthday = birth_day.replace(year=current_date.year)
#         birthday_weekday = new_birthday.weekday()
#         if __get_current_week()[0] <= new_birthday < __get_current_week()[1]:
#             if birthday_weekday < 5:
#                 congratulate[WEEKDAYS[birthday_weekday]].append(data['name'])
#             else:
#                 congratulate['monday'].append(data['name'])
#     for k, v in congratulate.items():
#         if len(v):
#             result.append(f"{k}: {' '.join(v)}")
#     return '_' * 50 + '\n' + '\n'.join(result) + '\n' + '_' * 50
#
# print(congratulate())

# import os
# import re
# from pathlib import Path
#
# dir_suff_dict = {"Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
#                  "Documents": [".md", ".epub", ".txt", ".docx", ".doc", ".ods", ".odt", ".dotx", ".docm", ".dox",
#                                ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".xml"],
#                  "Archives": [".iso", ".tar", ".gz", ".7z", ".dmg", ".rar", ".zip"],
#                  "Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"],
#                  "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mpg", ".mpeg", ".3gp"],
#                  "PDF": [".pdf"],
#                  "HTML": [".html", ".htm", ".xhtml"],
#                  "EXE_MSI": [".exe", ".msi"],
#                  "PYTHON": [".py", ".pyw"]}
#
#
# def normalize(name: str) -> str:
#     CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     TRANSLATION = (
#     "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#     "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja")
#
#     TRANS = {}
#     for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#         TRANS[ord(c)] = l
#         TRANS[ord(c.upper())] = l.upper()
#     t_name = name.translate(TRANS)
#     t_name = re.sub(r'\W', '_', t_name)
#     return t_name
#
#
# def sort_func(path_dir):
#     cur_dir = Path(path_dir)
#     dir_path = []
#
#     for root, dirs, files in os.walk(path_dir):
#         for d in dirs:
#             dir_path.append(os.path.join(root, d))
#         for file in files:
#             p_file = Path(root) / file
#             name_normalize = f"{normalize(p_file.name[0:-len(p_file.suffix)])}{p_file.suffix}"
#             p_file.rename(Path(root) / name_normalize)
#             p_file = Path(root) / name_normalize
#             for suff in dir_suff_dict:
#                 if p_file.suffix.lower() in dir_suff_dict[suff]:
#                     dir_img = cur_dir / suff
#                     dir_img.mkdir(exist_ok=True)
#                     try:
#                         p_file.rename(dir_img.joinpath(p_file.name))
#                     except FileExistsError:
#                         p_file.rename(dir_img.joinpath(f'{p_file.name.split(".")[0]}_c{p_file.suffix}'))
#                         print(f"Возможно дубликат: {p_file.name}")
#
#     for dir_p in reversed(dir_path):
#         if os.path.split(dir_p)[1] in dir_suff_dict or os.stat(dir_p).st_size != 0:
#             continue
#         else:
#             os.rmdir(dir_p)
#
#
# if __name__ == "__main__":
#     path_d = input('[+] Введите путь к директории для сортировки: ')
#     if not Path(path_d).exists():
#         print('[-] Директории не существует')
#     else:
#         sort_func(path_d)
#     print('[!] Сортировка завершена')

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






