# Import csv into data

# with open("weather_data.csv", mode="r") as file:
#     data = []
#     for element in file:
#         data.append(element.strip("\n").split(","))
#
# print(data)

# import csv
#
# with open("weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         else:
#             # print(row[1])
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# def calculate_average(data):
#     counter = 0
#     temp_sum = 0
#     for element in data:
#         temp_sum += element
#         counter += 1
#     av_temp = temp_sum / counter
#     print(av_temp)

# calculate_average(temp_list)

# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)

# Get data in row
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * (9 / 5)) + 32)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

# data_dict = {
#     "color": data["Primary Fur Color"],
#     "count": data["Primary Fur Color"].count()
# }

color = data["Primary Fur Color"].values
print(color)

# new_data = pandas.DataFrame(data_dict)
