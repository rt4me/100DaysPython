from turtle import Turtle

STARTING_POSITION = (-300, 300)
FONT = ("courier", 8, 'bold')
ALIGNMENT = "center"

class StateTurtle(Turtle):

    def __init__(self, state_name, x_loc, y_loc):
        super().__init__()
        #print(f"State: {state_name} ({x_loc}, {y_loc})")
        self.hideturtle()
        self.penup()
        self.goto(x_loc, y_loc)
        self.write(state_name, align=ALIGNMENT, font=FONT)
        #self.speed(1)
        #self.goto(STARTING_POSITION)
        #self.showturtle()


