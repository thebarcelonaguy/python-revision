from datetime import datetime

import requests

my_lat = 51.507351
my_long = -0.127758
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# position = (longitude, latitude)
# print(position)

parameters = {"lat": my_lat, "long": my_long, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split()[1].split(":")[0]
sunset = data["results"]["sunset"].split()[1].split(":")[0]

time_now = datetime.now()
print(time_now)
