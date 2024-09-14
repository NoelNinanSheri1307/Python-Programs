n=int(input())
k=n-1
for i in range(n-1):
    for j in range(k):
        print(" ",end="")
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print()
for i in range(n,0,-1):
    for j in range(k):
        print(" ",end="")
    k=k+1
    for j in range(i,0,-1):
        print("* ",end="")
    print()
