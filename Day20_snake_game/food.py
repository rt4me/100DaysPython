from random import randrange, randint
from turtle import Turtle
import random
import config

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh

    def refresh(self):
        self.goto(randint(-(config.SCREEN_WIDTH/2 - 50),(config.SCREEN_WIDTH/2 - 50)), randint(-(config.SCREEN_HEIGHT/2 - 50),(config.SCREEN_HEIGHT/2 - 50)))
