from tkinter import *
from tkinter import ttk
import random
import sys
import time
from tkinter import font

running = True
selected_ball = 6
selected_all_ball = 52


def main():
    def get_selected_ball(event):
        global selected_ball
        selected_ball = int(combobox_ball.get())
        print(selected_ball)

    def get_selected_all_ball(event):
        global selected_all_ball
        selected_all_ball = int(combobox_all_ball.get())
        print(selected_all_ball)

    def get_balls():
        global new_list
        new_list = []
        numbers = list(range(1, selected_all_ball + 1))
        column = 3
        for _ in numbers[:selected_ball]:
            num = random.choice(numbers)
            b = Button(text=f"{num}")
            # print(num, sep='\n')
            b.grid(row=7, column=column, padx=10, pady=10)
            column += 1
            # label_choose_ball.config(text=f"ball: {selected_ball}")
            # label_choose_all_ball.config(text=f"all ball: {selected_all_ball}")
            new_list.append(num)
            numbers.remove(num)
            random.shuffle(numbers)
            root.update()
            time.sleep(1)
        print(new_list)

    def sort_balls():
        list_sort = sorted(new_list)
        column = 3
        for num in list_sort:
            b = Button(text=f"{num}")
            b.grid(row=9, column=column, padx=10, pady=10)
            column += 1
            # label_choose_ball.config(text=f"ball: {selected_ball}")
            # label_choose_all_ball.config(text=f"all ball: {selected_all_ball}")
            root.update()
            time.sleep(1)
        print(list_sort)

    def clear():
        root.destroy()

    def exiting():
        global running
        running = False
        root.destroy()

    root = Tk()
    root.title("gui_lottery_generator")
    # root.iconbitmap(default="favicon.ico")
    root.resizable(False, False)
    root.geometry("600x400+500+100")
    root.update_idletasks()
    # устанавливаем тему "classic"
    ttk.Style().theme_use("clam")
    font1 = font.Font(family="Arial", size=10, weight="bold", slant="roman", underline=True)
    label = Label(text="gui_lottery_generator")
    label.grid(row=0, column=0, padx=10, pady=10)

    button_clear = Button(text="Clear", command=clear, bg="#F4A460", fg="#FFFFFF", font=font1)
    button_clear.grid(row=1, column=0, padx=10, pady=10)

    button_exiting = Button(text="Exit", command=exiting, bg="#8B0000", fg="#FFFFFF", font=font1)
    button_exiting.grid(row=1, column=1, padx=10, pady=10)

    label_choose_ball = ttk.Label(text="ball")
    label_choose_ball.grid(row=2, column=0, padx=10, pady=10)

    values_ball = [str(i) for i in range(9)]
    values_var = StringVar(value=str(selected_ball))
    combobox_ball = ttk.Combobox(values=values_ball,
                                 justify=CENTER,
                                 width=5,
                                 state="readonly",
                                 textvariable=values_var)
    combobox_ball.grid(row=2, column=1, padx=10, pady=10)
    values_var.get()
    combobox_ball.bind("<<ComboboxSelected>>", get_selected_ball)

    label_choose_all_ball = ttk.Label(text="all ball")
    label_choose_all_ball.grid(row=3, column=0, padx=10, pady=10)

    button_start = Button(text="Start", command=get_balls, bg="#008000", fg="#FFFFFF", font=font1)
    button_start.grid(row=5, column=0, padx=10, pady=10)

    button_start = Button(text="Sort", command=sort_balls, bg="#1E90FF", fg="#FFFFFF", font=font1)
    button_start.grid(row=5, column=1, padx=10, pady=10)

    values_all_ball = [str(i) for i in range(55)]
    values_all_var = StringVar(value=str(selected_all_ball))
    combobox_all_ball = ttk.Combobox(values=values_all_ball,
                                     justify=CENTER,
                                     width=5,
                                     state="readonly",
                                     textvariable=values_all_var)
    combobox_all_ball.grid(row=3, column=1, padx=10, pady=10)
    combobox_all_ball.bind("<<ComboboxSelected>>", get_selected_all_ball)
    print(selected_ball)
    print(selected_all_ball)
    root.mainloop()


if __name__ == '__main__':
    while running:
        main()
