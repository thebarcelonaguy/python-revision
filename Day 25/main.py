# import csv
#
# with open("weather_data.csv",mode='r') as file:
#     data= csv.reader(file)
#     temperatures=[]
#     for row in data:
#         if row[1]!='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

x = pandas.read_csv("weather_data.csv")
dictionary = x.to_dict()
temp_list = x["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(f"Print average temp is: {avg_temp:.2f}")

print(x[x["temp"] == x["temp"].max()])

monday = x[x["day"] == "Monday"]

monday_temp_celsius= int(monday["temp"])
print(((9*monday_temp_celsius)/5)+32)

