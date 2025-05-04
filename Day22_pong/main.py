from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

S_WIDTH_MIN = -400
S_WIDTH_MAX = 400
S_HEIGHT_MIN = -300
S_HEIGHT_MAX = 300


scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=S_WIDTH_MAX*2, height=S_HEIGHT_MAX*2)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) #This makes it so the information of the screen must be manually updated.

pencil = Turtle()


# def draw_center_line():
#     pencil.hideturtle()
#     pencil.penup()
#     pencil.pencolor("white")
#     pencil.pensize(5)
#     pencil.speed(1)
#     pencil.goto(x=0,y=S_HEIGHT_MIN-10)
#     pencil.setheading(90)
#     while pencil.ycor() < S_HEIGHT_MAX:
#         pencil.pendown()
#         pencil.forward(30)
#         pencil.penup()
#         pencil.forward(30)

# draw_center_line()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
sleep_time = .005

game_is_on = True
while game_is_on:
    screen.update()

    # print(ball.pos())
    # print(ball.heading())

    # Ball moves so long at still within screen boundaries.
    if S_WIDTH_MAX > ball.xcor() > S_WIDTH_MIN:
        # and S_HEIGHT_MAX - 10 > ball.ycor() > S_HEIGHT_MIN + 10:
        ball.ball_move()
        sleep(sleep_time)


    # Detect collision with wall; bounce
    if S_HEIGHT_MIN + 10 >= ball.ycor() or ball.ycor() >= (S_HEIGHT_MAX - 10):
        print("Wall collision")
        ball.wall_bounce(ball.heading())


    # Detect collision with paddles
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 330 and (ball.heading() < 90 or ball.heading() > 270))
            or (ball.distance(left_paddle) < 50 and ball.xcor() < -330 and 270 > ball.heading() > 90)):
        print(f"Paddle collision heading: {ball.heading()}")
        ball.paddle_bounce(ball.heading())
        sleep_time /= 1.3
        print(f"Sleep time: {sleep_time}")
        sleep(sleep_time)

    #Detect Left Paddle miss
    if ball.xcor() < S_WIDTH_MIN + 10:
        scoreboard.score_up_right()
        sleep_time = .005
        ball.reset_position()

    # Detect Right Paddle Miss
    if ball.xcor() > S_WIDTH_MAX - 10:
        scoreboard.score_up_left()
        sleep_time = .005
        ball.reset_position()

    # Game Over
    if scoreboard.left_score == 3 or scoreboard.right_score == 3:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()