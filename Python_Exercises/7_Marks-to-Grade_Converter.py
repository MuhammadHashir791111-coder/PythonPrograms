# Exercise 7: Marks-to-Grade Converter
# Objective: Write a Python program that asks the user to enter their marks and converts those marks into a letter grade.

# Requirements
#     1. Ask the user to enter their marks out of 100.
#     2. Check whether the entered marks are valid.
#     3. Assign a grade according to the grading scale below.
#     4. Display the grade.

#                    GRADING SCALE
#                  Marks   |   Grade
#                 90-100   |    A+
#                 80-89    |    A
#                 70-79    |    B
#                 60-69    |    C
#                 50-59    |    D
#                 33-49    |    E
#                 00-32    |    F

marks = int(input("Enter your marks (out of 100): "))                   #Taking marks as input


if marks < 0 or marks > 100:                                            #Checking whether the entered marks are valid
    print("\nINVALID-MARKS!\n")

elif marks >=90:
    print("\nGrade : A+\n")

elif marks >= 80 and marks < 90:
    print("\nGrade : A\n")

elif marks >= 70 and marks < 80:
    print("\nGrade : B\n")

elif marks >= 60 and marks < 70:
    print("\nGrade : C\n")

elif marks >= 50 and marks < 60:
    print("\nGrade : D\n")

elif marks >= 33 and marks < 50:
    print("\nGrade : E\n")

elif marks < 33:
    print("\nGrade : F\n")


#NOTE: I used \n because the output in the terminal looks good to me.