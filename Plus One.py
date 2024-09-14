n=int(input("Enter the number of digits: "))
p=[]
for i in range(n):
    f=int(input())
    p.append(f)
s=""
for i in p:
    s=s+str(i)
k=str(int(s)+1)
l=[]
for j in k:
    l.append(int(j))
print(l)

