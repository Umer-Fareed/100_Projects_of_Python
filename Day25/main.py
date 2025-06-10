#with open("weather_data.csv") as data_file:
#   data = data_file.readline()
#  print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"]

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(round(data["temp"].max()))


#data in rows
# print(data[data.day  == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#create a dataframe
data_dict = {
    "students" : ["any","james","angela"],
    "score" : [12,32,43]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
