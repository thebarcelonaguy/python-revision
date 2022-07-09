import smtplib
import random
import datetime as dt

my_email = "ritenbhagra2000@gmail.com"
password = "nfgbuojbueicosui"

with open("quotes.txt", mode='r') as quotes:
    list1 = quotes.readlines()
    random_quote = random.choice(list1)

current_weekday = dt.datetime.now().weekday()
if current_weekday == 4:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="barcelonaismylife2000@gmail.com",
                            msg=f"Subject:Motivation to do better\n\n {random_quote}")
