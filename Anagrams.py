string1=input("Enter first sentence: ")
string2=input("Enter second sentence: ")
d=0
if True:
    for i in string1:
        if i.isalpha():
            if i not in string2:
                d=1
if d==1:
    print("Not Anagrams")
else:
    print("Anagrams")
