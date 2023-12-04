__author__ = 'VadimTrubay'

from tkinter import *
from tkinter import ttk
import random
import sys
import time
from tkinter import font
from tkinter.messagebox import showinfo, askyesno


running = True
selected_ball = 6
selected_all_ball = 52


def main():
    def try_again():
        # Ask the user if they want to run again
        response = askyesno("Generate Again", "Do you want to generate again?")
        if response:
            return True
        else:
            return False

    def get_selected_ball(event):
        global selected_ball
        selected_ball = int(combobox_ball.get())
        print(selected_ball)


    def get_selected_all_ball(event):
        global selected_all_ball
        selected_all_ball = int(combobox_all_ball.get())
        print(selected_all_ball)


    def get_balls():
        answer = try_again()
        if answer:
            global new_list
            new_list = []
            numbers = list(range(1, selected_all_ball + 1))
            column = 0
            label = Label(text="random", font=('Arial', 10, 'bold'), fg='#996600')
            label.grid(row=7, column=0, padx=10, pady=10)
            for _ in numbers[:selected_ball]:
                num = random.choice(numbers)
                b = Button(text=f"{num}", bd=2, font=('Arial', 20, 'bold'), fg='#446655', width=3, height=1)
                b.grid(row=8, column=column, padx=5, pady=5)
                column += 1
                new_list.append(num)
                numbers.remove(num)
                random.shuffle(numbers)
                root.update()
                time.sleep(1)

    def sort_balls():
        new_list.sort()
        column = 0
        label = Label(text="sort", font=('Arial', 10, 'bold'), fg='#996600')
        label.grid(row=9, column=0, padx=10, pady=10)
        for num in new_list:
            b = Button(text=f"{num}", bd=2, font=('Arial', 20, 'bold'), fg='#006655', width=3, height=1)
            b.grid(row=10, column=column, padx=5, pady=5)
            column += 1
            root.update()
            time.sleep(1)


    def clear():
        root.destroy()


    def exiting():
        global running
        running = False
        root.destroy()

    root = Tk()
    root.title("lottery_tkinter")
    # root.iconbitmap(default="favicon.ico")
    root.resizable(False, False)
    root.geometry("600x400+300+100")
    root.update_idletasks()
    # устанавливаем тему "classic"
    ttk.Style().theme_use("clam")

    label = Label(text="lottery")
    label.grid(row=0, column=0, padx=10, pady=10)

    button_start = Button(text="Start", command=get_balls, bd=5, font=('Arial', 10, 'bold'), fg='green')
    button_start.grid(row=1, column=0, padx=10, pady=10)

    button_start = Button(text=" Sort ", command=sort_balls, bd=5, font=('Arial', 10, 'bold'), fg='#774400')
    button_start.grid(row=1, column=1, padx=10, pady=10)

    button_clear = Button(text="Clear", command=clear, bd=5, font=('Arial', 10, 'bold'), fg='blue')
    button_clear.grid(row=1, column=2, padx=10, pady=10)

    button_exiting = Button(text=" Exit ", command=exiting, bd=5, font=('Arial', 10, 'bold'), fg='red')
    button_exiting.grid(row=1, column=3, padx=10, pady=10)

    label_choose_ball = ttk.Label(text="ball", font=('Arial', 10, 'bold'))
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

    label_choose_all_ball = ttk.Label(text="all ball", font=('Arial', 10, 'bold'))
    label_choose_all_ball.grid(row=2, column=2, padx=10, pady=10)

    values_all_ball = [str(i) for i in range(55)]
    values_all_var = StringVar(value=str(selected_all_ball))
    combobox_all_ball = ttk.Combobox(values=values_all_ball,
                                     justify=CENTER,
                                     width=5,
                                     state="readonly",
                                     textvariable=values_all_var)
    combobox_all_ball.grid(row=2, column=3, padx=10, pady=10)
    combobox_all_ball.bind("<<ComboboxSelected>>", get_selected_all_ball)

    root.mainloop()


if __name__ == '__main__':
    while running:
        main()
