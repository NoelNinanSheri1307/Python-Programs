s=input("Enter the string: ")
l=[]
for i in s:
    l.append(i)
e=l
l.reverse()
d=""
for i in l:
    d=d+i
if s==d:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
print(e==l)
