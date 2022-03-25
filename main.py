import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)
tim = Turtle()
tim.color("orchid")
tim.shape("arrow")

tim.pensize(10)

def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def shapes(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)



for sides in range(3, 11):
    tim.color(set_color())
    shapes(sides)

screen = Screen()
screen.exitonclick()
print(tim)
