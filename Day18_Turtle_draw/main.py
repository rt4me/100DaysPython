import random
import turtle
from turtle import Turtle, Screen
from random import choice

#Changes colormode to use a range of 0-255 instead of default 0-1.0 for use in RGB
turtle.colormode(255)

tim = Turtle()
color_list = ['black', 'red', 'blue', 'green', 'orange', 'pink', 'cyan','peru','OliveDrab','purple']

def draw_square():
    tim.shape("turtle")
    tim.color("OrangeRed3")
    for _ in range(4):
        tim.forward(100)
        tim.right(90)
#draw_square()

def dashed_line():
    tim.shape("turtle")
    tim.color("blue")
    #Moved to left edge and face right; no line
    tim.penup()
    tim.setpos(-550,0)
    for _ in range(50):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)

#dashed_line()

def draw_shapes(min_sides, max_sides):
    tim.shape("turtle")
    #color_list = ['black', 'red', 'blue', 'green', 'orange', 'pink', 'cyan','peru','OliveDrab','purple']
    for side in range(min_sides,max_sides + 1):
        tim.color(choice(color_list))
        for _ in range(side):
            tim.forward(100)
            tim.right(360/side)


# draw_shapes(3, 10)


def random_rgb_color():
    """Return a tuple containing a random RGB color value"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_random_walk(distance):
    """Create a window and draw lines, using a random RGB color for each segment"""
    angles = [0, 90, 180,  270]
    tim.speed(0)
    tim.pensize(7)
    for _ in range(distance):
        tim.color(random_rgb_color())
        tim.setheading(choice(angles))
        tim.forward(30)

#draw_random_walk(200)

def draw_spyrograph(circle_radius, repeat_num):
    """Draw a circle multiple times, rotating it around the start point to make a spyrograph-like pattern"""
    tim.speed(0)
    tim.pensize(3)
    for i in range(repeat_num):
        tim.color(random_rgb_color())
        tim.circle(circle_radius)
        tim.left(360/repeat_num)

#draw_spyrograph(100, 60)

def follow_directions():
    tim.speed(5)
    tim.setheading(180)
    tim.forward(50)
    tim.setheading(270)
    tim.forward(40)

follow_directions()

screen = Screen()
screen.exitonclick()