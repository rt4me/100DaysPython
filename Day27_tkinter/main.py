# Using the below method of importing, you don't have to user tkintet.<method name>
# and instead just use the method name (like Label or Button)
from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Add padding around all elements being draw away from the window edges


# Methods of placing elements in a Window.
#   .pack() is rudimentary method for putting elements in a window
#   .place(x= , y=) is a more detailed method, taking X,Y coordinates to place elements
#   .grid(column= , row=)  - The column/row are relative to each other.
#       So if there is only one element but you specify column = 2 and row = 3,
#       it will still be in the upper left corner, because there are no other elements in relation to it.
# You can't mix and match grid and pack in the same program.


# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# Insert label and place at center bottom of window
# https://docs.python.org/3/library/tkinter.html#the-packer
my_label.grid(column=1, row=1)

# Change the existing label text
my_label["text"] = "New Text"
# or
my_label.config(text="New Text 2")


# Buttons

def button_clicked():
    print("I got clicked")
    # get() gets the value that was placed in the Entry field.
    my_label.config(text=input.get())


button = Button(
    text="Click Me", command=button_clicked)  # Note that this is the name of the function, so no parenthisis needed.
button.grid(column=2, row=2)
# Add padding around just this element in relation to other drawn elements.
# Note that since this is a button, it will make the button itself bigger.
button.config(padx=10, pady=10)

button2 = Button(
    text="I'm the second button"
)
button2.grid(column=3, row=1)


# Entry field

input = Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()
