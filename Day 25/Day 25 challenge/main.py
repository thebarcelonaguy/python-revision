import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
Turtle = turtle.Turtle()
Turtle.penup()
Turtle.hideturtle()
scoreboard = 0

states = pandas.read_csv("50_states.csv")
game_on = True
states_guessed = []
while (game_on):
    answer_state = screen.textinput(title=f"{scoreboard}/ 50", prompt=f"What's another state name").title()
    if answer_state == "Exit":
        break
    for l in states["state"]:
        if l == answer_state:
            k = states[states["state"] == l]
            x = int(k["x"])
            y = int(k["y"])
            Turtle.goto(x, y)
            Turtle.write(f"{l}", False, align="left", font=("Times New Roman", 7, "normal"))
            if l not in states_guessed:
                states_guessed.append(l)
                scoreboard += 1

        if scoreboard == 50:
            game_on = False
            screen.exitonclick()

total_states = states["state"].to_list()

missing_states=[state for state in total_states if state not in states_guessed]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")