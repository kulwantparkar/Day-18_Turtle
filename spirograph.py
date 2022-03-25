import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()

turtle.colormode(255)


def set_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rand_color = (r, g, b)
    return rand_color

timmy.speed("fastest")

def donut(num):
    for _ in range(int(360/num)):
        timmy.circle(50)
        timmy.color(set_color())
        current_heading = timmy.heading()
        timmy.setheading(current_heading + 10)

donut(5)



screen = Screen()
screen.exitonclick()