#!/home/killian/PYTHON/venv/bin/python3

import customtkinter
from tkinter import *

# Initialize a window
root = Tk()
root.geometry("1360x768")

# creating a Fra, e which can expand according
# to the size of the window
pane = Frame(root)
pane.pack(fill = BOTH)

# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text = "Click me !", background = "blue")
b1.pack(fill = BOTH, expand = True)
 
root.mainloop()

