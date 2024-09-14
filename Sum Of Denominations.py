a=int(input("Enter amount "))
l = [2000, 1000,500, 200, 100, 50, 20, 10, 5, 2, 1]
d = {}
for i in l:
        d[i] = 0
for i in l:
    if a >= i:
        count = a// i
        a -= count * i
        d[i] = count
for i in d:
    print(i,d[i])


