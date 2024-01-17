# Creating the list of students
students_data = [

    {"name": "Shivang", "grades": [76, 85, 52, 88, 80]},
    {"name": "Naman", "grades": [30, 92, 88, 85, 78]},
    {"name": "Varana", "grades": [82, 79, 88, 80, 75]},
    {"name": "Triparna", "grades": [45, 88, 92, 85, 90]},
    {"name": "Apar", "grades": [88, 76, 90, 85, 92]},
    {"name": "Kevin", "grades": [65, 60, 62, 88, 78]},
    {"name": "Nishil", "grades": [92, 88, 85, 90, 76]},
    {"name": "Mahmad", "grades": [78, 85, 72, 90, 88]},
    {"name": "Kush", "grades": [50, 68, 72, 85, 80]},
    {"name": "Mridul", "grades": [88, 62, 85, 90, 78]},
    {"name": "Riya", "grades": [75, 88, 90, 92, 85]},
    {"name": "Dhruv", "grades": [72, 85, 88, 90, 76]},
    {"name": "Rudra", "grades": [88, 80, 85, 92, 78]},
    {"name": "Neel", "grades": [85, 92, 78, 90, 88]}
]

#/--- Generator expression to calculate average grades
average_grades = [
    {"name": student["name"], "average_grade": sum(student["grades"]) / len(student["grades"])}
    for student in students_data
]
print(average_grades)
print("----------------------------")


#/--- Students above grade 85
for student in average_grades:
    if student['average_grade']>85:
        print(f"{student['name']} Grade{student['average_grade']}")


#/--- Sort desc
sorted_students = sorted(average_grades, key=lambda student: student["average_grade"], reverse=True)
print(sorted_students)
copylist=sorted_students
print("----------------------------")

#/--- Highest Grade
copylist.reverse()
Highest_Grade=copylist.pop()
print(Highest_Grade)

#/--- Store results in text file
# Open a text file in write mode
with open("Assignment1.txt", "w") as file:
    file.write("Average Grades of all students\n\n")
    for student in average_grades:
        file.write(f"{student['name']} - Average Grade: {student['average_grade']:.2f}\n")
    file.write("\n\n------------------------\n")
    file.write("Students in desc form\n")
    average_grades.reverse()
    for student in average_grades:
        file.write(f"{student['name']} - Average Grade: {student['average_grade']:.2f}\n")
    file.write("\n\n------------------------\n")
    file.write("Students having more than 85\n")
    for student in average_grades:
        if student['average_grade'] > 85:
            file.write(f"{student['name']} - Average Grade: {student['average_grade']:.2f}\n")
    file.write("\n\n------------------------\n")
    file.write("Student with highest grade\n")
    file.write(f"{Highest_Grade}")