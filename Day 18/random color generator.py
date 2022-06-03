import random
import turtle as T

direction = [0, 90, 180, 270]
s = T.Screen()
turtle = T.Turtle()
turtle.speed(10)
turtle.width(5)
T.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for shape in range(0, 100):
    turtle.pencolor(random_color())
    random_direction = random.choice(direction)
    turtle.setheading(random_direction)
    turtle.forward(30)
s.exitonclick()
