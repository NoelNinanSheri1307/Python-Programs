def fibonacci (n):
   lst=[0,1]
   if n==1:
       print(0)
   elif n==2:
        print(0,1)
   else:
        while len(lst)<n:
            x=lst[-1]+lst[-2]
            lst.append(x)
        for i in lst:
            print(i,end=" ")
n=int(input("Enter a number: "))
fibonacci(n)
