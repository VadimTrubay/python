#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from common import get_parsed_two_column_table_stats


def get_stats_ds1() -> [(str, str)]:
    url = 'http://ru.darksouls.wikia.com/wiki/Характеристики_(Dark_Souls)'
    return get_parsed_two_column_table_stats(url)


if __name__ == '__main__':
    items = get_stats_ds1()
    print(f'items ({len(items)}): {items}')
    print()

    # ['Вера', 'Выносливость', 'Живучесть', 'Интеллект', 'Ловкость', 'Поиск предметов', 'Сила', 'Сопротивление', 'Уровень', 'Ученость', 'Человечность']
    stats_titles = [x[0] for x in items]
    print(stats_titles)

    print()

    for title, description in items:
        print('{:20}: {}'.format(title, repr(description)))
