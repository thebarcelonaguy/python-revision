import turtle

turtle_riten = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    turtle_riten.forward(50)


def event_listener():
    screen.listen()
    screen.onkey(key="space", fun=move_forward)
    screen.exitonclick()


event_listener()
