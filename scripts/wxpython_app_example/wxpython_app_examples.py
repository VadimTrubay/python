__author__ = 'VadimTrubay'

import random
import sys
import time
import wx

APP_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent, title=title, size=size)

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()

        exp_menu = wx.Menu()
        exp_menu.Append(wx.ID_ANY, '&Export image')
        exp_menu.Append(wx.ID_ANY, '&Export video')
        exp_menu.Append(wx.ID_ANY, '&Export data')

        file_menu.Append(wx.ID_NEW, '&New\tCtrl+N')
        file_menu.Append(wx.ID_OPEN, '&Open\tCtrl+O')
        file_menu.Append(wx.ID_SAVE, '&Save\tCtrl+S')
        file_menu.AppendSubMenu(exp_menu, '&Export')
        file_menu.AppendSeparator()

        item = file_menu.Append(APP_EXIT, 'Exit\tCtrl+Q', 'exit to program')
        item.SetBitmap(wx.Bitmap('image/exit.png'))

        menu_bar.Append(file_menu, '&File')

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.cansel, id=APP_EXIT)

    def cansel(self, event):
        self.Close()


app = wx.App()  # create instance app
frame = MyFrame(None, title='gui_lottery_generator', size=(600, 400))  # create main window
frame.Center()
frame.Show()  # window show
app.MainLoop()  # run program
