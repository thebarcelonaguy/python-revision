import time
from turtle import Screen

import snake
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("my Snake Game")
screen.tracer(0)

Snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()
    screen.listen()
    screen.onkey(fun=Snake.up, key="Up")
    screen.onkey(fun=Snake.down, key="Down")
    screen.onkey(fun=Snake.left, key="Left")
    screen.onkey(fun=Snake.right, key="Right")

screen.exitonclick()
