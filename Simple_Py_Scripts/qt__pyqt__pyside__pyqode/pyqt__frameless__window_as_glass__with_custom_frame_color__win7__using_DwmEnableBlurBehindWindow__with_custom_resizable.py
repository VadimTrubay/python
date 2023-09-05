#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from pyqt__mouse_manual_move__FramelessWindowHint__with_custom_resizable import ResizableFramelessWidget


from ctypes.wintypes import DWORD, HRGN
from ctypes import windll, c_bool, c_int, POINTER, Structure
from ctypes import WINFUNCTYPE


class DWM_BLURBEHIND(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa969500%28v=vs.85%29.aspx
    """
    _fields_ = [
        ('dwFlags', DWORD),
        ('fEnable', c_bool),
        ('hRgnBlur', HRGN),
        ('fTransitionOnMaximized', c_bool)
    ]


prototype = WINFUNCTYPE(c_int, c_int, POINTER(DWM_BLURBEHIND))
params = (1, "hWnd", 0), (1, "pBlurBehind", 0)
_DwmEnableBlurBehindWindow = prototype(("DwmEnableBlurBehindWindow", windll.dwmapi), params)

# Before we get started, see if we have the DWM functions.
has_dwm = hasattr(windll, 'dwmapi') and hasattr(windll.dwmapi, 'DwmIsCompositionEnabled')


# SOURCE: https://github.com/stendec/siding/blob/master/siding/_aeroglass.py
def DWM_enable_blur_behind_window(widget):
    DWM_BB_ENABLE = 0x0001

    bb = DWM_BLURBEHIND()
    bb.fEnable = c_bool(True)
    bb.dwFlags = DWM_BB_ENABLE
    bb.hRgnBlur = None

    # NOTE: с WA_TranslucentBackground клики проходят сквозь окно
    # widget.setAttribute(Qt.WA_TranslucentBackground)
    widget.setAttribute(Qt.WA_NoSystemBackground)

    result = _DwmEnableBlurBehindWindow(c_int(widget.winId()), bb)

    return not result


class Widget(ResizableFramelessWidget):
    def __init__(self):
        super().__init__()

        DWM_enable_blur_behind_window(self)

        self.frame_color = Qt.darkCyan

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(QPushButton("Закрыть окно", clicked=self.close))

        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(Qt.transparent)
        painter.setPen(QPen(Qt.darkCyan, self.MARGINS))

        painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.resize(400, 300)
    w.show()

    app.exec()
