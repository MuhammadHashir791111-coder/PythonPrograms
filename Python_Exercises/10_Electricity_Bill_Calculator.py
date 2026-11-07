# Exercise 10: Electricity Bill Calculator
# Objective: Write a Python program that asks the user how many electricity units (kWh) they have consumed and calculates their electricity bill.

# Requirements
#     1. Ask the user to enter their electricity consumption in units.
#     2. Check whether the entered units are valid.
#     3. Assign an electricity rate according to the consumption.
#     4. Calculate the total bill.
#     5. Display the total amount.

# Use the following fictional rates for this exercise.                          Formula:
#                                                                                        Bill = Units Consumed * Rate
#       Electricity consumption	| Rate per unit
#            0–100 units	    |    Rs 10
#           101–200 units       |    Rs 15
#        More than 200 units	|    Rs 20

units = int(input("Enter your electricity consumption in units: "))                 #Taking units as input


if units < 0:                                                                       #Checking whether the entered units are valid
    print("\nINVALID-ENTRY!\n")

elif units == 0:
    print("\nNO CONSUMPTION THIS MONTH")
    print("TOTAL PAYABLE AMOUNT: Rs 0\n")

elif units <= 100:
    bill = units * 10                                                               #Calculating the total bill with Rs 10 as rate per unit.
    print(f"\nTOTAL PAYABLE AMOUNT : Rs {bill}\n")

elif units <= 200:
    bill = units * 15                                                               #Calculating the total bill with Rs 15 as rate per unit.
    print(f"\nTOTAL PAYABLE AMOUNT : Rs {bill}\n")

elif units > 200:
    bill = units * 20                                                               #Calculating the total bill with Rs 20 as rate per unit.
    print(f"\nTOTAL PAYABLE AMOUNT : Rs {bill}\n")


#NOTE: I used \n because the output in the terminal looks good to me.