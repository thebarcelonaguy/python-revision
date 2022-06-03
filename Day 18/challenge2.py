from turtle import Turtle as T, Screen as S

s = S()
turtle = T()
turtle.color("red")
for i in range(0,10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

s.exitonclick()
