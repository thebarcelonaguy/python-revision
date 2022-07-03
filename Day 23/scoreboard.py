from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.update_scoreboard()

    def add_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align="center", font=FONT)
