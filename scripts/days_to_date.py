from datetime import datetime


def get_days():
    """function calculates the days to date"""
    user_input = input('Enter the date to (dd.mm)>:')
    user_date = datetime.strptime(user_input, '%d.%m')
    curent_date = datetime.now()
    user_date = user_date.replace(year=curent_date.year)
    delta_days = user_date - curent_date
    target_date = datetime.strftime(user_date, "%d-%B-%Y")

    if delta_days.days > 0:
        print(f'{delta_days.days} days left to date before {target_date}\n')
    else:
        user_date = user_date.replace(year=user_date.year + 1)
        delta_days = user_date - curent_date
        print(f'{delta_days.days} days left to date before {target_date}\n')

# def make_backup(data):
#     current_time = datetime.now()
#     with open(f'backup_{current_time.hour}.txt', 'w') as fh:
#         fh.write(data)
# make_backup('regtgdyhe')

if __name__ == '__main__':
    get_days()
