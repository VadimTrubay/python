from tkinter import *
from tkinter import ttk
import random
import sys

runing = True


def run():
    def get_selected_ball(even):  # получаем выделенный элемент1
        global selected_ball
        selected_ball = int(combobox_ball.get())
        print(selected_ball)

    def get_selected_all_ball(event):  # получаем выделенный элемент1
        global selected_all_ball
        selected_all_ball = int(combobox_all_ball.get())
        print(selected_all_ball)

    def get_balls():  # start
        start_list = list(range(1, selected_all_ball + 1))
        new_list = []
        for i in range(1, selected_ball + 1):
            random.shuffle(start_list)
            num = random.choice(start_list)
            new_list.append(num)
            start_list.remove(num)
        for i in new_list:
            b = Button(text=f"{i}")  # создаем кнопку из пакета ttk
            b.pack()

    def clear():
        root.destroy()

    def exiting():
        global runing
        runing = False
        root.destroy()

    root = Tk()  # создаем корневой объект - окно
    root.title("gui_lottery_generator")  # устанавливаем заголовок окна
    root.iconbitmap(default="favicon.ico")  # установим иконку
    root.resizable(False, False)  # запрет изменение окна
    root.geometry("600x400+300+100")  # устанавливаем размеры окна
    root.update_idletasks()
    label = Label(text="gui_lottery_generator")  # создаем текстовую метку
    label.pack()  # размещаем метку в окне

    button_clear = Button(text="Clear", command=clear)
    button_clear.pack(anchor=NW, fill=X, padx=0, pady=0)

    button_exiting = Button(text="Exit", command=exiting)
    button_exiting.pack(anchor=NW, fill=X, padx=0, pady=0)

    label_choose_ball = ttk.Label(text="choose ball")
    label_choose_ball.pack(anchor=NW, fill=X, padx=0, pady=0)

    combobox_ball = ttk.Combobox(values=[str(i) for i in range(13)],
                                 justify=CENTER, width=5, state="readonly",
                                 )
    combobox_ball.pack(anchor=NW, padx=0, pady=0)
    combobox_ball.bind("<<ComboboxSelected>>", get_selected_ball)

    label_choose_all_ball = ttk.Label(text="choose all ball")
    label_choose_all_ball.pack(anchor=NW, fill=X, padx=0, pady=0)
    combobox_all_ball = ttk.Combobox(values=[str(i) for i in range(66)],
                                     justify=CENTER, width=5, state="readonly",
                                     )
    combobox_all_ball.pack(anchor=NW, padx=0, pady=0)
    combobox_all_ball.bind("<<ComboboxSelected>>", get_selected_all_ball)

    button_start = Button(text="Start", command=get_balls)  # создаем кнопку из пакета ttk
    button_start.pack()
    root.mainloop()


while runing:
    run()
