# Exercise 4: Largest of Two Numbers
# Objective: Write a Python program that asks the user to enter two numbers and determines which number is larger.

# Requirements
#     1. Ask the user to enter the first number.
#     2. Ask the user to enter the second number.
#     3. Compare the two numbers.
#     4. Display the larger number.
#     5. If both numbers are equal, display a message saying they are equal.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > num2:
    print(f"{num1} is larger than {num2}.")
elif num1 < num2:    
    print(f"{num2} is larger than {num1}.")
elif num1 == num2:
    print("Both numbers are equal.")