# Exercise 1: Age Eligibility Checker
# Objective: Write a Python program that asks the user for their age and determines whether they meet a specified age requirement.

# Requirements
#   1. Ask the user to enter their age.
#   2. If the age is negative, display an invalid-age message.
#   3. If the age is 0, display a message stating that the user is a newborn.
#   4. If the age is between 1 and 17, state that the user is under 18.
#   5. If the age is 18 or older, state that the user meets the age requirement.
#   6. Display a goodbye message at the end.

age = int(input("Enter your age: "))                 #Taking the age as input


if age < 0:
    print("\nINALID-AGE!")                           #The age cannot be negative

elif age == 0:
    print("\nThe user is a newborn.")

elif age > 0 and age < 18:
    print("\nThe user is under 18.")

elif age >= 18:
    print("\nThe user meets the age requirement.")

else:
    print("\nINVALID-INPUT!")                       #This statement will be executed when the user is smart

print("\nGood-bye\n")


#NOTE: I used \n because the output in the terminal looks good to me.