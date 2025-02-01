#!/bin/python3

import customtkinter as ctk
from customtkinter import CTkScrollableFrame
import os

# Constants
TODO_FILE = "todo.txt"

# Functions
def load_tasks():
    """Load tasks from file and create checkboxes."""
    try:
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, "r") as f:
                for line in f:
                    task, status = line.strip().rsplit("::", 1)
                    create_task(task, status == "1")
    except Exception as e:
        print(f"Error loading tasks: {e}")

def create_task(task_text, checked=False):
    """Create a checkbox and delete button for a task."""
    var = ctk.StringVar(value="1" if checked else "0")
    task_frame = ctk.CTkFrame(left_frame, fg_color="white")
    task_frame.pack(anchor="w", padx=10, pady=2, fill="x")

    checkbox = ctk.CTkCheckBox(task_frame, text=task_text, variable=var, command=save_tasks, onvalue="1", offvalue="0")
    checkbox.pack(side="left", padx=(0, 10))

    delete_button = ctk.CTkButton(task_frame, text="Delete", width=50, command=lambda: delete_task(checkbox))
    delete_button.pack(side="right")

    task_list.append((checkbox, var))

def add_task():
    """Add a new task from the entry box."""
    task_text = entry.get().strip()
    if task_text:
        if "::" in task_text:
            print("Error: Task text cannot contain '::'")
        else:
            create_task(task_text, False)
            entry.delete(0, "end")
            save_tasks()

def delete_task(task_widget):
    """Delete a specific task."""
    for task in task_list:
        if task[0] == task_widget:
            task[0].destroy()
            task_list.remove(task)
            break
    save_tasks()

def save_tasks():
    """Save tasks to file."""
    try:
        with open(TODO_FILE, "w") as f:
            for checkbox, var in task_list:
                f.write(f"{checkbox.cget('text')}::{var.get()}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Initialize the app
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Digital Whiteboard")
app.geometry("800x500")
app.configure(bg="white")

# Task list to store checkboxes and their variables
task_list = []

# Left Side: Scrollable task list
left_frame = CTkScrollableFrame(app, fg_color="white", width=400)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Right Side: Input section
right_frame = ctk.CTkFrame(app, fg_color="white", width=300)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

# Input field
entry = ctk.CTkEntry(right_frame, placeholder_text="New task...", width=250)
entry.pack(pady=20)

# Add task button
add_button = ctk.CTkButton(right_frame, text="Add Task", command=add_task, width=250)
add_button.pack(pady=10)

# Load tasks from file
load_tasks()

# Run the app
app.mainloop()

