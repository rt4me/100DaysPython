import tkinter
# from tkinter import *
# from tkinter import messagebox
from password_gen import PassGen as pg
import json
import logging

WHITE = "#ffffff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s() ] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
    #,filename = 'basic.log'
)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # Clear out whatever is already in the password field
    password_entry.delete(0,END)
    
    new_pass = pg.generate_password()
    password_entry.insert(0, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    
    # Get current values from entry boxes
    website = website_entry.get().lower()
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
        # Try to open file in Read mode first
        try:
            with open('Day29_Password_Manager\\data.json','r') as data_file:
                # Read the existing data from file, if it exists.
                data = json.load(data_file)
        except FileNotFoundError:
            logging.error("Data json file not found. Creating one.")
            with open('Day29_Password_Manager\\data.json','w') as data_file:
                json.dump(new_data, data_file, indent=4)                
        else:
            # Update old data with new data
            data.update(new_data)     
            with open('Day29_Password_Manager\\data.json','w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear out the values in the website and password fields of the UI.
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    
# ---------------------------- SEARCH PASSWORDS ------------------------------- #

def find_password():
    website = website_entry.get().lower() 
    if len(website) == 0:
        messagebox.showerror(title="Empty Website", message="Please enter a value for the Website to search for")
    else:
        try:
            with open('Day29_Password_Manager\\data.json','r') as data_file:
                data = json.load(data_file) # Gets the contents of the file and stores it in a dictionary
        except FileNotFoundError:
            messagebox.showerror(title="No data file", message="No Data File Found")
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f"Email/Username = {email}\nPassword = {password}")
            else:
                messagebox.showerror(title="No match found", message="No details for the website exists.") 
                


    
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
website_entry = Entry(width=27)
website_entry.grid(column=2, row=2)
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
search_button = Button(text="Search", command=find_password,width=14)
search_button.grid(column=3,row=2)


window.mainloop()