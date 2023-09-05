#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# Генерация списка
items = ['KMS1.kmch.pos.out_dE_%s.mx' % i for i in range(20)]

# Перемешивание элементов списка
import random
random.shuffle(items)

print(items)

# Обычная сортировка не работает
print(sorted(items))
print()


def get_number_1(x):
    return int(x.split('.')[-2].split('_')[-1])


def get_number_2(x):
    import re
    match = re.search('KMS1.kmch.pos.out_dE_(\d+).mx', x)
    return int(match.group(1))


print(sorted(items, key=get_number_1))
print(sorted(items, key=get_number_2))
