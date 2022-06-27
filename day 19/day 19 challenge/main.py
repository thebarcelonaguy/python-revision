import random
from turtle import Turtle, Screen

game_on = False
screen = Screen()
screen.setup(width=800, height=600)
colors = ["red", "orange", "blue", "green", "purple", "yellow"]
y_position = [-50, -20, 10, 40, 70, 100]
all_turtles = []
winning_turtle = ""
for i in range(0, 6):
    turtle_race = Turtle("turtle")
    turtle_race.penup()
    turtle_race.color(colors[i])
    turtle_race.setpos(x=-380, y=y_position[i])
    all_turtles.append(turtle_race)
user_bet = screen.textinput("Place a bet", "Pick a color of the turtle you wanna place bet on")
game_on = True
while game_on:
    for turtle in all_turtles:
        random_step = random.randint(0, 10)
        turtle.forward(random_step)
        if turtle.xcor() > 370:
            game_on = False
            winning_turtle = turtle.color()[0]

screen.exitonclick()

if winning_turtle == user_bet:
    print("You won the bet!")
else:
    print("Fucking loser!")
