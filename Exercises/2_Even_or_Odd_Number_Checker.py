# Exercise 2: Even or Odd Number Checker
# Objective: Write a Python program that asks the user to enter an integer and determines whether it is even or odd.

# Requirements
#     1. Ask the user to enter an integer.
#     2. If the number is divisible by 2 with no remainder, print that it is an even number.
#     3. Otherwise, print that it is an odd number

num = int(input("Enter a number:"))

if num % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")    