from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
USER_PADDLE_X_POS = 350
NEW_PADDLE_Y_POS = 0
COMPUTER_PADDLE_X_POS = -350

class Paddle(Turtle): # Inheriting from Turtle
    def __init__(self, coordinates):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        # Default turtle size is 20x20 so these multipliers are used to end up with 20x100
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.setposition(coordinates)
        self.showturtle()



    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)