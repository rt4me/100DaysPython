from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 600/2 -40)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score}  :  {self.right_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_up_left(self):
        self.left_score += 1
        self.write_scoreboard()

    def score_up_right(self):
        self.right_score += 1
        self.write_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)