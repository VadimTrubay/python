__author__ = 'VadimTrubay'

import random
import sys
import time
import wx

APP_START = 1
APP_SORT = 2
APP_CLEAR = 3
APP_EXIT = 4


class AppContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        it_min = self.Append(wx.ID_ANY, 'Minimum size')
        it_max = self.Append(wx.ID_ANY, 'Maximum size')
        self.Bind(wx.EVT_MENU, self.onMinimize, it_min)
        self.Bind(wx.EVT_MENU, self.onMaximize, it_max)

    def onMinimize(self, event):
        self.parent.Iconize()

    def onMaximize(self, event):
        self.parent.Maximize()



class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent, title=title, size=size)
        self.selected_ball = 4
        self.selected_all_ball = 9
        self.list_result = []
        menu_bar = wx.MenuBar()

        menu_start = wx.Menu()
        menu_sort = wx.Menu()
        menu_clear_all = wx.Menu()
        menu_exit = wx.Menu()


        menu_bar.Append(menu_start, 'Start')
        menu_bar.Append(menu_sort, 'Sort')
        menu_bar.Append(menu_clear_all, 'Clear')
        menu_bar.Append(menu_exit, 'Exit')

        self.SetMenuBar(menu_bar)

        toolbar = self.CreateToolBar()
        toolbar.AddTool(APP_START, 'Start', wx.Bitmap('image/start32.png'))
        toolbar.AddSeparator()
        toolbar.AddTool(APP_SORT, 'Sort', wx.Bitmap('image/sort32.png'))
        toolbar.AddSeparator()
        toolbar.AddTool(APP_CLEAR, 'Clear', wx.Bitmap('image/clear32.png'))
        toolbar.AddSeparator()
        toolbar.AddTool(APP_EXIT, 'Exit', wx.Bitmap('image/exit32.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.start, id=APP_START)
        self.Bind(wx.EVT_TOOL, self.sort, id=APP_SORT)
        self.Bind(wx.EVT_MENU, self.clear_all, id=APP_CLEAR)
        self.Bind(wx.EVT_TOOL, self.cansel, id=APP_EXIT)

        self.ctx = AppContextMenu(self)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.panel = wx.Panel(self)
        self.vbox = wx.BoxSizer()



    def OnRightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition())

    def start(self, event):

        numbers = list(range(1, self.selected_all_ball + 1))

        for _ in range(self.selected_ball):
            num = random.choice(numbers)
            self.list_result.append(num)
            print(num)


            button = wx.Button(self.panel, label=f'{num}', size=(50, 50))

            hbox = wx.BoxSizer()
            hbox.Add(button, 0, wx.LEFT + 10 | wx.RIGHT + 10, 20)
            self.vbox.Add(hbox, flag=wx.ALIGN_CENTRE)
            self.panel.SetSizer(self.vbox)
            self.Layout()

            numbers.remove(num)
            random.shuffle(numbers)
            time.sleep(1)



    def sort(self, event):
        pass


    def clear_all(self, event):
        self.panel = self.GetChildren()[0]
        # Get the panel containing the buttons
        self.panel.DestroyChildren()
        print('ok')# Remove all child buttons from the panel
        self.Layout()

    def cansel(self, event):
        print('exit')
        self.Close()

def main():
    app = wx.App()  # create instance app
    frame = MyFrame(None, title='gui_lottery_generator', size=(600, 400))  # create main window
    frame.Center()
    frame.Show()  # window show
    app.MainLoop()  # run program


if __name__ == '__main__':
    # while running:
    main()
