#!/home/killian/PYTHON/venv/bin/python3

import customtkinter

customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.geometry("1360x768")
app.title("PYboard")

# centers my button
app.grid_columnconfigure((0, 1), weight=1)


app.frame = customtkinter.CTkFrame(app, fg_color="grey")
app.frame.grid(row=0, column=0, padx=0, pady=(0, 0), sticky="nesw", columnspan="2")


app.mainloop()
