from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(positions)

    def move_left(self):
        self.setheading(90)
        self.forward(20)
        self.setheading(0)

    def move_right(self):
        self.setheading(270)
        self.forward(20)
        self.setheading(0)
