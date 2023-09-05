__author__ = 'ipetrash'


from grab import Grab
import sys
from PySide.QtGui import *
from threading import Thread
import time


def get_confucius_quotes():
    g = Grab()
    # http://ru.wikiquote.org/wiki/Конфуций
    url = "http://ru.wikiquote.org/wiki/%D0%9A%D0%BE%D0%BD%D1%84%D1%83%D1%86%D0%B8%D0%B9"
    g.go(url)

    quotes = list()
    for el in g.doc.select('//h2/following-sibling::ul/li'):
        quotes.append(el.text())

    return quotes


class MyThread(Thread):
    def __init__(self, log):
        super().__init__()
        self.log = log

    def run(self):
        for i, quote in enumerate(get_confucius_quotes(), 1):
            self.log.append('{}. "{}"\n'.format(i, quote))
            time.sleep(0.1)  # задержка каждые 100 миллисекунд


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.te_quotes = QTextEdit()
        self.te_quotes.setReadOnly(True)
        self.setCentralWidget(self.te_quotes)

    def slot_refresh(self):
        self.te_quotes.clear()
        thread = MyThread(self.te_quotes)
        thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()
    w.setWindowTitle("Пример 4")
    w.show()
    w.slot_refresh()

    sys.exit(app.exec_())
