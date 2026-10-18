input_dict = {"p" : 1,
              "r" : -1,
              "s" : 0}
system_dict = {1 : "Paper",
              -1 : "Rock",
               0 : "Scissors"}


print("\n     <<GAME START>>\n")

import random

computer = random.choice([-1, 0, 1])
you_input = input("Enter your choice: ")

you = input_dict[you_input]
print("")
print(f"YOU : {system_dict[you]} | COMPUTER : {system_dict[computer]}")

if you==computer:
    print("     It's a Draw!")
else:

    if (computer==1 and you==-1):
        print("     RESULT : You Lose")

    elif (computer==1 and you==0):
        print("     RESULT : You Win!")

    elif (computer==-1 and you==1):
         print("     RESULT : You Win!")

    elif (computer==-1 and you==0):
        print("     RESULT : You Lose")

    elif(computer==0 and you==1):
        print("     RESULT : You Lose")  

    elif(computer==0 and you==-1):
        print("     RESULT : You Win!")

    else:
        print("     !!SOMETHING WENT WRONG!!")


print("\n     >>GAME END<<\n")
