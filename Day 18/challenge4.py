import random
import turtle
from turtle import Turtle as T, Screen as S

turtle.colormode(255)
s = S()
riten_turtle = T()
riten_turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def spirograph(size_gap):
    for i in range(0, int(360/size_gap)):
        riten_turtle.pencolor(random_color())
        riten_turtle.circle(100)
        current_heading = riten_turtle.heading()
        riten_turtle.setheading(current_heading + size_gap)


spirograph(5)

s.exitonclick()
