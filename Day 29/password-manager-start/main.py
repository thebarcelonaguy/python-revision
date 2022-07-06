import random
import pyperclip
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    list1 = [random.choice(letters) for _ in range(nr_letters)]
    list2 = [random.choice(symbols) for _ in range(nr_symbols)]
    list3 = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = list1 + list2 + list3
    random.shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def check_field_empty():
    if len(website_text.get()) == 0 or len(password_text.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave the fields empty")
    else:
        add_button()


def add_button():
    is_ok = messagebox.askokcancel(title=website_text.get(),
                                   message=f"These are the details you entered : \n Email: {email_text.get()}\n"
                                           f" Password: {password_text.get()} \n "
                                           f"Is it okay to save?")
    if is_ok:
        password_save()
        website_text.delete(0, END)
        email_text.delete(0, END)
        password_text.delete(0, END)


def password_save():
    with open("password.txt", mode='a') as f1:
        f1.write(f"{website_text.get()} | {email_text.get()} | {password_text.get()} \n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image_url = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_url)
canvas.grid(row=0, column=1)
label_website = Label(text="Website:", bg="white")
label_website.grid(row=1, column=0)
website_text = Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
email_text = Entry(width=35)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "abc@yahoo.com")
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)
password_text = Entry(width=21)
password_text.grid(row=3, column=1)
button = Button(text="Generate Password", highlightthickness=0, command=random_password)
button.grid(row=3, column=2)
button1 = Button(text="Add", width=36, command=check_field_empty)
button1.grid(row=4, column=1, columnspan=2)

window.mainloop()
