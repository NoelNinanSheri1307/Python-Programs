import re
panno=input("Enter the pan number for verification: ")
if len(panno)>10 or len(panno)<10:
    print("Length of the entered Pan number should be 10")
    exit
elif re.search("[0-9]",panno[0:5]):
    print("The first 5 characters must be alphabets")
    exit
elif re.search("[A-Za-z]",panno[5:9]):
    print("The characters at 5,6,7,8 indexes must be numbers")
    exit
elif re.search("[0-9]",panno[-1]):
    print("The last character must be an alphabet")
    exit
else:
    print("Your pan card number",panno,"satisfies all conditions...It is Valid!")


