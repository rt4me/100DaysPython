###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

def get_color_pallet():
    """Uses the colorgram module to pull the RGB values from a jpg image"""
    rgb_colors = []
    final_color_list = []
    colors = colorgram.extract('Dot_painting.jpg', 20)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        #Don't add what is probably the background color, white, to the rgb_colors list
        if r + g + b <= 740:
            new_color = (r, g, b)
            rgb_colors.append(new_color)
    # print(len(rgb_colors))
    # print(rgb_colors)

    return rgb_colors

def create_hirst_like_painting():
    """Creat a hirst-like DOT painting. Should have 10x10 dots.
    Dots should be sized 20, with a spacing of 50 between them.
    Dots should use a random color from the color pallet returned by get_color_pallet()"""

    tim = Turtle()
    tim.penup()
    tim.hideturtle()
    tim.speed(0)
    start_location = -250
    tim.goto(start_location, start_location)
    color_pallet = get_color_pallet()

    for vertical in range(1,11):
        for horizontal in range(1, 11):
            tim.dot(20, random.choice(color_pallet))
            tim.forward(50)
        tim.goto((start_location, start_location + (50 * vertical)))

create_hirst_like_painting()

screen = Screen()
screen.exitonclick()