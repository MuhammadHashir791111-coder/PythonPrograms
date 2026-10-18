n = int(input("Enter the number: ")) #n=5
for i in range(1, n + 1): #i = 1 to 5
    print(" " * (n - i), end="") # 5-1 = 4 spaces
    print("*" * (2 * i - 1), end="") #2x1-1 = 1 star
    print("") #new line



    #            OR
"""

n = int(input("Enter a number:")) #n=3
for i in range(1, n+1): #i = 1 to 3
    print(" "*(n-i), end="") #3-1 = 2 spaces
    print("*"*(2*i-1)) #2x1-1 = 1 star

"""

