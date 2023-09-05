'''Разработайте функцию get_days_from_today(date), которая будет возвращать количество дней
от текущей даты, где параметр date — это строка формата '2020-10-09' (год-месяц-день).
Подсказки:
Параметр date разбить на год, месяц и день можно, используя метод строк split.
datetime принимает аргументы типа int, используйте преобразование типов.
игнорируйте часы, минуты и секунды для вашей даты, важны полные дни.
количество дней вы можете получить вычитанием из текущей даты, заданной в date (без времени).
Например: Если текущая дата — 5 мая 2021, то вызов get_days_from_today("2021-10-09") вернет нам -157.'''
from datetime import datetime


def get_days_from_today(date):
    date_lst = date.split('-')
    date_f = datetime(year=int(date_lst[0]), month=int(date_lst[1]), day=int(date_lst[2]))
    date_f = date_f.date()
    today = datetime.now()
    today = today.date()
    difference = today - date_f
    return difference.days

print(get_days_from_today("2021-10-09"))