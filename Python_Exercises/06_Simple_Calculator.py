# Exercise 6: Simple Calculator
# Objective: Write a Python program that asks the user to enter two numbers and an arithmetic operator, then performs the selected operation.

# Requirements
#     1. Ask the user to enter the first number.
#     2. Ask the user to enter the second number.
#     3. Ask the user to enter an arithmetic operator.
#     4. Perform the calculation based on the operator.
#     5. Display the result.
#     6. Display an error message if the user enters an unsupported operator.
#     7. Prevent division by zero.

num1 = int(input("Enter the first number: "))                 #Taking the first number as input and storing it in num1
num2 = int(input("Enter the second number: "))                #Taking the second number as input and storing it in num2
op   = input("Enter an arithmetic operator: ")                #Taking an arithmetic operator as input and storing it in op.


# ADDITION
if op == "+":
    print(f"\nThe sum is {num1 + num2}\n")

# SUBTRACTION
elif op == "-":
    print(f"\nThe result is {num1 - num2}\n")

# MULTIPLICATION
elif op == "*" or op == "x" or op == "X":       #Some users can be extremely smart, so our program should be ready for them.
    if op == "*":
        print(f"\nThe product is {num1 * num2}\n")
    elif  op == "x" or op == "X":
        print(f"\nThe product is {num1 * num2}")
        print("Has anyone ever told you that you are smart?\n")                 #We must appreciate the smart people

# DIVISION
elif op == "/":
    if num2 != 0:
        print(f"\nThe result is {num1 / num2}\n")
    else:
        print("\nERROR: Cannot divide by zero")

else:
    print("\nINVALID-OPERATOR!\n")


#NOTE: I used \n because the output in the terminal looks good to me.

#NOTE: I am one of the smart people.