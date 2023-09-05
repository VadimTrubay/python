#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://stepik.org/lesson/360560/step/12?unit=345000


"""
Напишите программу, которая выводит решение ребуса ЖУК*ЕЖ=ЖЖЖЖЖ. 
Одинаковым буквам соответствуют одинаковые цифры. 
Разным буквам соответствуют разные цифры. Числа не могут начинаться с нуля.

В выводе между цифрами и знаками должны отсутствовать пробелы. 
"""

for ж in range(10):
    for у in range(10):
        for к in range(10):
            for е in range(10):
                # Разным буквам соответствуют разные цифры
                if len({ж, у, к, е}) != 4:
                    continue

                жук = int(f'{ж}{у}{к}')
                еж = int(f'{е}{ж}')
                жжжжж = int(f'{ж}' * 5)
                if (жук < 100 or жук > 999) or (еж < 10 or еж > 99) or (жжжжж < 10000 or жжжжж > 99999):
                    continue

                if жук * еж == жжжжж:
                    print(f'{жук}*{еж}={жжжжж}')

"""
271*82=22222
"""
