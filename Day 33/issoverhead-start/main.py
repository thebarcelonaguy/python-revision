import smtplib
import time
from datetime import datetime

import requests

MY_LAT = 32.109500  # Your latitude
MY_LONG = 76.535800  # Your longitude

my_email = "ritenbhagra2000@gmail.com"
password = "nfgbuojbueicosui"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


def is_overhead():
    if abs(abs(iss_longitude) - abs(MY_LONG)) < 5 and abs(abs(iss_latitude) - abs(MY_LAT)) < 5:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="barcelonaismylife2000@gmail.com",
                                msg="ISS JUST OVER YOUR LOCATION \n\n Dear Riten \n,"
                                    "Just a reminder that you created a python program to check if space stati"
                                    "on was above you. \n "
                                    "GO CHECK IT OUT!"
                                    "\n HAVE FUN! STAY HYDRATED AND FORCA BARCA")
