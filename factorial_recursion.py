def factorial(n): #     if n! = 5!
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1) #   n! = n*(n-1)!     //      5! = 5 x 4!     //      fact(5) == 5*fact(4)


n = int(input("Enter a number: "))
print(f"Factorial is: {factorial(n)}")