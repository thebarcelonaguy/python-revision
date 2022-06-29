from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Scoreboard: {self.score}", False, align='center', font=('Times New Roman', 14, 'normal'))

    def addscore(self):
        self.clear()
        self.score += 1
        self.write(f"Scoreboard: {self.score}", False, align='center', font=('Times New Roman', 14, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center', font=('Times New Roman', 14, 'normal'))
