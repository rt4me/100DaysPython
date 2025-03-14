import random
from turtle import Turtle, Screen

list_of_colors = ["red", "blue", "green", "orange", "purple", "black", "pink", "brown", "gold4", "navy"]
all_turtles = []
screen = Screen()
screen.setup(width=500, height=300)

user_bet = screen.textinput(title="Make your bet!", prompt="Which color turtle will win the race: ")

def set_default_turtle_state():
    default_x = -230
    default_y = int(-len(list_of_colors)/2) * 20
    for color in list_of_colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(default_x, default_y)
        new_turtle.setx(default_x)
        default_y += 20
        new_turtle.sety(default_y)
        new_turtle.pendown()
        all_turtles.append(new_turtle)

def move_forward(color, dist):
    return color.forward(dist)

def turtle_race():
    if user_bet:
        still_playing = True
    set_default_turtle_state()
    winner = ""
    while still_playing:
        for turtle_runner in all_turtles:
            random_len = random.randint(1,10)
            move_forward(turtle_runner, random_len)

        for turtle_check in all_turtles:
            if turtle_check.xcor() >= 230:
                winner = turtle_check
                still_playing = False
    if winner.color()[0] == user_bet:
        print("You win!")
    else:
        print(f"You lose. Turtle {winner.color()[0]} won.")

turtle_race()

screen.exitonclick()