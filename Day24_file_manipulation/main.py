file = open("/home/timb/Documents/Python_Projects/100 days of Code/Day24_file_manipulation/my_file.txt") #Using relative path (i.e. needing to go up multiple directories to get to file.
contents = file.read()
print(contents)
file.close()

# Don't need to include the close() if using "with"
# By default, it's open in Read Only mode.
# Write mode is "w". This will overwrite everything in the file. If file doesn't exist it will create it in this mode.
# Append mode is "a". This will append to the file.
with open("/home/timb/my_file.txt", mode='a') as myfile:
    myfile.write("\nAdded via code.")


with open("new_file.txt", mode='w') as newfile:
    newfile.write("\nFile created by code.")