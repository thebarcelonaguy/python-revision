import random

from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed= STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1, 5)
        if random_num == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300,random.randint(-260, 260))
            self.cars.append(car)
            car.setheading(180)

    def move(self):
        for i in self.cars:
            i.forward(self.speed)

    def speed_increase(self):
        self.speed+=MOVE_INCREMENT


