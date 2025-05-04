from turtle import Turtle

#STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
START_NUM_SEGMENTS = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    starting_positions = []

    def set_start_positions(self):
        for seg in range(0,START_NUM_SEGMENTS):
            x_position = seg * -20
            self.starting_positions.append((x_position, 0))

    def create_snake(self):
        self.set_start_positions()
        for position in self.starting_positions:
            self.add_segment(position)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(700, 700)
        self.segments.clear()
        self.starting_positions.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        """Extend the snake after eating a food pelet.
        Pass along the coordinates for the last snake segment's position"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

