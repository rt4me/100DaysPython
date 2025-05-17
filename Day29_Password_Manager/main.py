import tkinter
# from tkinter import *
# from tkinter import messagebox
from password_gen import PassGen as pg
import json

WHITE = "#ffffff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # Clear out whatever is already in the password field
    password_entry.delete(0,END)
    
    new_pass = pg.generate_password()
    password_entry.insert(0, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    
    # Get current values from entry boxes
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {"email": email,
                  "password": password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!", )
    else: 
        with open('Day29_Password_Manager\\data.json','w') as f:
            json.dump(new_data, f)
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
# Have to include the directory below because the Python's current working directory is 100DAYSPYTHON, not Day29_Password_Manager.
logo_image = PhotoImage(file="Day29_Password_Manager\\logo.png")
# To get the image centered, position is 1/2 the total distance of the canvas
canvas.create_image(100, 100, image=logo_image)
# canvas.grid() or pack() are required for the image to actually be displayed in the canvas.
canvas.grid(column=2, row=1)

# Labels
website_label = Label(text="Website: ",font=(FONT_NAME,12,),)
website_label.grid(column=1, row=2)
email_un_label = Label(text="Email/Username: ", font=(FONT_NAME, 12,),)
email_un_label.grid(column=1, row=3)
password_label = Label(text="Password: ", font=(FONT_NAME, 12,),)
password_label.grid(column=1, row=4)

# Text entry boxes
website_entry = Entry(width=45)
website_entry.grid(column=2, row=2, columnspan=2)
# Place cursor in this box by default
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(column=2, row=3, columnspan=2)
# Pre-populate email field with an email address. 0 represents the beginning of the field.
email_entry.insert(0, 'tim.bergin@gmail.com')
password_entry = Entry(width=27)
password_entry.grid(column=2, row=4)

# Buttons
genpass_button = Button(text="Generate Password", command=generate_pass)
genpass_button.grid(column=3, row=4)
add_button = Button(text="Add", width=40, command=add_password)
add_button.grid(column=2, row=5, columnspan=2)


window.mainloop()