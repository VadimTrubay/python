from tkinter import *
from tkinter import ttk
import random
import sys
import time

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
        column = 1
        for _ in numbers[:selected_ball]:
            num = random.choice(numbers)
            b = Button(text=f"{num}")
            b.grid(row=7, column=column, padx=10, pady=10)
            column += 1
            label_choose_ball.config(text=f"choose ball: {selected_ball}")
            label_choose_all_ball.config(text=f"choose all ball: {selected_all_ball}")
            numbers.remove(num)
            random.shuffle(numbers)
            print(numbers)
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
    root.geometry("400x400+500+100")
    root.update_idletasks()
    # устанавливаем тему "classic"
    ttk.Style().theme_use("clam")

    label = Label(text="gui_lottery_generator", justify=CENTER)
    label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    button_clear = Button(text="Clear", command=clear)
    button_clear.grid(row=0, column=5, padx=10, pady=10)

    button_exiting = Button(text="Exit", command=exiting)
    button_exiting.grid(row=0, column=6, padx=10, pady=10)

    label_choose_ball = ttk.Label(text="choose ball")
    label_choose_ball.grid(row=2, column=3, padx=10, pady=10)

    combobox_ball = ttk.Combobox(values=[str(i) for i in range(13)],
                                 justify=CENTER, width=5, state="readonly")
    combobox_ball.grid(row=3, column=3, padx=10, pady=10)
    combobox_ball.bind("<<ComboboxSelected>>", get_selected_ball)

    label_choose_all_ball = ttk.Label(text="choose all ball")
    label_choose_all_ball.grid(row=2, column=6, padx=10, pady=10)

    combobox_all_ball = ttk.Combobox(values=[str(i) for i in range(66)],
                                     justify=CENTER, width=5, state="readonly")
    combobox_all_ball.grid(row=3, column=6, padx=10, pady=10)
    combobox_all_ball.bind("<<ComboboxSelected>>", get_selected_all_ball)

    button_start = Button(text="Start", command=get_balls)
    button_start.grid(row=6, column=6, columnspan=4, padx=10, pady=10)

    root.mainloop()


while running:
    run()
