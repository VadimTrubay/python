#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import re
from common import get_html, process_td
from bs4 import BeautifulSoup


html = get_html()
root = BeautifulSoup(html, 'html.parser')

# Таблица "Награды Пиратов Соломенной Шляпы"
table = root.select('.wikitable')[0]

# Список строк исключая строку заголовка
row_list = table.select('tr')[1:]

# Перебор tr с шагом 2
items = [[process_td(td) for td in x.select('td')] for x in row_list[::2]]

print('Награды:')
for row, x in enumerate(items, 1):
    print('{:2}. {}'.format(row, x))

#  1. ['Монки Д. Луффи', '«Соломенная Шляпа» / «Пятый Император»', '1 500 000 000']
#  2. ['Ророноа Зоро', '«Охотник на пиратов»', '320 000 000']
#  3. ['Нами', '«Кошка воровка»', '66 000 000']
#  4. ['Усопп', '«Согекинг» / «Бог»', '200 000 000']
#  5. ['Винсмок Санджи', '«Черная нога»', '330 000 000']
#  6. ['Тони Тони Чоппер', '«Любитель сахарной ваты»', '100']
#  7. ['Нико Робин', '«Дитя дьявола»', '130 000 000']
#  8. ['Фрэнки', '«Киборг»', '94 000 000']
#  9. ['Брук', '«Напевающий» / «Соул Кинг»', '83 000 000']
# 10. ['Дзимбэй', '«Рыцарь Моря»', 'Более 400 000 000']

print()

print('Награды (по убыванию):')

# Вывод с сортировкой по наградам:
items.sort(key=lambda x: int(re.sub(r'\D', '', x[-1])), reverse=True)

for row, x in enumerate(items, 1):
    print('{:2}. {}'.format(row, x))

#  1. ['Монки Д. Луффи', '«Соломенная Шляпа» / «Пятый Император»', '1 500 000 000']
#  2. ['Дзимбэй', '«Рыцарь Моря»', 'Более 400 000 000']
#  3. ['Винсмок Санджи', '«Черная нога»', '330 000 000']
#  4. ['Ророноа Зоро', '«Охотник на пиратов»', '320 000 000']
#  5. ['Усопп', '«Согекинг» / «Бог»', '200 000 000']
#  6. ['Нико Робин', '«Дитя дьявола»', '130 000 000']
#  7. ['Фрэнки', '«Киборг»', '94 000 000']
#  8. ['Брук', '«Напевающий» / «Соул Кинг»', '83 000 000']
#  9. ['Нами', '«Кошка воровка»', '66 000 000']
# 10. ['Тони Тони Чоппер', '«Любитель сахарной ваты»', '100']
