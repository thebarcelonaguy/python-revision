import turtle
from turtle import Screen

screen = Screen()

positions = [0, -20, -40]
movement = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            snake = turtle.Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setposition(x=positions[i], y=0)
            self.segment.append(snake)

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(x=new_x, y=new_y)
        self.segment[0].forward(movement)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(0)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(180)
