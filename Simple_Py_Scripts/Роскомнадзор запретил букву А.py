#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
result = "Роскомнадзор запретил букву "

# Перебор всех символов алфавита
for i in alp:
    # Проверяем, что в строке result текущая буква найдена
    if i in result or i.upper() in result:
        # Выводим надпись
        print(result + i.upper())

        # Удаляем букву из надписи
        result = result.replace(i, '')
        result = result.replace(i.upper(), '')
