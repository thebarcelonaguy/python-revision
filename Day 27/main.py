import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
input_user = tkinter.Entry(width=10)

input_user.pack()


def button_click():
    x = input_user.get()
    my_label.config(text=x)


my_button = tkinter.Button(text="Click me", command=button_click)
my_button.pack()

window.mainloop()
