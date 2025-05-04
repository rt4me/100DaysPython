from turtle import Turtle
import config

ALIGNMENT = "center"
FONT = ("courier", 16, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data_file:
            self.high_score = int(data_file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,config.SCREEN_HEIGHT/2 -30)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.write_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            with open("data.txt", mode = "w") as hs_file:
                hs_file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.write_scoreboard()