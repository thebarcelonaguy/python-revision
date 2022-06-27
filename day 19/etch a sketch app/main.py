import turtle

turtle_sketch = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    turtle_sketch.forward(30)


def move_backward():
    turtle_sketch.backward(50)


def move_clockwise():
    turtle_sketch.right(10)


def move_anticlockwise():
    turtle_sketch.left(10)


def clear():
    turtle_sketch.reset()


def etch_sketch_app():
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=move_clockwise)
    screen.onkey(key="d", fun=move_anticlockwise)
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()


etch_sketch_app()
