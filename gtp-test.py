#!/bin/python3

import customtkinter as ctk
import os

TODO_FILE = "todo.txt"

def load_tasks():
    """Load tasks from file and create checkboxes."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            for line in f:
                task, status = line.strip().rsplit("::", 1)
                create_task(task, status == "1")

def create_task(task_text, checked=False):
    """Create a checkbox for a task."""
    var = ctk.StringVar(value="1" if checked else "0")
    checkbox = ctk.CTkCheckBox(frame, text=task_text, variable=var, command=save_tasks, onvalue="1", offvalue="0")
    checkbox.pack(anchor="w", padx=10, pady=2)
    task_list.append((checkbox, var))

def add_task():
    """Add a new task from the entry box."""
    task_text = entry.get().strip()
    if task_text:
        create_task(task_text, False)
        entry.delete(0, "end")
        save_tasks()

def save_tasks():
    """Save tasks to file."""
    with open(TODO_FILE, "w") as f:
        for checkbox, var in task_list:
            f.write(f"{checkbox.cget('text')}::{var.get()}\n")

# Initialize the app
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Whiteboard To-Do List")
app.geometry("400x500")
app.configure(bg="white")

task_list = []

frame = ctk.CTkFrame(app, fg_color="white")
frame.pack(pady=10, padx=10, fill="both", expand=True)

load_tasks()

entry = ctk.CTkEntry(app, placeholder_text="New task...", width=280)
entry.pack(pady=5)

add_button = ctk.CTkButton(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

app.mainloop()

