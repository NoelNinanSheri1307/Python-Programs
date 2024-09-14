l=[2000,500,200,100,50,20,10,5,2,1]
n=int(input("Enter the amount: "))
d={}
for i in l:
    d[i]=0
for i in l:
    if n>=i:
        d[i]=n//i
        n=n-(d[i]*i)
for i in d:
    print(i,':',d[i])

        
