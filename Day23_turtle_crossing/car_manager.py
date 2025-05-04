from turtle import Turtle
from random import  choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(randrange(-300, 300, 40), randrange(-220, 220, 30))
        self.showturtle()
        self.current_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        self.forward(self.current_speed)
        if self.xcor() < -300:
            self.goto(320, randrange(-220, 220, 30))

    def level_speed_up(self):
        self.current_speed += MOVE_INCREMENT