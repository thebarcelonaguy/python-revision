from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

entry1 = Entry()
entry1.config(width=10)
entry1.grid(row=0, column=1)

label1 = Label(text=" Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to ")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)


def calculate():
    miles = float(entry1.get())
    label3.config(text=round(miles * 1.6))


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
button.config(width=5)

window.mainloop()
