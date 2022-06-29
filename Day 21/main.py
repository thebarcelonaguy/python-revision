import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("my Snake Game")
screen.tracer(0)

Snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=Snake.up, key="Up")
screen.onkey(fun=Snake.down, key="Down")
screen.onkey(fun=Snake.left, key="Left")
screen.onkey(fun=Snake.right, key="Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()

    if Snake.segment[0].distance(food) < 15:
        food.refresh()
        scoreboard.addscore()
        Snake.extend()

    if Snake.segment[0].xcor() > 280 or Snake.segment[0].xcor() < -280 or Snake.segment[0].ycor() > 280 or \
            Snake.segment[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in Snake.segment:
        if segment == Snake.segment[0]:
            pass
        elif Snake.segment[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
