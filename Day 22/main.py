import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

turtle = Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
screen.listen()
screen.onkey(paddle1.move_left, key="Up")
screen.onkey(paddle1.move_right, key="Down")
screen.onkey(paddle2.move_left, key="w")
screen.onkey(paddle2.move_right, key="s")
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
