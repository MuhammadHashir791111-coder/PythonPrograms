def pattern(n):
    if (n==0):
        return
    print("*"*n) # '*' x 5 = *****
    pattern(n-1) # '*' x (n-1)
n= int(input("Enter a number:"))
pattern(n)    
