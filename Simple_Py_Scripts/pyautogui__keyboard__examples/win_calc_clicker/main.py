#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


BUTTONS = {
    '+': 'buttons/add.png',
    '-': 'buttons/sub.png',
    '/': 'buttons/div.png',
    '*': 'buttons/mul.png',
    '=': 'buttons/equal.png',
}
for i in range(10):
    BUTTONS[str(i)] = 'buttons/{}.png'.format(i)

CACHE_POS_BUTTON = dict()


def go(expression):
    # OpenCv -- for performance
    # pip install opencv-python

    # pip install pyautogui
    import pyautogui

    for x in expression:
        if x not in BUTTONS:
            print('Not found: "{}"'.format(x))
            continue

        if x in CACHE_POS_BUTTON:
            pos = CACHE_POS_BUTTON[x]
        else:
            file_name = BUTTONS[x]
            pos = pyautogui.locateCenterOnScreen(file_name)
            if not pos:
                continue

            CACHE_POS_BUTTON[x] = pos

        print(x, pos)
        pyautogui.click(pos)


def show_test_calc():
    import os
    os.startfile('calc.exe')

    import time
    time.sleep(1)


if __name__ == '__main__':
    show_test_calc()

    expression = '1234 * 222 + 3214 = '
    go(expression)
