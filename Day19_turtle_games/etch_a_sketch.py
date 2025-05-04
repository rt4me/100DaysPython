from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    return tim.forward(10)

def move_backward():
    return tim.backward(10)

def rotate_clockwise():
    return tim.right(10)

def rotata_counter_clockwise():
    return tim.left(10)

def reset():
    return tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotata_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key='c', fun=reset)


screen.exitonclick()