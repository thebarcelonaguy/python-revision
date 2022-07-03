import pandas

file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = file["Primary Fur Color"].dropna()
list_furcolor = fur_color.to_list()
gray = list_furcolor.count("Gray")
red = list_furcolor.count("Cinnamon")
black = list_furcolor.count("Black")
fur_dict = {"Fur Color": ["grey", "red", "black"],
            "Count": [gray, red, black]}
df_fur_count=pandas.DataFrame(fur_dict)
df_fur_count.to_csv("squirrel.csv")
