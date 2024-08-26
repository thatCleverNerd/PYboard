#!/home/killian/PYTHON/venv/bin/python3

import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.geometry("1360x768")
app.title("PYboard")

# centers my button
app.grid_columnconfigure((0, 3), weight=1)

button = customtkinter.CTkButton(app, text='Click Me :)', command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan="4")

checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")



app.mainloop()
