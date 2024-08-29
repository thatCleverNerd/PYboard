#!/home/killian/PYTHON/venv/bin/python3

import customtkinter
from tkinter import *
from functools import partial
import os

os.system('clear')


#\/\/\/\\/\/\/\\/\/\/\/\/\/\/\\/\/\/\/\/\\/\/

lightgrey = "#d9d9d9"
offwhite = "#e3e3e3"

customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.geometry("1360x768")
app.title("PYboard")

app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure((1, 1), weight=1)

main_font = "Helvetica"
font2 = "Saturday Sweat"
title_font = "Pinky Blues"
note_size = 45

file_path = os.path.expanduser("~/todo.txt")

#\/\/\\/\/\\\\\\\\\\\\\\/\\/\/\\/\/\\\\\\\/\/\\/

if os.path.exists(file_path):
    pass
else:
    with open(file_path, "w"):
        pass


############ TOOLBAR ######################
# My toolbar up at the top
toolbar = customtkinter.CTkFrame(app, height=200, fg_color=lightgrey, corner_radius=0)
toolbar.grid(row=0,column=0,sticky="we", columnspan="2")

title = Label(toolbar, text="PYboard", padx=30, pady=30, font=(title_font, 20))
title.grid(row=0, column=0, sticky="nw")


####################### LEFT FRAME #####################################

# Left side of the window. Text should end up in here
whiteboard = customtkinter.CTkFrame(app, width=1000, height=1000, fg_color=offwhite, corner_radius=0)
whiteboard.grid_rowconfigure((1, 1), weight=1)
whiteboard.grid_columnconfigure((2, 0), weight=1)

# Stops the window from shrinking after adding a note (widget)
whiteboard.pack_propagate(False)
whiteboard.grid(row=1, column=0, sticky="nesw")


###################### RIGHT FRAME #####################################
# Right side of the window. User can Input text over here 
rightFrame = customtkinter.CTkFrame(app, width=700, fg_color=lightgrey, corner_radius=0)
rightFrame.pack_propagate(False)
rightFrame.grid(row=1, column=1, sticky="nesw")

# 'Add note' label before entry field
label = Label(app, text="Add note:", font=(main_font, 16))
label.grid(row=1, column=1, sticky="n", columnspan="2", pady="150", padx=(0, 340))


##################### CREATE NOTE ##############################

checkboxes = {}

def create_note(user_input):
    if not user_input.strip():
        return  # Skip if input is empty

    # Prevent duplicate notes
    existing_notes = {checkbox.cget("text") for checkbox in checkboxes.keys()}
    if user_input in existing_notes:
        return  # Skip if note already exists

    # Clears text when this function is called
    note_var = BooleanVar()
    new_note = customtkinter.CTkCheckBox(
        whiteboard,
        text=user_input,
        font=(font2, note_size),
        variable=note_var)
    new_note.configure(command=partial(on_checkbox_change, note_var, new_note))
    new_note.pack(side="top", padx=(40, 0), pady=(30, 10), fill="x", anchor="w")


    with open(file_path, 'a') as file:
        file.write(user_input + '\n')


    ############# 'REMOVE' BUTTON ##################
    # Add a remove button for each checkbox
    remove_button = customtkinter.CTkButton(whiteboard,
        hover_color="red",
        fg_color=lightgrey,
        text="Remove",
        command=partial(remove_checkbox, new_note))

    remove_button.pack(side="top", padx=(30, 710), pady=(20, 6), anchor="w")


    # Store the checkbox reference
    checkboxes[new_note] = remove_button

################## RETURN KEY EVENT ####################################

def return_key_event(event):
    user_input = entry.get()
    if user_input.strip():
        create_note(user_input)  
    entry.delete(0, 'end')



def on_checkbox_change(note_var, new_note):
    if note_var.get() == 1:
        crossed_out_font = customtkinter.CTkFont(family=font2, size=note_size, overstrike=True)
        new_note.configure(text_color="red", font=crossed_out_font)

    elif note_var.get() == 0:
        original_font = customtkinter.CTkFont(family=font2, size=note_size, overstrike=False)
        new_note.configure(text_color="black", font=original_font)


def remove_checkbox(checkbox):
    # Remove the checkbox and associated remove button
    checkbox.pack_forget()
    if checkbox in checkboxes:
        checkboxes[checkbox].pack_forget()
        del checkboxes[checkbox]

    # Remove the note from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() != checkbox.cget("text"):
                file.write(line)


def clear_all_checkboxes():
    # Clear all checkboxes and their remove buttons
    for checkbox in list(checkboxes.keys()):
        remove_checkbox(checkbox)

    # Clear the file
    with open(file_path, 'w') as file:
        pass  # Simply opening the file in write mode clears its content


################## USER INPUT ######################

# Entry for user input
entry = customtkinter.CTkEntry(
    app, 
    fg_color="white", 
    corner_radius=0, 
    placeholder_text="type here...",
    font=(main_font, 18))

entry.bind('<Return>', return_key_event)
entry.grid(row=1, column=1, sticky="n", columnspan="2", pady="150", ipady=20, ipadx="30")

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            user_input = line.strip()
            if user_input:
                create_note(user_input) 


#################### CLEARS ALL TEXT ##################################
clear_button = customtkinter.CTkButton(rightFrame,
        hover_color="red",
        fg_color="black",
        text="Clear",
        command=clear_all_checkboxes)

clear_button.pack(side="bottom", padx=(30, 30), pady=(20, 390), anchor="n")

##############################################
def load_notes():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_notes = {line.strip() for line in file if line.strip()}
            for note in existing_notes:
                if note not in {checkbox.cget("text") for checkbox in checkboxes.keys()}:
                    create_note(note)  # Create a new note if it doesn't already exist

# Call this function to load notes when the app starts
load_notes()

app.mainloop()
