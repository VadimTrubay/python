#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
import traceback

from PyQt5.QtWidgets import (
    QWidget, QApplication, QMessageBox, QVBoxLayout, QGridLayout, QPushButton, QSpinBox, QLabel, QLineEdit, QStyle
)
from PyQt5.QtGui import QPainter, QPaintEvent, QColor
from PyQt5.QtCore import Qt, QTimer

from board import Board, StepResultEnum, get_random_seed


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = f'{ex_cls.__name__}: {ex}:\n'
    text += ''.join(traceback.format_tb(tb))

    if isinstance(ex, KeyboardInterrupt):
        sys.exit(0)

    print(text)
    QMessageBox.critical(None, 'Error', text)
    sys.exit(1)


sys.excepthook = log_uncaught_exceptions


class BoardWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.board = Board()
        self.cell_size = 1

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.cell_size = min(self.width(), self.height()) // min(self.board.rows, self.board.cols)
        if self.cell_size < 1:
            self.cell_size = 1

        self.update()

    def _draw_cell_board(self, painter: QPainter, x: int, y: int, color: QColor):
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        painter.drawRect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)

    def _draw_board(self, painter: QPainter):
        painter.save()

        # Рисование заполненных ячеек
        for y, row in enumerate(self.board.matrix):
            for x, cell in enumerate(row):
                if not cell:
                    continue

                self._draw_cell_board(painter, x, y, Qt.black)

        painter.restore()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self._draw_board(painter)


class MainWindow(QWidget):
    SPEED_MS = 50

    TITLE = 'Life'

    def __init__(self):
        super().__init__()

        self.board_widget = BoardWidget()
        self.board = self.board_widget.board
        self.board.on_update_generation.connect(self._update_states)

        self.timer = QTimer()
        self.timer.timeout.connect(self._on_tick)
        self.timer.setInterval(self.SPEED_MS)

        self.button_start = QPushButton('Start')
        self.button_start.clicked.connect(self.start)

        self.button_timer = QPushButton('Start/Pause')
        self.button_timer.setCheckable(True)
        self.button_timer.clicked.connect(self.start_pause_timer)

        self.sb_timer_interval = QSpinBox()
        self.sb_timer_interval.setRange(10, 5000)
        self.sb_timer_interval.setValue(self.SPEED_MS)
        self.sb_timer_interval.valueChanged.connect(lambda value: self.timer.setInterval(value))

        self.le_seed = QLineEdit(get_random_seed())
        self.le_seed.returnPressed.connect(self.start)
        action_rand_seed = self.le_seed.addAction(
            self.style().standardIcon(QStyle.SP_BrowserReload), QLineEdit.TrailingPosition
        )
        action_rand_seed.triggered.connect(self._do_rand_seed)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.button_timer, 0, 0, 1, 2)
        grid_layout.addWidget(QLabel('Timer (ms):'), 1, 0)
        grid_layout.addWidget(self.sb_timer_interval, 1, 1)
        grid_layout.addWidget(QLabel('Seed:'), 2, 0)
        grid_layout.addWidget(self.le_seed, 2, 1)

        main_layout = QVBoxLayout()
        main_layout.addLayout(grid_layout)
        main_layout.addWidget(self.button_start)
        main_layout.addWidget(self.board_widget)

        self.setLayout(main_layout)
        self._update_states()

    def _do_rand_seed(self):
        self.le_seed.setText(get_random_seed())

    def start(self):
        self.board.generate(seed=self.le_seed.text())

        self.timer.stop()
        self.start_pause_timer()

    def start_pause_timer(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()

        self._update_states()

    def _update_states(self):
        is_paused = not self.timer.isActive()
        prefix = '[IS PAUSED] ' if is_paused else ''
        self.setWindowTitle(
            f'{prefix}{self.TITLE}. '
            f'Board: {self.board.rows}x{self.board.cols}. '
            f'Seed: {self.board.seed}. '
            f'Generation: {self.board.generation_number}. '
            f'Living cells: {self.board.count_living_cells}'
        )

        self.button_timer.setChecked(self.timer.isActive())

    def abort_game(self, reason: str):
        self.timer.stop()
        self._update_states()
        QMessageBox.information(self, "Информация", f"Проигрыш! {reason}")

    def _on_logic(self):
        result = self.board.do_step()
        if result == StepResultEnum.OK:
            return

        match result:
            case StepResultEnum.NO_CELLS:
                reason = 'Закончили клетки'
            case StepResultEnum.NO_CHANGE:
                reason = 'Мир перестал меняться'
            case StepResultEnum.REPEATS:
                reason = 'Мир зациклен'
            case _:
                raise Exception(f'Неизвестный результат {result}')

        self.abort_game(reason)

    def _on_tick(self):
        self._on_logic()
        self._update_states()
        self.board_widget.update()


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.resize(600, 600)
    mw.show()

    app.exec()
