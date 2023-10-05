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
        self.selected_ball = 3
        self.selected_all_ball = 6
        self.number_display = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)

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
        self.Bind(wx.EVT_TOOL, self.clear_all, id=APP_CLEAR)
        self.Bind(wx.EVT_TOOL, self.cansel, id=APP_EXIT)

        self.ctx = AppContextMenu(self)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        sizer = wx.BoxSizer()
        sizer.Add(self.number_display, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def OnRightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition())

    def start(self, event):
        self.number_display.Clear()
        numbers = list(range(1, self.selected_all_ball + 1))
        for _ in range(self.selected_ball):
            num = random.choice(numbers)
            self.number_display.AppendText(str(num) + ' ')
            numbers.remove(num)
            random.shuffle(numbers)
            time.sleep(1)

    def sort(self, event):
        current_numbers = self.number_display.GetValue().strip()
        if not current_numbers:
            return
        current_numbers_list = [int(num.strip()) for num in current_numbers.split(' ')]
        sorted_numbers_list = sorted(current_numbers_list)
        sorted_numbers_text = ' '.join(map(str, sorted_numbers_list))
        self.number_display.SetValue(sorted_numbers_text)

    def clear_all(self, event):
        self.number_display.SetValue('')

    def cansel(self, event):
        self.Close()


app = wx.App()  # create instance app
frame = MyFrame(None, title='gui_lottery_generator', size=(600, 400))  # create main window
frame.Center()
frame.Show()  # window show
app.MainLoop()  # run program

#
#
# def main():
#     def try_again():
#         # Ask the user if they want to run again
#         response = askyesno("Generate Again", "Do you want to generate again?")
#         if response:
#             clear()
#             return
#         else:
#             pass
#
#     def get_selected_ball(event):
#         global selected_ball
#         selected_ball = int(combobox_ball.get())
#         print(selected_ball)
#
#     def get_selected_all_ball(event):
#         global selected_all_ball
#         selected_all_ball = int(combobox_all_ball.get())
#         print(selected_all_ball)
#
#     def get_balls():
#         global new_list
#         new_list = []
#         numbers = list(range(1, selected_all_ball + 1))
#         column = 3
#         for _ in numbers[:selected_ball]:
#             num = random.choice(numbers)
#             b = Button(text=f"{num}")
#             # print(num, sep='\n')
#             b.grid(row=7, column=column, padx=10, pady=10)
#             column += 1
#             # label_choose_ball.config(text=f"ball: {selected_ball}")
#             # label_choose_all_ball.config(text=f"all ball: {selected_all_ball}")
#             new_list.append(num)
#             numbers.remove(num)
#             random.shuffle(numbers)
#             root.update()
#             time.sleep(1)
#         try_again()
#         print(new_list)
#
#     def sort_balls():
#         new_list.sort()
#         column = 3
#         for num in new_list:
#             b = Button(text=f"{num}")
#             b.grid(row=9, column=column, padx=10, pady=10)
#             column += 1
#             # label_choose_ball.config(text=f"ball: {selected_ball}")
#             # label_choose_all_ball.config(text=f"all ball: {selected_all_ball}")
#             root.update()
#             time.sleep(1)
#         try_again()
#         print(new_list)
#
#     def clear():
#         root.destroy()
#
#     def exiting():
#         global running
#         running = False
#         root.destroy()
#
#
#
#     root.update_idletasks()
#     # устанавливаем тему "classic"
#     ttk.Style().theme_use("clam")
#     font1 = font.Font(family="Arial", size=10, weight="bold", slant="roman", underline=True)
#     label = Label(text="gui_lottery_generator")
#     label.grid(row=0, column=0, padx=10, pady=10)
#
#     button_clear = Button(text="Clear", command=clear, bg="#F4A460", fg="#FFFFFF", font=font1)
#     button_clear.grid(row=1, column=0, padx=10, pady=10)
#
#     button_exiting = Button(text="Exit", command=exiting, bg="#8B0000", fg="#FFFFFF", font=font1)
#     button_exiting.grid(row=1, column=1, padx=10, pady=10)
#
#     label_choose_ball = ttk.Label(text="ball")
#     label_choose_ball.grid(row=2, column=0, padx=10, pady=10)
#
#     values_ball = [str(i) for i in range(9)]
#     values_var = StringVar(value=str(selected_ball))
#     combobox_ball = ttk.Combobox(values=values_ball,
#                                  justify=CENTER,
#                                  width=5,
#                                  state="readonly",
#                                  textvariable=values_var)
#     combobox_ball.grid(row=2, column=1, padx=10, pady=10)
#     values_var.get()
#     combobox_ball.bind("<<ComboboxSelected>>", get_selected_ball)
#
#     label_choose_all_ball = ttk.Label(text="all ball")
#     label_choose_all_ball.grid(row=3, column=0, padx=10, pady=10)
#
#     button_start = Button(text="Start", command=get_balls, bg="#008000", fg="#FFFFFF", font=font1)
#     # print(button_start)
#     button_start.grid(row=5, column=0, padx=10, pady=10)
#
#     button_start = Button(text="Sort", command=sort_balls, bg="#1E90FF", fg="#FFFFFF", font=font1)
#     button_start.grid(row=5, column=1, padx=10, pady=10)
#
#     values_all_ball = [str(i) for i in range(55)]
#     values_all_var = StringVar(value=str(selected_all_ball))
#     combobox_all_ball = ttk.Combobox(values=values_all_ball,
#                                      justify=CENTER,
#                                      width=5,
#                                      state="readonly",
#                                      textvariable=values_all_var)
#     combobox_all_ball.grid(row=3, column=1, padx=10, pady=10)
#     combobox_all_ball.bind("<<ComboboxSelected>>", get_selected_all_ball)
#     print(selected_ball)
#     print(selected_all_ball)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     while running:
#         main()
