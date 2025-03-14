from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0,0)
        self.start_heading = 35
        self.speed = 1
        self.setheading(35)


    def ball_move(self):
        self.forward(self.speed)

    def wall_bounce(self, heading):
        new_heading = 360 - heading + randint(1, 3)
        return self.setheading(new_heading)

    def paddle_bounce(self, heading):
        new_heading = 180 - heading + randint(-1, 1)
        print(f"Incoming heading: {heading}; Outgoing heading: {new_heading}")
        return self.setheading(new_heading)

    def reset_position(self):
        self.goto(0, 0)
        self.start_heading += 180
        self.setheading(self.start_heading)