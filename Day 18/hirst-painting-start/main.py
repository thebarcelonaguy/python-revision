import random
import turtle
import colorgram
from turtle import *

turtle.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


def dot_draw():
    t = Turtle()
    s = Screen()
    t.hideturtle()
    t.penup()
    t.speed("fastest")
    t.setheading(225)
    t.forward(400)
    t.setheading(0)
    for outer in range(0, 10):
        for inner in range(0, 10):
            t.pencolor(random.choice(rgb_colors))
            t.dot(20)
            t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(90)
        t.forward(50)
        t.setheading(0)
    s.exitonclick()


dot_draw()
