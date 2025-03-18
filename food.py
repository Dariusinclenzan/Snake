import turtle
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("purple")
        self.speed(0)
        self.reset_food()

    def reset_food(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)