def get_birthdays_per_week(users):  # дні народження наступного тижня

    from datetime import datetime, timedelta

    bithdays_next_week = {0: ['Monday', []], 1: ['Tuesday', []], 2: ['Wednesday', []],
                          3: ['Thursday', []], 4: ['Friday',  []]}

    current_datetime = datetime.now()

    # залишилось до суботи(int) цього тижня(може бути -1)
    to_saturday = 5 - current_datetime.weekday()

    this_saturday = current_datetime + \
        timedelta(days=to_saturday)   # субота цього тижня(datetime)
    # субота наступного тижня(datetime)
    next_saturday = this_saturday + timedelta(days=7)

    for di in users:
        bd = di['bithday']
        # ДН в цьому році(datetime)
        bithday_this_year = datetime(current_datetime.year, bd.month, bd.day)
        if this_saturday.date() <= bithday_this_year.date() < next_saturday.date():
            if bithday_this_year.weekday() > 4:  # додаємо ДН за вихідні на понеділок
                bithdays_next_week[0][1].append(di['name'])
            else:
                bithdays_next_week[bithday_this_year.weekday()][1].append(
                    di['name'])  # сортуємо інші ДН

    for value in bithdays_next_week.values():  # Роздруковуємо
        if value[1]:
            print(value[0].ljust(10) + ':', end=' ')
            for i in range(len(value[1]) - 1):
                print(value[1][i], end=', ')
            print(value[1][len(value[1]) - 1])
