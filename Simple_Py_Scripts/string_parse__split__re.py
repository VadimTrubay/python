#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


text = """\
Пушкин 1799-1837
Лермонтов 1814-1841
"""


import re
for name, start, end in re.findall(r'(\w+) (\d+)-(\d+)', text):
    print('{}, {} лет'.format(name, int(end) - int(start)))

print()

for line in text.splitlines():
    name, age = line.split()
    start, end = map(int, age.split('-'))

    print('{}, {} лет'.format(name, end - start))
