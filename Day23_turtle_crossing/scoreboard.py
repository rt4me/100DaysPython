from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 16, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.level = 1
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.write_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)