#FOR LOOP
n = int(input("Enter a number:"))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(f"FACTORIAL of {n} is {fact}")


#WHILE LOOP
n = int(input("Enter a number:"))
fact = 1
i = 1
while i<=n:
    fact = fact*i
    i+=1
print(f"FACTORIAL of {n} is {fact}")


