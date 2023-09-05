#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from tkinter import Tk, messagebox
import traceback


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)

    # Если Yes, сохраняем ошибку в файл
    if messagebox.askyesno("Неизвестная ошибка", "Сохранить лог с ошибкой?"):
        with open('error.txt', 'w', encoding='utf-8') as f:
            f.write(text)

    sys.exit(1)


import sys
sys.excepthook = log_uncaught_exceptions

root = Tk()
root.report_callback_exception = log_uncaught_exceptions


def m_geometry(win):
    # NOTE: this error -> root.report_callback_exception
    # x = (win.winfo_screenwidth() / 2) - (295 / 2)
    y = (win.winfo_screenheight() / 2) - (395 / 2)
    root.wm_geometry("+%d+%d" % (x, y))

# NOTE: this error -> sys.excepthook
m_geometry(None)

# Функция m_geometry(root) сработает через 2 секунды
root.after(2000, lambda: m_geometry(root))

root.mainloop()
