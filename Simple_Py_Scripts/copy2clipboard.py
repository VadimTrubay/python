#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def to(text):
    try:
        from PyQt5.QtGui import QGuiApplication as QApplication

    except ImportError:
        try:
            from PyQt4.QtGui import QApplication

        except ImportError:
            from PySide.QtGui import QApplication

    app = QApplication([])
    app.clipboard().setText(text)
    app = None


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        print('Text: "{}"'.format(text))
        to(text)

    else:
        import os
        file_name = os.path.basename(sys.argv[0])
        print('usage: {} [-h] text'.format(file_name))
