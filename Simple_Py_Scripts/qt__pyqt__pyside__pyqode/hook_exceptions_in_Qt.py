#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from PyQt5.QtWidgets import *


# Для отлова всех исключений, которые в слотах Qt могут "затеряться" и привести к тихому падению
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)

    import traceback
    text += ''.join(traceback.format_tb(tb))

    print('Error: ', text)
    QMessageBox.critical(None, 'Error', text)
    sys.exit(1)


import sys
sys.excepthook = log_uncaught_exceptions


app = QApplication([])

w = QLineEdit()
w.textChanged.conneect(lambda x: 1 + '1')

# Emit textChanged signal
w.setText('!!!')
