# with open("weather_data.csv") as csv_data:
#     wd = csv_data.readlines()
#     weather_data = []
#     for day in wd:
#         weather_data.append(day.strip())

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#print(data)
data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
# print(average)
# #Faster way:
# print(data["temp"].mean())
# #alternate
# print(data.temp.mean())
#
# print(f"Max temp in the week: {data['temp'].max()}")
#
#Get data in rows. The below will give all the data in the Row where the day was Monday
# print(data[data.day == "Monday"])
#
# #Get the row of data where it has the max temperature
# print(data[data.temp == data.temp.max()])

#Get temp from Monday but convert from C to F
monday_temp = data[data.day == "Monday"].temp[0]
def celc_to_fht(c):
    return c * 9/5 + 32
print(f"Celc to Fahrenheit: {monday_temp} -> {celc_to_fht(monday_temp)}")
