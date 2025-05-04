from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=30, pady=30)


def convert_mi_to_km():
    km_value = int(float(entry.get()) * 1.609)
    result_label.config(text=f"{km_value}")


# Miles entry box
entry = Entry(width=10)
entry.grid(column=2, row=1)

# text labels
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=2)
km_label = Label(text="Km")
km_label.grid(column=3, row=2)
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)
result_label = Label(text="0")
result_label.grid(column=2, row=2)

# Calculate button
button = Button(text="Calculate", command=convert_mi_to_km)
button.grid(column=2, row=3)


window.mainloop()