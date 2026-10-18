def sum_to_n(n):
    if n==1:
        return 1
    return n+sum_to_n(n-1)
n= int(input("Enter a number:"))
print(f"Sum is {sum_to_n(n)}")