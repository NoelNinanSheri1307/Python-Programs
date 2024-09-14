k=int(input("Enter number of terms: "))
l=[]
o=[]
for i in range(k):
    a=input("Enter string: ")
    l.append(a)
d={}
for i in l:
    d[i]=len(i)
f=[]
for i in d:
    f.append(d[i])
for i in range(k):
    for j in f:
        y=min(f)
        for b in d:
            if d[b]==y:
                mins=b
                o.append(b)
        f.remove(min(f))
print(o)
    
