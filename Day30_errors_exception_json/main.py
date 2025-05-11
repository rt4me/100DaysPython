# Day 30 - Errors, Exceptions and JSON Data

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# try: 
#     file = open('a_file.txt')
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("Something")
# except KeyError as e:
#     print(f"That key doesn't exist: {e}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")


height = float(input("Height (meters): "))
weight = int(input("Weight (kg): "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
if weight > 400:
    raise ValueError("Sorry if you weigh that much, but I have my doubts.")

bmi = weight / height ** 2
print(bmi)





# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Cherry", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# Keywords:
# try
# except
# else
# finally


