#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from PyQt5 import Qt
from urllib import request


class LoadImageThread(Qt.QThread):
    about_new_image = Qt.pyqtSignal(Qt.QPixmap)

    def run(self):
        data = request.urlopen(self.url).read()
        pixmap = Qt.QPixmap()
        pixmap.loadFromData(data)

        # Передаем картинку с сигналом
        self.about_new_image.emit(pixmap)


class URLView(Qt.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = Qt.QVBoxLayout(self)

        self.urlEdit = Qt.QLineEdit()
        self.urlEdit.setText('https://www.python.org/static/img/python-logo.png')
        layout.addWidget(self.urlEdit)

        self.imageLabel = Qt.QLabel("No image")
        self.imageLabel.setScaledContents(True)
        layout.addWidget(self.imageLabel)

        self.loadButton = Qt.QPushButton("Load")
        layout.addWidget(self.loadButton)

        self.loadButton.clicked.connect(self.on_load)

        # Создаем объект потока и привязываем его сигнал к слоту установки картинки
        self.thread = LoadImageThread()
        self.thread.about_new_image.connect(self.imageLabel.setPixmap)

        # Пока выполняется загрузка картинки, кнопка недоступна
        self.thread.started.connect(lambda: self.loadButton.setEnabled(False))
        self.thread.finished.connect(lambda: self.loadButton.setEnabled(True))

    def on_load(self):
        print("Load image")

        # Запускаем поток
        self.thread.url = self.urlEdit.text()
        self.thread.start()


if __name__ == '__main__':
    app = Qt.QApplication([])
    w = URLView()
    w.show()
    app.exec()
