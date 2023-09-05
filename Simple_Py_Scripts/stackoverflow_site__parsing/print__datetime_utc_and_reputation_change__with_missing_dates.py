#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import datetime as DT


def generate_range_dates(start_date, end_date) -> list:
    date_1 = min(start_date, end_date)
    date_2 = max(start_date, end_date)

    # Сразу добавляем стартовую дату
    items = [date_1]

    while date_1 < date_2:
        date_1 += DT.timedelta(days=1)
        items.append(date_1)

    return items


if __name__ == '__main__':
    url = 'https://ru.stackoverflow.com/users/201445/gil9red?tab=reputation'

    from print__datetime_utc_and_reputation_change import get_day_by_rep
    day_by_rep = get_day_by_rep(url)

    start_date, end_date = min(day_by_rep), max(day_by_rep)
    print('Start: {}, end: {}'.format(start_date, end_date))
    print()

    # Сгенерируем диапазон дат
    dates = generate_range_dates(start_date, end_date)

    # Print
    for day in reversed(dates):
        print('{:%d/%m/%Y} : {}'.format(day, day_by_rep.get(day, 0)))
