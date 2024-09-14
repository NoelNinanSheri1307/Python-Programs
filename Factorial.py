#Factorial of a number

def factorial(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f
n=int(input("Enter a number: "))
if n<0:
    print("No factorial for negative numbers")
if n==0:
    print(0)
if n==1:
    print(1)
if n==2:
    print(2)
if n>2:
    print(factorial(n))
