#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

def callback(number):
    print(number)

ttk.Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
ttk.Button(root, text='Click Me 2', command = lambda: callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()


root.mainloop()
