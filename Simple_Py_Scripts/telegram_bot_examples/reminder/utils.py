#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import datetime as DT
from typing import Optional
import re


PATTERN = re.compile(
    r'напомни через (\d+) (секунд|минут|час|день|дня|дней|неделю|недели|недель|)',
    flags=re.IGNORECASE
)


def parse_command(command: str) -> Optional[DT.datetime]:
    m = PATTERN.search(command)
    if not m:
        return

    value, kind = m.groups()
    kind = kind.lower()
    value = int(value)

    if kind == 'секунд':
        data = dict(seconds=value)
    elif kind == 'минут':
        data = dict(minutes=value)
    elif kind == 'час':
        data = dict(hours=value)
    elif kind in ['день', 'дня', 'дней']:
        data = dict(days=value)
    elif kind in ['неделю', 'недели', 'недель']:
        data = dict(weeks=value)
    else:
        return

    return DT.datetime.now() + DT.timedelta(**data)


def get_pretty_datetime(finish_time: DT.datetime) -> str:
    return finish_time.strftime('%d.%m.%Y %H:%M:%S')


if __name__ == '__main__':
    date_time = DT.datetime.now()
    print('Current datetime:', get_pretty_datetime(date_time))
    print()

    commands = [
        'напомни через 10 секунд', 'НАПОМНИ ЧЕРЕЗ 1 час',
        'напомни через 5 часов', 'напомни через 1 день'
    ]
    fmt = "{:%s} -> {}" % len(max(commands, key=len))

    for command in commands:
        date_time = parse_command(command)
        print(fmt.format(command, get_pretty_datetime(date_time)))
