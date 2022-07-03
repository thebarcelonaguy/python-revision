import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for cars in car.cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 280:
        player.reset_turtle()
        car.speed_increase()
        scoreboard.add_level()
screen.exitonclick()