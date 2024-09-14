def reverse():
    n=int(input("Enter a number"))
    s=0
    while n!=0:
        dig=n%10
        s=s*10+dig
        n=n//10
    print(s)
reverse()

        
