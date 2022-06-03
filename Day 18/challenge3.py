from turtle import Turtle as T, Screen as S
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
s = S()
turtle = T()
for shape in range(3,11):
    turtle.color(random.choice(colours))
    for i in range(0, shape):
        turtle.forward(100)
        turtle.right(360/shape)



s.exitonclick()
