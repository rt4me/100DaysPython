from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

def correct_answer():
    pass

def wrong_answer():
    pass


#====================Create Card===============================

def create_card():
    data = pd.read_csv("Day31_Flash_Card_Capstone\data\french_words.csv")
    data_dict = data.to_dict(orient="records")
    
    word = random.choic(data_dict)



#================================ UI =================================
# window = Tk()
# window.title("Language Flash Cards")
# window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# #PhotoImages must be initialized after the creation of the window
# RIGHT_IMG = PhotoImage(file='Day31_Flash_Card_Capstone/images/right.png')
# WRONG_IMG = PhotoImage(file='Day31_Flash_Card_Capstone/images/wrong.png')

# canvas = Canvas(width=800 , height=526 ,bg = BACKGROUND_COLOR, highlightthickness=0)
# card_front_img = PhotoImage(file='Day31_Flash_Card_Capstone/images/card_front.png')
# canvas.create_image(400,263,image = card_front_img)
# title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
# word_text = canvas.create_text(400, 253, text = "French Word", font=("Ariel", 60, "bold"))
# canvas.grid(column=1, row=1, columnspan=2)

# # Buttons
# correct_button = Button(image=RIGHT_IMG, highlightthickness=0, command=correct_answer)
# correct_button.grid(column=1, row=2)
# wrong_button = Button(image=WRONG_IMG, highlightthickness=0, command=wrong_answer)
# wrong_button.grid(column=2,row=2)


# window.mainloop()

create_card()