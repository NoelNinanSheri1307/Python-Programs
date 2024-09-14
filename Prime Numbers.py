def prime(n):
    if n==0:
        print("Concept of prime numbers not applicable to 0")
    elif n<1:
        print("Concept of prime numbers not applicable to negative numbers")
    elif n==1:
        print("1 is neither prime nor composite")
    elif n==2:
        print("2 is a prime number")
    elif n==2:
        print("3 is a prime number")
    else:
        flag=0
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
        if flag==1:
            print(n,"is composite")
        else:
            print(n,"is prime")
n=int(input("Enter a number: "))
prime(n)

