from turtle import Turtle, Screen

riten_turtle = Turtle()
screen = Screen()
riten_turtle.shape("turtle")
riten_turtle.color("red")
for i in range(0,4):
    riten_turtle.forward(100)
    riten_turtle.right(90)
# riten_turtle.right(90)
# riten_turtle.forward(100)
# riten_turtle.left(90)
screen.exitonclick()
