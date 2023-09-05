#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
sys.path.append('..')


import tkinter as tk
from center_window import center_window


app = tk.Tk()
app.title("Label Image")
center_window(app)

image = tk.PhotoImage(file='image.png')
label_image = tk.Label(app, image=image)
label_image.pack()

app.mainloop()
