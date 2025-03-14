from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def reset_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
        time.sleep(1)


    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_back(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)