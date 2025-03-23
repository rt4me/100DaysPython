# Using the below method of importing, you don't have to user tkintet.<method name>
# and instead just use the method name (like Label or Button)
from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# Insert label and place at center bottom of window
# https://docs.python.org/3/library/tkinter.html#the-packer
my_label.pack()  # pack is needed to place element on screen

# Change the existing label text
my_label["text"] = "New Text"
# or
my_label.config(text="New Text 2")


# Button


def button_clicked():
    print("I got clicked")
    # get() gets the value that was placed in the Entry field.
    my_label.config(text=input.get())


button = Button(
    text="Click Me", command=button_clicked)  # Note that this is the name of the function, so no parenthisis needed.
button.pack()


# Entry field
input = Entry(width=10)
input.pack()


window.mainloop()
