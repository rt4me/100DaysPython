import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

scoreboard = Scoreboard()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
car_list = []

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_back, "Down")

# Set number of cars and create instances
for i in range(20):
    new_car = CarManager()
    car_list.append(new_car)

game_is_on = True
while game_is_on:

    for i in car_list:
        i.move_car()

    time.sleep(0.1)
    screen.update()

    # Turtle gets to finish line
    if player.ycor() > 240:
        scoreboard.level_up()
        for i in car_list:
            i.level_speed_up()
        player.reset_start()

    # Detect turtle hit by car
    for i in car_list:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()