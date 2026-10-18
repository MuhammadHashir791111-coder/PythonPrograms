import pyttsx3
pyttsx3.speak("WELCOME!")
pyttsx3.speak("Do you want to know if you can have sex?")
choice_1 = input("""Do you want to know if you are allowed to have SE*?\t[yes/no]\n""")
if(choice_1 == "yes" or choice_1 == "Yes" or choice_1 == "YES" or choice_1 == "y" or choice_1 == "Y"):
    pyttsx3.speak("enter your age")
    age = int(input("Enter your age:"))
    if(age >= 18):
        print("YOU CAN HAVE FUN!")
        pyttsx3.speak("congrats man!")
    elif(age == 0):
        print("You are just born.\n You can only do it once you are 18.")
    elif(age < 0):
        print("You are not born yet.")
    elif(age < 18 and age > 0):
        print("Be patient till the time comes.")
        if(18-age==1):
            print("The coming year is YOURS.")
        else:
            print("Wait for",18-age,"years.")
    else:
        print("INVALID INPUT")
        pyttsx3.speak("ivalid input")
        pyttsx3.speak("please try again")
else:
    print("Then there is none of your business here.")
    pyttsx3.speak("get,lost")
print("Good-bye!")

