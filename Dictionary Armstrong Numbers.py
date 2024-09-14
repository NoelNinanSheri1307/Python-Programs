n=int(input("Enter the number of terms in the list: "))
def armstrong(n):
    temp=n
    s=0
    while n!=0:
        dig=n%10
        s=s+dig**3
        n=n//1
    return(s)
l=[]
c=0
for i in range(n):
    a=int(input("Enter the term: "))
    l.append(a)
print("The list of inputed numbers is",l)
d={}
for i in l:
    if armstrong(i)==i:
        d[i]=c
    c+=1
for i in d:
    print(d)
