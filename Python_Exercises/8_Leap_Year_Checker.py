# Exercise 8: Leap Year Checker
# Objective: Write a Python program that asks the user to enter a year and determines whether it is a leap year.

# Requirements
#     1. Ask the user to enter a year.
#     2. Check whether the year is a leap year.
#     3. Print that the year is a leap year if it is.
#     4. Print that the year is not a leap year if it isn't.

year = int(input("Enter a year: "))                 #Taking a year as input


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"\n{year} is a leap year.\n")
else:
    print(f"\n{year} is not a leap year.\n")


#NOTE: Not every year divisible by 4 is a leap year.

#NOTE: A century year is not a leap year unless it is divisible by 400.

#NOTE: I used \n because the output in the terminal looks good to me.