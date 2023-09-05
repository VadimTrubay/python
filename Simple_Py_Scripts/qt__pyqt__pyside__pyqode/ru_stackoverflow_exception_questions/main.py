#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""Скрипт добавляет метку 'исключения' для указанных вопросов."""


import sys
from PySide.QtGui import QApplication


import json
config = json.load(open('config', encoding='utf8'))
LOGIN = config['login']
PASSWORD = config['password']

#
# import time
# import traceback


from gatherer import query, session

from web_tag_editor import WebTagEditor, get_logger

logger = get_logger('so_questions')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # TODO: удалять из базы измененный вопрос

    # tag_editor = WebTagEditor(LOGIN, PASSWORD, query.all()[-1].url)
    tag_editor = WebTagEditor(LOGIN, PASSWORD, 'https://ru.stackoverflow.com/questions/504080')
    tag_editor.show()
    tag_editor.go()

    sys.exit(app.exec_())
