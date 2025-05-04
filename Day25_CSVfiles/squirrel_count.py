import pandas

from main import data_dict

sql_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250214.csv")

# Short way to find information but in the incorrect format
# sql_type_counts = sql_data["Primary Fur Color"].value_counts()
# sql_type_counts.to_csv("SQL Report Counts.csv")

"""Pull information from Central Park Squirrel census file. 
Get a count of each type of squirrel, based on primary fur color"""

# Use len() to get the count of squirrels with each fur color
gray_squirrels_count = len(sql_data[sql_data["Primary Fur Color"]  == "Gray"])
red_squirrels_count = len(sql_data[sql_data["Primary Fur Color"]  == "Cinnamon"])
black_squirrels_count = len(sql_data[sql_data["Primary Fur Color"]  == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# Creat a dictionary  of the fur color and counts
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count,black_squirrels_count]
}

# Create a Data Frame based on the dictionary. Output to CSV.
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel Report Counts.csv")





