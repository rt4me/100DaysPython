from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import config

screen = Screen()
screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Process keyboard commands
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision and move dot
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_up()
        snake.extend_snake()

    # Detect collision with wall
    if snake.head.xcor() > (config.SCREEN_WIDTH/2 -10) or snake.head.xcor() < -(config.SCREEN_WIDTH/2 - 10) or snake.head.ycor() > (config.SCREEN_HEIGHT/2 - 10) or snake.head.ycor() < -(config.SCREEN_HEIGHT/2 - 10):
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail.
    # Don't include checking against the head of the snake, as it will end the game immediately
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()