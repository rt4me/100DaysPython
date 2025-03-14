import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
#Insert label and place at center bottom of window
# https://docs.python.org/3/library/tkinter.html#the-packer
my_label.pack(side = "bottom")








window.mainloop()