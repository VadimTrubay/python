__author__ = 'VadimTrubay'

from datetime import datetime
import random
import sys
import time
from tkinter import font
from tkinter.messagebox import showinfo, askyesno
from tkinter import *
from tkinter import ttk


running = True
selected_ball = 6
selected_all_ball = 52
selected_year = 2023
selected_month = 6
selected_day = 15
selected_hour = 21
selected_minut = 0
selected_second = 0


def main():

    def try_again():
        # Ask the user if they want to run again
        response = askyesno("Generate Again", "Do you want to generate?")
        if response:
            return True
        else:
            return False


    def get_selected_year(event):
        global selected_year
        selected_year = int(combobox_year.get())


    def get_selected_month(event):
        global selected_month
        selected_month = int(combobox_month.get())


    def get_selected_day(event):
        global selected_day
        selected_day = int(combobox_day.get())


    def get_selected_hour(event):
        global selected_hour
        selected_hour = int(combobox_hour.get())


    def get_selected_minut(event):
        global selected_minut
        selected_minut = int(combobox_minut.get())


    def get_selected_second(event):
        global selected_second
        selected_second = int(combobox_second.get())


    def get_selected_ball(event):
        global selected_ball
        selected_ball = int(combobox_ball.get())


    def get_selected_all_ball(event):
        global selected_all_ball
        selected_all_ball = int(combobox_all_ball.get())


    def get_balls():
        answer = try_again()
        if answer:
            global new_list
            new_list = []
            numbers = list(range(1, selected_all_ball + 1))
            column = 0

            for _ in numbers[:selected_ball]:
                random.seed(my_seed)
                num = random.choice(numbers)
                b = Button(text=f"{num}", bd=2, font=('Arial', 15, 'bold'), fg='#002222', width=3, height=1)
                b.grid(row=11, column=column, padx=5, pady=10)
                column += 1
                new_list.append(num)
                numbers.remove(num)
                random.shuffle(numbers)
                root.update()
                time.sleep(1)

    def sort_balls():
        new_list.sort()
        column = 0

        for num in new_list:
            b = Button(text=f"{num}", bd=2, font=('Arial', 15, 'bold'), fg='#002222', width=3, height=1)
            b.grid(row=13, column=column, padx=5, pady=10)
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

    my_seed = datetime(year=selected_year, month=selected_month, day=selected_day, hour=selected_hour, minute=selected_minut, second=selected_second).timestamp()

    label = Label(text="", font=('Arial', 10, 'bold'))
    label.grid(row=0, column=0)

    # year
    label_choose_year = ttk.Label(text="year", font=('Arial', 10, 'bold'))
    label_choose_year.grid(row=2, column=0, padx=10)

    values_year = [str(i) for i in range(2010, 2030)]
    year = StringVar(value=str(selected_year))
    combobox_year = ttk.Combobox(values=values_year,
                                 justify=CENTER,
                                 width=4,
                                 state="readonly",
                                 textvariable=year)
    combobox_year.grid(row=3, column=0, padx=10)
    year.get()
    combobox_year.bind("<<ComboboxSelected>>", get_selected_year)


    # month
    label_choose_month = ttk.Label(text="month", font=('Arial', 10, 'bold'))
    label_choose_month.grid(row=2, column=1, padx=10)

    values_month = [str(i) for i in range(1, 13)]
    month = StringVar(value=str(selected_month))
    combobox_month = ttk.Combobox(values=values_month,
                                 justify=CENTER,
                                 width=4,
                                 state="readonly",
                                 textvariable=month)
    combobox_month.grid(row=3, column=1, padx=10)
    month.get()
    combobox_month.bind("<<ComboboxSelected>>", get_selected_month)


    # day
    label_choose_day = ttk.Label(text="day", font=('Arial', 10, 'bold'))
    label_choose_day.grid(row=2, column=2, padx=10)

    values_day = [str(i) for i in range(1, 32)]
    day = StringVar(value=str(selected_day))
    combobox_day = ttk.Combobox(values=values_day,
                                 justify=CENTER,
                                 width=4,
                                 state="readonly",
                                 textvariable=day)
    combobox_day.grid(row=3, column=2, padx=10)
    day.get()
    combobox_day.bind("<<ComboboxSelected>>", get_selected_day)

    # hour
    label_choose_hour = ttk.Label(text="hour", font=('Arial', 10, 'bold'))
    label_choose_hour.grid(row=2, column=3, padx=10)

    values_hour = [str(i) for i in range(1, 25)]
    hour = StringVar(value=str(selected_hour))
    combobox_hour = ttk.Combobox(values=values_hour,
                                 justify=CENTER,
                                 width=4,
                                 state="readonly",
                                 textvariable=hour)
    combobox_hour.grid(row=3, column=3, padx=10)
    hour.get()
    combobox_hour.bind("<<ComboboxSelected>>", get_selected_hour)


    # minut
    label_choose_minut = ttk.Label(text="min ", font=('Arial', 10, 'bold'))
    label_choose_minut.grid(row=2, column=4, padx=10)

    values_minut = [str(i) for i in range(0, 61)]
    minut = StringVar(value=str(selected_minut))
    combobox_minut = ttk.Combobox(values=values_minut,
                                 justify=CENTER,
                                 width=4,
                                 state="readonly",
                                 textvariable=minut)
    combobox_minut.grid(row=3, column=4, padx=10)
    minut.get()
    combobox_minut.bind("<<ComboboxSelected>>", get_selected_minut)


    # second
    label_choose_second = ttk.Label(text="sec ", font=('Arial', 10, 'bold'))
    label_choose_second.grid(row=2, column=5, padx=10)

    values_second = [str(i) for i in range(0, 61)]
    second = StringVar(value=str(selected_second))
    combobox_second = ttk.Combobox(values=values_second,
                                 justify=CENTER,
                                 width=4,
                                 state="readonly",
                                 textvariable=second)
    combobox_second.grid(row=3, column=5, padx=10)
    second.get()
    combobox_second.bind("<<ComboboxSelected>>", get_selected_second)


    button_seed = Button(text="Enter seed", command=clear, bd=5, font=('Arial', 10, 'bold'), fg='#000000')
    button_seed.grid(row=3, column=6)

    label = Label(text="", font=('Arial', 10, 'bold'))
    label.grid(row=4, column=0)

    label_choose_ball = ttk.Label(text="ball", font=('Arial', 10, 'bold'))
    label_choose_ball.grid(row=5, column=0, padx=10)

    values_ball = [str(i) for i in range(9)]
    values_var = StringVar(value=str(selected_ball))
    combobox_ball = ttk.Combobox(values=values_ball,
                                 justify=CENTER,
                                 width=4,
                                 state="readonly",
                                 textvariable=values_var)
    combobox_ball.grid(row=6, column=0, padx=10)
    values_var.get()
    combobox_ball.bind("<<ComboboxSelected>>", get_selected_ball)

    label_choose_all_ball = ttk.Label(text="all ball", font=('Arial', 10, 'bold'))
    label_choose_all_ball.grid(row=5, column=1, padx=10)

    values_all_ball = [str(i) for i in range(55)]
    values_all_var = StringVar(value=str(selected_all_ball))
    combobox_all_ball = ttk.Combobox(values=values_all_ball,
                                     justify=CENTER,
                                     width=4,
                                     state="readonly",
                                     textvariable=values_all_var)
    combobox_all_ball.grid(row=6, column=1, padx=10)
    combobox_all_ball.bind("<<ComboboxSelected>>", get_selected_all_ball)


    button_ball = Button(text="Enter ball", command=clear, bd=5, font=('Arial', 10, 'bold'), fg='#000000')
    button_ball.grid(row=6, column=6)


    button_start = Button(text="Start", command=get_balls, bd=5, font=('Arial', 10, 'bold'), fg='green')
    button_start.grid(row=8, column=0, pady=10)

    button_start = Button(text=" Sort ", command=sort_balls, bd=5, font=('Arial', 10, 'bold'), fg='#774400')
    button_start.grid(row=8, column=1, pady=10)

    button_clear = Button(text="Clear", command=clear, bd=5, font=('Arial', 10, 'bold'), fg='blue')
    button_clear.grid(row=8, column=2, pady=10)

    button_exiting = Button(text=" Exit ", command=exiting, bd=5, font=('Arial', 10, 'bold'), fg='red')
    button_exiting.grid(row=8, column=3, pady=10)

    root.mainloop()


if __name__ == '__main__':
    while running:
        main()
