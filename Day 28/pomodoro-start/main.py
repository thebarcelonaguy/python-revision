import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def calculate_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    work_sec = 5
    short_sec = 3
    long_sec = 2

    if reps % 2 != 0:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    elif reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(long_sec)

    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_sec)


def calculate_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        calculate_start()
        mark = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer")
label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
label.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
t_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=t_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
button_start = Button(text="Start", command=calculate_start, width=5, bg="white")

button_start.grid(row=2, column=0)
button_reset = Button(text="Reset", command=calculate_reset, width=5, bg="white")
button_reset.grid(row=2, column=2)
checkmark_label = Label(width=10, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
checkmark_label.grid(row=3, column=1)
window.mainloop()
