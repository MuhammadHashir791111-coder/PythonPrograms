# Exercise 9: Vowel or Consonant Checker
# Objective: Write a Python program that asks the user to enter a single alphabet letter and determines whether it is a vowel or a consonant.

# Requirements
#     1. Ask the user to enter one alphabet letter.
#     2. If the letter is a vowel, print "The letter is a vowel."
#     3. If the letter is a consonant, print "The letter is a consonant."
#     4. The program should recognise both uppercase and lowercase letters.

letter = (input("Enter an alphabet letter: "))                   #Taking a letter as input


if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("\nThe letter is a vowel.\n")

elif letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    print("\nThe letter is a vowel.\n")

else:
    print("\nThe letter is a consonant.\n")


#NOTE: I used \n because the output in the terminal looks good to me.