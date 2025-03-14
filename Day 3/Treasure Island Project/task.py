print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
question1_answer = input("You've reached a T in the road. Go left or right?")
if question1_answer.lower() != 'left':
    print("You fell into an eternal pit!")
    print("GAME OVER")
else:
    question2_answer = input("You've reached a slow flowing, wide river. Swim or wait for a boat?")
    if question2_answer.lower() != "wait" and question2_answer.lower() != "boat":
        print("The river is full of man-eating fish!")
        print("GAME OVER")
    else:
        question3_answer = input("There is a wall on the other side with 3 doors, painted Red, Yellow and Blue. Which door do you open?")
        if question3_answer.lower() == "red":
            print("A large explosion goes off on the other side of the door and consumes you!")
            print("GAME OVER")
        elif question3_answer.lower() == 'blue':
            print("A wave of acid flows over you!")
            print("GAME OVER")
        else:
            print("The room is full of unimaginable riches!")