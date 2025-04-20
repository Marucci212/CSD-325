# Justin Marucci
# Assignment 8.2

import json

# Function to print student list
def print_students(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load student data from JSON file
with open("student.json", "r") as file:
    students = json.load(file)

print("Original Student List:")
print_students(students)

# Add your data
new_student = {
    "F_Name": "Justin",
    "L_Name": "Marucci",
    "Student_ID": 163729,
    "Email": "JustinMarucci@example.com"
}
students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

# Write updated list back to JSON file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file has been updated.")
