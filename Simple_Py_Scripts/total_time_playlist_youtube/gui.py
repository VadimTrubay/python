#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import traceback

try:
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QWidget
    )

except:
    try:
        from PyQt4.QtGui import (
           QApplication, QMainWindow, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QWidget
        )

    except:
        from PySide.QtGui import (
            QApplication, QMainWindow, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QWidget
        )


from main import parse_playlist_time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('total_time_playlist_youtube')

        self.url_line_edit = QLineEdit()
        self.url_line_edit.returnPressed.connect(self.go)

        self.go_button = QPushButton('Go!')
        self.go_button.clicked.connect(self.go)

        self.result_text = QTextEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.url_line_edit)
        layout.addWidget(self.go_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.result_text)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def go(self):
        try:
            url = self.url_line_edit.text()
            title, total_seconds, total_seconds_text, items = parse_playlist_time(url)

            text = f'Playlist {title!r}:\n'
            for i, (title, time) in enumerate(items, 1):
                text += f'  {i}. {title!r} ({time})\n'
            text += f'\nTotal time: {total_seconds_text} ({total_seconds} total seconds).'

            self.result_text.setPlainText(text)

        except Exception as e:
            text = f'{e}\n\n{traceback.format_exc()}'
            self.result_text.setPlainText(text)


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    # Пусть хоть что-то будет по умолчанию
    mw.url_line_edit.setText('https://www.youtube.com/playlist?list=PLndO6DOY2cLyxQYX7pkDspTJ42JWx07AO')

    app.exec()
