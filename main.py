#!/bin/python3

import customtkinter
from tkinter import *
from functools import partial
import os

os.system('clear')

# Ensure paths are absolute
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "assets", "todo.txt")

lightgrey = "#d9d9d9"
offwhite = "#e3e3e3"

customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.geometry("1360x768")
app.title("PYboard")

app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure((1, 1), weight=1)

# Ensure fonts are available, fallback to system default
main_font = "Helvetica"
font2 = "Saturday Sweat"
title_font = "Pinky Blues"
note_size = 45

# Ensure the todo file exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)
if not os.path.exists(file_path):
    with open(file_path, "w"):
        pass

############ TOOLBAR ######################
toolbar = customtkinter.CTkFrame(app, height=200, fg_color=lightgrey, corner_radius=0)
toolbar.grid(row=0,column=0,sticky="we", columnspan="2")

title = Label(toolbar, text="PYboard", padx=30, pady=30, font=(title_font, 20))
title.grid(row=0, column=0, sticky="nw")

####################### LEFT FRAME #####################################
whiteboard = customtkinter.CTkFrame(app, width=1000, height=1000, fg_color=offwhite, corner_radius=0)
whiteboard.grid_rowconfigure((1, 1), weight=1)
whiteboard.grid_columnconfigure((2, 0), weight=1)
whiteboard.pack_propagate(False)
whiteboard.grid(row=1, column=0, sticky="nesw")

###################### RIGHT FRAME #####################################
rightFrame = customtkinter.CTkFrame(app, width=700, fg_color=lightgrey, corner_radius=0)
rightFrame.pack_propagate(False)
rightFrame.grid(row=1, column=1, sticky="nesw")

label = Label(app, text="Add note:", font=(main_font, 16))
label.grid(row=1, column=1, sticky="n", columnspan="2", pady="150", padx=(0, 340))

checkboxes = {}

def create_note(user_input, from_load=False):
    if not user_input.strip():
        return
    existing_notes = {checkbox.cget("text") for checkbox in checkboxes.keys()}
    if user_input in existing_notes:
        return
    if not from_load:
        with open(file_path, 'r') as file:
            if user_input + '\n' in file.readlines():
                return
    if not from_load:
        with open(file_path, 'a') as file:
            file.write(user_input + '\n')

    note_var = BooleanVar()
    new_note = customtkinter.CTkCheckBox(
        whiteboard, text=user_input, font=(font2, note_size), variable=note_var)
    new_note.configure(command=partial(on_checkbox_change, note_var, new_note))
    new_note.pack(side="top", padx=(40, 0), pady=(30, 10), fill="x", anchor="w")

    remove_button = customtkinter.CTkButton(whiteboard, hover_color="red", fg_color=lightgrey,
                                            text="Remove", command=partial(remove_checkbox, new_note))
    remove_button.pack(side="top", padx=(30, 710), pady=(20, 6), anchor="w")

    checkboxes[new_note] = remove_button

def return_key_event(event):
    user_input = entry.get()
    if user_input.strip():
        create_note(user_input)
    entry.delete(0, 'end')

def on_checkbox_change(note_var, new_note):
    new_note.configure(text_color="red" if note_var.get() else "black",
                        font=customtkinter.CTkFont(family=font2, size=note_size, overstrike=note_var.get()))

def remove_checkbox(checkbox):
    checkbox.pack_forget()
    if checkbox in checkboxes:
        checkboxes[checkbox].pack_forget()
        del checkboxes[checkbox]
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() != checkbox.cget("text"):
                file.write(line)

def clear_all_checkboxes():
    for checkbox in list(checkboxes.keys()):
        remove_checkbox(checkbox)
    with open(file_path, 'w') as file:
        pass

entry = customtkinter.CTkEntry(app, fg_color="white", corner_radius=0, placeholder_text="type here...",
                               font=(main_font, 18))
entry.bind('<Return>', return_key_event)
entry.grid(row=1, column=1, sticky="n", columnspan="2", pady="150", ipady=20, ipadx="30")

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            create_note(line.strip())

clear_button = customtkinter.CTkButton(rightFrame, hover_color="red", fg_color="black", text="Clear",
                                       command=clear_all_checkboxes)
clear_button.pack(side="bottom", padx=(30, 30), pady=(20, 390), anchor="n")

def load_notes():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_notes = {line.strip() for line in file if line.strip()}
            for note in existing_notes:
                if note not in {checkbox.cget("text") for checkbox in checkboxes.keys()}:
                    create_note(note, from_load=True)

load_notes()
app.mainloop()

