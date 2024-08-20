#!/home/killian/PYTHON/venv/bin/python3

import customtkinter
from tkinter import *


lightgrey = "#d9d9d9"
offwhite = "#e3e3e3"

customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.geometry("1360x768")
app.title("PYboard")

main_font = "Helvetica"

app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure((1, 1), weight=1)


############ TOOLBAR ######################
# My toolbar up at the top
toolbar = customtkinter.CTkFrame(app, height=200, fg_color=lightgrey, corner_radius=0)
toolbar.grid(row=0,column=0,sticky="we", columnspan="2")

# PYboard title
title = Label(toolbar, text="PYboard", padx=30, pady=30, font=(main_font, 16))
title.grid(row=0, column=0, sticky="nw")


####################### LEFT FRAME #####################################

# Left side of the window. Text should end up in here
whiteboard = customtkinter.CTkFrame(app, width=1000, height=1000, fg_color=offwhite, corner_radius=0)

# Stops the window from shrinking after adding a note (widget)
whiteboard.pack_propagate(False)
whiteboard.grid(row=1, column=0, sticky="nesw")


###################### RIGHT FRAME #####################################
# Right side of the window. User can Input text over here 
rightFrame = customtkinter.CTkFrame(app, width=800, fg_color=lightgrey, corner_radius=0)
rightFrame.grid(row=1, column=1, sticky="nesw")

# 'Add note' label before entry field
label = Label(app, text="Add note:", font=(main_font, 16))
label.grid(row=1, column=1, sticky="n", columnspan="2", pady="150", padx=(0, 340))



################## RETURN KEY EVENT FUCTION ####################################

new_note = ""

# Clears text after pressing enter

def return_key_event(event):
    user_input = entry.get()
    
    # Deletes old input
    entry.delete(0, 'end')

    global new_note
    global state

    # Add a new note
    new_note = customtkinter.CTkCheckBox(
    whiteboard, 
    text=user_input, 
    onvalue="on", 
    offvalue="off", 
    font=("Comic Sans", 20))
    
    new_note.pack(side="top", padx=(40, 0), pady=(18, 12), fill="x")

########################################




# Entry for user input
entry = customtkinter.CTkEntry(
    app, 
    fg_color="white", 
    corner_radius=0, 
    placeholder_text="type here...",
    font=(main_font, 18))

entry.bind('<Return>', return_key_event)
entry.grid(row=1, column=1, sticky="n", columnspan="2", pady="150", ipady=20, ipadx="30")






app.mainloop()
