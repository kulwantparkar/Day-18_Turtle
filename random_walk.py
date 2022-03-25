import turtle
from turtle import Turtle, Screen
import random
tom = Turtle()
screen = Screen()
turtle.colormode(255)

def set_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    rand_color = (r, g, b)
    return rand_color
# color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]


tom.pensize(15)
tom.speed(0)

directions = [0, 90, 180, 270]

for _ in range(100):
    tom.color(set_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))

screen.exitonclick()