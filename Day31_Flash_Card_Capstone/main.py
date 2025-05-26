from tkinter import *
from tkinter import messagebox
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

# french_words.csv is the main list of study words.
# words_to_learn.csv is the list of words the user needs to work on.
# If words_to_learn.csv doesn't exist, read information from french_words.csv, create a words_to_learn.csv containing all the information from the french_words.csv.
# when using the application, if the user knows the french to english pair, they will select the Correct button, which will remove the word from the list of words_to_learn.


try:
    DATA = pd.read_csv("Day31_Flash_Card_Capstone/data/words_to_learn.csv")
except FileNotFoundError:
    print("Can not find words_to_learn.csv. Will create one")
    try:
        DATA = pd.read_csv("Day31_Flash_Card_Capstone/data/french_words.csv")
        DATA.to_csv("Day31_Flash_Card_Capstone/data/words_to_learn.csv", index=False)
    except FileNotFoundError:
        print("Can't find either word source files.")
# Create a list of dictionary items from the DATA dataframe
WORD_DICT_LIST = DATA.to_dict(orient="records")
CURRENT_WORD = {}


def remove_word():
    WORD_DICT_LIST.remove(CURRENT_WORD)
    df = pd.DataFrame(WORD_DICT_LIST)
    df.to_csv("Day31_Flash_Card_Capstone/data/words_to_learn.csv")
    if len(WORD_DICT_LIST) == 0:
        print("No more words to learn!")
    else:
        print(f"Words remaining to learn: {len(WORD_DICT_LIST)}")
        next_card()


def flip_card():
    global CURRENT_WORD

    # Update the image of the existing background item
    canvas.itemconfig(background_image_id,image = card_back_img)
    
    # IMPORTANT: Update the persistent reference to the new PhotoImage
    canvas.current_background_image_ref = card_back_img
    
    # Update text
    canvas.itemconfig(word_text, text=CURRENT_WORD['English'], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")


def next_card():
    global CURRENT_WORD, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(background_image_id,image = card_front_img)
    canvas.current_background_image_ref = card_front_img
    
    CURRENT_WORD = random.choice(WORD_DICT_LIST)
    
    canvas.itemconfig(word_text, text=CURRENT_WORD['French'], fill="black")
    canvas.itemconfig(title_text, text='French', fill="black")
    flip_timer = window.after(3000, flip_card)
    

#================================ UI =================================
window = Tk()
window.title("Language Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#PhotoImages must be initialized after the creation of the window
try:
    RIGHT_IMG = PhotoImage(file='Day31_Flash_Card_Capstone/images/right.png')
    WRONG_IMG = PhotoImage(file='Day31_Flash_Card_Capstone/images/wrong.png')
except FileNotFoundError as e:
    print(f"Can not find button images: {e}")

canvas = Canvas(width=800 , height=526 ,bg = BACKGROUND_COLOR, highlightthickness=0)
try:
    card_front_img = PhotoImage(file='Day31_Flash_Card_Capstone/images/card_front.png')
    card_back_img = PhotoImage(file='Day31_Flash_Card_Capstone/images/card_back.png')
except FileNotFoundError as e:
    print(f"Can not find card background image: {e}")

# Create the background image item on the canvas. Store its ID for later modification.
background_image_id = canvas.create_image(400,263,image = card_front_img)
# Keep a reference to the PhotoImage to prevent garbage collection
canvas.current_background_image_ref = card_front_img

# Text elements
title_text = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 253, text = "Word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

# Buttons
correct_button = Button(image=RIGHT_IMG, highlightthickness=0, command=remove_word)
correct_button.grid(column=1, row=2)
wrong_button = Button(image=WRONG_IMG, highlightthickness=0, command=next_card)
wrong_button.grid(column=2,row=2)

next_card()

window.mainloop()