from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        window.after(1000,count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas allows layering of elements
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file="Day28_Pomodoro_app\\tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


title_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=2, row=1)

check_mark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font = (FONT_NAME, 18, "bold"))
check_mark_label.grid(column=2, row=4)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row = 3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)






window.mainloop()