#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
import traceback

from typing import Optional

from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QPaintEvent, QKeyEvent, QColor
from PyQt5.QtCore import Qt, QTimer

from board import Board
from config import DEBUG
from common import logger
from piece import Piece


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = f'{ex_cls.__name__}: {ex}:\n'
    text += ''.join(traceback.format_tb(tb))

    logger.error(text)
    QMessageBox.critical(None, 'Error', text)
    sys.exit(1)


sys.excepthook = log_uncaught_exceptions


class MainWindow(QWidget):
    CELL_SIZE = 20
    SPEED_MS = 400

    TITLE = 'Tetris'

    def __init__(self):
        super().__init__()

        self.board = Board()
        self.board.on_update_score.connect(self._update_states)

        self.current_piece: Optional[Piece] = None
        self.next_piece: Optional[Piece] = None

        self.timer = QTimer()
        self.timer.timeout.connect(self._on_tick)
        self.timer.setInterval(self.SPEED_MS)
        self.timer.start()

        self._update_states()

    def _update_states(self):
        self.setWindowTitle(f'{self.TITLE}. Score: {self.board.score}')

    def abort_game(self):
        self.timer.stop()
        QMessageBox.information(self, "Информация", "Проигрыш!")

    def _on_logic(self):
        if not self.board.do_step():
            self.abort_game()
            return

        self.current_piece = self.board.current_piece
        self.next_piece = self.board.next_piece

    def _on_tick(self):
        self._on_logic()
        self._update_states()
        self.update()

    def _draw_cell_board(self, painter: QPainter, x: int, y: int, color: QColor):
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        painter.drawRect(x * self.CELL_SIZE, y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)

    def _draw_board(self, painter: QPainter):
        painter.save()

        # Рисование заполненных ячеек
        for y, row in enumerate(self.board.matrix):
            for x, cell_color in enumerate(row):
                if not cell_color:
                    continue

                self._draw_cell_board(painter, x, y, cell_color)

        painter.setPen(Qt.black)

        # Горизонтальные линии
        y1, y2 = 0, 0
        for i in range(self.board.ROWS + 1):
            painter.drawLine(0, y1, self.CELL_SIZE * self.board.COLS, y2)
            y1 += self.CELL_SIZE
            y2 += self.CELL_SIZE

        # Вертикальные линии
        x1, x2 = 0, 0
        for i in range(self.board.COLS + 1):
            painter.drawLine(x1, 0, x2, self.CELL_SIZE * self.board.ROWS)
            x1 += self.CELL_SIZE
            x2 += self.CELL_SIZE

        painter.restore()

    def _draw_current_piece(self, painter: QPainter):
        if not self.current_piece:
            return

        painter.save()

        for x, y in self.current_piece.get_points():
            self._draw_cell_board(painter, x, y, self.current_piece.get_color())

        # Рисуем центр фигуры
        if DEBUG:
            self._draw_cell_board(painter, self.current_piece.x, self.current_piece.y, Qt.black)

        x_next = self.board.COLS + 3
        y_next = 1
        for x, y in self.next_piece.get_points_for_state(x=x_next, y=y_next):
            self._draw_cell_board(painter, x, y, self.next_piece.get_color())

        painter.restore()

    def _draw_score(self, painter: QPainter):
        painter.save()

        painter.setPen(Qt.black)

        x, y = self.CELL_SIZE * (self.board.COLS + 1), self.CELL_SIZE * 5
        painter.drawText(x, y, f'Score: {self.board.score}')

        painter.restore()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self._draw_board(painter)
        self._draw_current_piece(painter)
        self._draw_score(painter)

    def keyReleaseEvent(self, event: QKeyEvent):
        match event.key():
            case Qt.Key_Left if self.current_piece:
                if self.current_piece.move_left():
                    self.update()

            case Qt.Key_Right if self.current_piece:
                if self.current_piece.move_right():
                    self.update()

            case Qt.Key_Up if self.current_piece:
                if self.current_piece.turn():
                    self.update()

            case Qt.Key_Down if self.current_piece:
                while self.current_piece.move_down():
                    self.update()


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.resize(360, 480)
    mw.show()

    app.exec()
