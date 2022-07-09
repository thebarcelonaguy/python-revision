##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib

import pandas as pd

my_email = "ritenbhagra2000@gmail.com"
password = "nfgbuojbueicosui"


# 1. Update the birthdays.csv

def random_letter():
    l1 = "letter_1.txt"
    l2 = "letter_2.txt"
    l3 = "letter_3.txt"
    list_letters = [l1, l2, l3]
    return random.choice(list_letters)


# 2. Check if today matches a birthday in the birthdays.csv
birthday_df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
today_day = now.day
today_month = now.month
today_tuple = (today_month, today_day)
random_letter_template = random_letter()
birthday_dict = {(row["month"], row["day"]): row for (index, row) in birthday_df.iterrows()}

if today_tuple in birthday_dict:
    with open(f"./letter_templates/{random_letter()}", mode='r') as f1:
        contents = f1.read()
        contents = contents.replace("[NAME]", birthday_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_dict[today_tuple]["email"],
                            msg=f"Subject:Happy Birthday! From Riten Bhagra\n\n {contents}")
