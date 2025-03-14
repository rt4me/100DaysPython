import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Loop through dictionary using old school for loop
for (key, value) in student_dict.items():
    print(f"key = {key}")
    print(f"value = {value}")

print("\n")

student_data_frame = pandas.DataFrame(student_dict)
print(f"Pandas DataFrame: \n {student_data_frame}")
print("\n")

# Looping through dataframe (which is almost the same as going through a python dictionary)
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of data frame (vs looping through columns, as shown above)
# Each row is a Pandas series object
for (index, row) in student_data_frame.iterrows():
    print(f"Students: {row.student}")



