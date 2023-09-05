''' Напишите функцию для определения количества дней в конкретном месяце.
Ваша функция должна принимать два параметра:
month — номер месяца в виде целого числа в диапазоне от 1 до 12 и year — год, состоящий из четырех цифр.
Убедитесь, что функция корректно обрабатывает февраль високосного года.    '''



from datetime import date


def get_days_in_month(month, year):

    if year % 4 == 0:
        if month == 2:
            return 29
    elif year % 4 != 0:
        if month == 2:
            return 28
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30

print(get_days_in_month(5, 2022))