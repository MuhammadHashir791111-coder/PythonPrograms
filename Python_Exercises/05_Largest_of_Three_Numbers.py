# Exercise 5: Largest of Three Numbers
# Objective: Write a Python program that asks the user to enter three numbers and determines which number is the largest.

# Requirements
#     1. Ask the user to enter the first number.
#     2. Ask the user to enter the second number.
#     3. Ask the user to enter the third number.
#     4. Compare the three numbers.
#     5. Display the largest number.
#     6. If all the numbers are equal, display a message saying they are equal.

num1 = int(input("Enter the first number: "))                    #Taking the first number as input and storing it in num1
num2 = int(input("Enter the second number: "))                   #Taking the second number as input and storing it in num2
num3 = int(input("Enter the third number: "))                    #Taking the third number as input and storing it in num3


if num1 == num2 and num2 == num3:
    print("\nAll the numbers are equal.\n")

elif num1 >= num2 and num1 >= num3:
    print(f"\n{num1} is the largest.\n")

elif num2 >= num1 and num2 >= num3:
    print(f"\n{num2} is the largest.\n")

else:
    print(f"\n{num3} is the largest.\n")


#NOTE: I used \n because the output in the terminal looks good to me.