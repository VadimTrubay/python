from datetime import datetime
from random_birthday import get_random_birthdays
import pprint


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
    days_in_month = get_days_in_month(datetime.now().month, datetime.now().year)
    day = datetime.now().day

    if days_in_month == 28 and day > 21:
        count = 0
        for i in range(0, 7):
            i += 1
            if day < 28:
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
                app = datetime.strptime(date_datetime, "%Y, %m, %d")
                list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})

            else:
                while len(list_days_next_week) < 7:
                    count += 1
                    date_datetime = f'{datetime.now().year}, {datetime.now().month + 1}, {count}'
                    app = datetime.strptime(date_datetime, "%Y, %m, %d")
                    list_days_next_week.append({app.strftime("%A"): f'{app.date()}'})

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
    random_birthday = get_random_birthdays(20, 7)
    print()
    print('random_birthdays:')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    pprint.pprint(random_birthday)
    # print('\ndays_next_week:')
    # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # pprint.pprint(get_days_next_week())
    print("\nLet's celebrate birthdays:")
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    concatenation_of_key_values(get_birthdays_on_week(random_birthday))
    print("\nHappy birthday coworkers!!!")
