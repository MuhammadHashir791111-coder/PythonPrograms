# Exercise 3: Positive, Negative, or Zero Detector
# Objective: Write a Python program that asks the user to enter a number and determines whether it is positive, negative, or zero.

# Requirements
#    1. Ask the user to enter a number.
#    2. If the number is greater than zero, print "The number is positive."
#    3. If the number is less than zero, print "The number is negative."
#    4. If the number equals zero, print "The number is zero."

num = int(input("Enter a number:"))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")