from datetime import datetime
import name_list
import random


def get_random_birthdays(n, end):

    """The function receives the number of required birthday dates
    in the range from n to the end and returns a list of such dates """

    current_days = datetime.now()
    birthdays_list = []

    while len(birthdays_list) < n:
        coworker_birthday = random.randint(current_days.day - 3, current_days.day + end)
        try:
            test_birthday = datetime(year=current_days.year, month=current_days.month, day=coworker_birthday)

        except ValueError:
            continue

        birthdays_list.append({'name': name_list.get_names(), 'birthday': f'{test_birthday.date()}'})

    return birthdays_list


# if __name__ == '__main__':
#     get_random_birthdays()
