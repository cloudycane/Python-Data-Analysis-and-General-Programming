import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
graysquirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinammonsquirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
blacksquirrels = len(data[data["Primary Fur Color"] == "Black"])
print(graysquirrels)
print(cinammonsquirrels)
print(blacksquirrels)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [graysquirrels, cinammonsquirrels, blacksquirrels]

}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrelcount.csv")