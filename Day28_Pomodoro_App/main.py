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
timer = None
REPS = 1
check_count = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    global check_count
    
    REPS = 1
    check_count = ""
    check_mark_label.config(text=check_count)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text = "0:00")
    # Stops the running timer
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
        
          
    REPS += 1

    #count_down(start_min * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_count
    global timer
    count_min = count // 60
    count_sec = count % 60

# window.after is code built into tkinter to handle looking for input from the user and keeping track of time.
# The example below is waiting 1000ms (1 sec)/ After 1 second it calls count_down module to subtract 1 second from timer.
# itemconfig changes the value of timer_text variable
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        # made into a variable so it be cancelled when the Reset button is used.
        timer = window.after(1000,count_down, count - 1)
    else:
        if REPS % 2 == 0:
            check_count += "✔"
            check_mark_label.config(text=check_count)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas allows layering of elements
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file="Day28_Pomodoro_app\\tomato.png")
# Image location tweaked to not cut off image edge
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


title_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=2, row=1)


check_mark_label = Label(fg=GREEN, bg=YELLOW, font = (FONT_NAME, 18, "bold"))
check_mark_label.grid(column=2, row=4)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row = 3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)






window.mainloop()