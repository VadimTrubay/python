from tkinter import *
from tkinter import ttk
import random
import sys
import time
from tkinter import font

running = True


def run():
    def get_selected_ball(event):
        global selected_ball
        selected_ball = int(combobox_ball.get())
        print(selected_ball)

    def get_selected_all_ball(event):
        global selected_all_ball
        selected_all_ball = int(combobox_all_ball.get())
        print(selected_all_ball)

    def get_balls():
        numbers = list(range(1, selected_all_ball + 1))
        column = 3
        global new_list
        new_list = []
        for _ in numbers[:selected_ball]:
            num = random.choice(numbers)
            b = Button(text=f"{num}")
            b.grid(row=7, column=column, padx=10, pady=10)
            column += 1
            label_choose_ball.config(text=f"choose ball: {selected_ball}")
            label_choose_all_ball.config(text=f"choose all ball: {selected_all_ball}")
            new_list.append(num)
            numbers.remove(num)
            random.shuffle(numbers)
            print(numbers)
            root.update()
            time.sleep(1)

    def sort_balls():
        list_sort = sorted(new_list)
        column = 3
        for num in list_sort:
            b = Button(text=f"{num}")
            b.grid(row=9, column=column, padx=10, pady=10)
            column += 1
            label_choose_ball.config(text=f"choose ball: {selected_ball}")
            label_choose_all_ball.config(text=f"choose all ball: {selected_all_ball}")
            root.update()
            time.sleep(1)

    def clear():
        root.destroy()

    def exiting():
        global running
        running = False
        root.destroy()

    root = Tk()
    root.title("gui_lottery_generator")
    root.iconbitmap(default="favicon.ico")
    root.resizable(False, False)
    root.geometry("600x400+500+100")
    root.update_idletasks()
    # устанавливаем тему "classic"
    ttk.Style().theme_use("clam")
    font1 = font.Font(family="Arial", size=10, weight="bold", slant="roman", underline=True)
    label = Label(text="gui_lottery_generator")
    label.grid(row=0, column=0, padx=10, pady=10)

    button_start = Button(text="Start", command=get_balls, bg="blue", fg="white", font=font1)
    button_start.grid(row=1, column=2, padx=10, pady=10)

    button_start = Button(text="Sort", command=sort_balls, bg="yellow", fg="white", font=font1)
    button_start.grid(row=1, column=3, padx=10, pady=10)

    button_clear = Button(text="Clear", command=clear, bg="green", fg="white", font=font1)
    button_clear.grid(row=1, column=4, padx=10, pady=10)

    button_exiting = Button(text="Exit", command=exiting, bg="red", fg="white", font=font1)
    button_exiting.grid(row=1, column=5, padx=10, pady=10)

    label_choose_ball = ttk.Label(text="choose ball")
    label_choose_ball.grid(row=2, column=0, padx=10, pady=10)

    values_ball = [str(i) for i in range(9)]
    values_var = StringVar(value=values_ball[6])
    combobox_ball = ttk.Combobox(values=values_ball,
                                 justify=CENTER,
                                 width=5,
                                 state="readonly",
                                 textvariable=values_var)
    combobox_ball.grid(row=2, column=1, padx=10, pady=10)
    values_var.get()
    combobox_ball.bind("<<ComboboxSelected>>", get_selected_ball)

    label_choose_all_ball = ttk.Label(text="choose all ball")
    label_choose_all_ball.grid(row=3, column=0, padx=10, pady=10)

    values_all_ball = [str(i) for i in range(55)]
    values_all_var = StringVar(value=values_all_ball[52])
    combobox_all_ball = ttk.Combobox(values=values_all_ball,
                                     justify=CENTER,
                                     width=5,
                                     state="readonly",
                                     textvariable=values_all_var)
    combobox_all_ball.grid(row=3, column=1, padx=10, pady=10)
    combobox_all_ball.bind("<<ComboboxSelected>>", get_selected_all_ball)

    root.mainloop()


while running:
    run()
