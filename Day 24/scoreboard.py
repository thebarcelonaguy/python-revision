from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def addscore(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}  High Score: {self.maintain_high()}", False, align='center',
                   font=('Times New Roman', 14, 'normal'))

    def reset(self):
        if self.score > self.maintain_high() :
            with open("data.txt",'w') as high_score:
                high_score.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def maintain_high(self):
        with open("data.txt") as high_score:
            highscore = int(high_score.read())
            return  highscore