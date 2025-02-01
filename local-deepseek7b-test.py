#!/bin/python3

import tkinter as tk
from tkinter import ttk


def set_checkbutton_text(checkbox, text):
    checkbox['text'] = text


def destroy_checkbutton(checkbox):
    checkbox['text'] = ""
    checkbox['value'].set("")
    checkbox['command'] = None
    checkbox['state'] = "disabled"


def set_checkbutton_command(checkbox, command_func):
    checkbox['command'] = command_func


def toggle_checkboxes():
    global selected_checkboxes, checkboxes_list, whiteboard_text

    for checkbox in checkbox_list:
        if (
            checkbox.get() == ""
            and not bool(checkbox.get())
            and len(checkbox['value']) > 0
        ):
            checkbox_list.append(checkbox)

    whiteboard_text.delete("1.0", tk.END)
    for item in checkbox_list:
        text = f"{item['text']}: {item['value'].get()}\n"
        if text.strip():
            whiteboard_text.insert(tk.END, text.strip())
    
    selected_checkboxes.clear()


def clear_selection():
    global checkboxes_list
    for checkbox in checkbox_list:
        destroy_checkbutton(checkbox)
    checkboxes_list = []
    clear_button["state"] = "disabled"


def create_checkbutton(text, value, command_func=None):
    var = ttk.Button(root, text=text, width=10)

    def set_value():
        nonlocal text
        if value is not None:
            var['text'] = text
        else:
            var['text'] = ""
        var['value'].set("")
    
    var['command'] = command_func or lambda: None

    def destroy():
        var['text'] = ""
        var['value'].set("")
        var['command'] = None
        var['state'] = "disabled"

    if value is not None:
        var['text'] = text
    
    var.pack(side=tk.LEFT)

    return var


def create_text_area():
    global whiteboard_text
    whiteboard_text = ttk.Text(
        root,
        wrap=tk.WORD,
        font=tk.font.Font(family='Arial', weight='bold')
    )
    
    def disable_yscroll():
        whiteboard_text['yscrollcommand'] = None
    
    whiteboard_text['yscrollcommand'] = disable_yscroll
    whiteboard_text.pack(side=tk.LEFT)


def main():
    root = tk.Tk()
    root.title("Digital Whiteboard")

    def create_frame(label, command_func=None):
        frame = tk.LabelFrame(root, text=label)
        if command_func is not None:
            frame.bind("<Button-1>", lambda e: command_func())
        return frame


    frame_left = create_frame("Checkbox List")
    frame_right = create_frame("Whiteboard")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frame_left.pack(row=0, column=0, sticky='ew')
    frame_right.pack(row=0, column=1, sticky='ew')

    whiteboard_text = create_text_area()

    checkboxes = [
        ("Header", "Select from the left"),
        ("List Item 1", "Enter text here"),
        ("List Item 2", "Enter more text here"),
        ("List Item 3", "Click to add")
    ]

    for checkbox_text, initial_value in checkboxes:
        create_checkbutton(checkbox_text, value=initial_value)

    clear_button = ttk.Button(root, text="Clear All", command=lambda: destroy_checkbutton(clear_button))
    frame_left.create('Clear', clear_button)

    root.mainloop()

