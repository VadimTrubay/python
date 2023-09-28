from datetime import datetime, timedelta, date
from colorama import init, Fore, Style

data = [
    {'name': 'vad', 'birthday': '29.06.1982'},
    {'name': 'nik', 'birthday': '28.06.1984'},
    {'name': 'vika', 'birthday': '30.06.1985'}]


def get_current_week():
    now = datetime.now()
    current_weekday = now.weekday()
    if current_weekday < 5:
        week_start = now - timedelta(days=2 + current_weekday)
    else:
        week_start = now - timedelta(days=current_weekday - 5)
    return week_start.date(), week_start.date() + timedelta(days=7)


def congratulate(data):
    result = []
    WEEKDAYS = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    congratulate = {'monday': [], 'tuesday': [],
                    'wednesday': [], 'thursday': [], 'friday': []}
    for contact in data:
        if contact['birthday']:
            birthday = contact['birthday']
            birth_day = datetime.strptime(birthday, '%d.%m.%Y')
            birth_day = date(birth_day.year, birth_day.month, birth_day.day)
            current_date = date.today()
            new_birthday = birth_day.replace(year=current_date.year)
            birthday_weekday = new_birthday.weekday()
            if get_current_week()[0] <= new_birthday < get_current_week()[1]:
                if birthday_weekday < 5:
                    congratulate[WEEKDAYS[birthday_weekday]].append(
                        contact['name'])
                else:
                    congratulate['monday'].append(contact['name'])
    print(congratulate)
    for k, v in congratulate.items():
        result.append(Fore.GREEN + f"{k}:" + Fore.WHITE + f" {', '.join(v)}")

    if result:
        return '  ' + '\n  '.join(result)
    else:
        return Fore.RED + '  no birthdays this week'


print(congratulate(data))
