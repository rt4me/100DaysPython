#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]
print(f"letters_list = {letters_list}")

#Range as List
range_list = [n * 2 for n in range(1, 5)]
print(f"Range as a list; range_list = {range_list}")

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(f"Student grades: {student_grades}")

passed_students = {student: grade for (student, grade) in student_grades.items() if grade >= 60
}
print(f"Students that passed: {passed_students}"
      )
