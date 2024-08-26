#!/home/killian/PYTHON/venv/bin/python3

from tkinter import *
import customtkinter as ctk
from functools import partial

# Initialize the CustomTkinter window
ctk.set_appearance_mode("light")  # Set the appearance mode: "light" or "dark"
ctk.set_default_color_theme("blue")  # Set the default color theme



#class App(ctk.CTk):
    #def __init__(self):
        #super().__init__()

        # Configure window
app = ctk.CTk()
app.title("CustomTkinter Example with Multiple Checkboxes")
app.geometry("300x300")



def on_check(var, checkbox):
    # Change color when the checkbox is selected
    if var.get() == 1:
        checkbox.configure(text_color="red") 
    elif var.get() == 0:
        checkbox.configure(text_color="black")  # Reset to default color

def create_box():
    #checkboxes = {}
    for i in range(4):  # Example with 5 checkboxes
        var = ctk.IntVar(value=0)
        checkbox = ctk.CTkCheckBox(app,
            text=f"Check me {i+1}",
            variable=var)
        checkbox.configure(command=partial(on_check, var, checkbox))
        checkbox.pack(pady=10)
        #checkboxes[f"checkbox_{i+1}"] = var

        # Debugging: Print the state of all checkboxes

create_box()
app.mainloop()

