# Exercise 1: Age Eligibility Checker
# Objective: Write a Python program that asks the user for their age and determines whether they meet a specified age requirement.

# Requirements
#    1. Ask the user to enter their age.
#    2. If the age is negative, display an invalid-age message.
#    3. If the age is 0, display a message saying the user is a newborn.
#    4. If the age is between 1 and 17, display that the user is under 18.
#    5. If the age is 18 or older, display that the user meets the age requirement.
#    6. Display a goodbye message at the end.

age = int(input("Enter your age:"))

if age < 0:
    print("INALID-AGE!")
elif age == 0:
    print("The user is a newborn.")
elif age > 0 and age < 18:
    print("The user is under 18.")
elif age >= 18:
    print("The user meets the age requirement.")
else:
    print("INVALID-INPUT!")
print("Good-bye\n")                     