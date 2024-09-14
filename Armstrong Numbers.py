n=int(input())
s=0
temp=n
while n!=0:
    dig=n%10
    s=s+(dig**3)
    n=n//10
if temp==s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
