import turtle
import time
import random

screen = turtle.Screen()
screen.listen()


class Snek(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.parts = [(0, 0), (-20, 0), (-40, 0)]
        self.snek = []
        self.create_snake()
        self.head = self.snek[0]

    def create_snake(self):
        for segments in self.parts:
            self.add_parts(segments)

    def add_parts(self, segment):
        new_part = turtle.Turtle(shape="square")
        new_part.penup()
        new_part.color("green")
        new_part.goto(segment)
        self.snek.append(new_part)

    def extend(self):
        self.add_parts(self.snek[-1].position())

    def movement(self):

        def left():
            self.snek[0].setheading(180)

        def right():
            self.snek[0].setheading(0)

        def up():
            self.snek[0].setheading(90)

        def down():
            self.snek[0].setheading(270)

        for snek_parts in range(len(self.snek) - 1, 0, -1):
            new_x = self.snek[snek_parts - 1].xcor()
            new_y = self.snek[snek_parts - 1].ycor()
            self.snek[snek_parts].goto(new_x, new_y)
        self.head.forward(20)
        screen.onkey(up, "w")
        screen.onkey(down, "s")
        screen.onkey(left, "a")
        screen.onkey(right, "d")

    def sneak_reset(self):
        for seg in self.snek:
            seg.hideturtle()
        self.snek.clear()
        self.create_snake()
        self.head = self.snek[0]
