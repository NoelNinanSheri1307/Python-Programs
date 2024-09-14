def twoSum(nums,target):
    for i in nums:
        for j in nums:
            if i!=j:
                if i+j==target:
                    print([nums.index(i),nums.index(j)])
nums=[]
n=int(input("Enter the number of terms: "))
for i in range(n):
    m=int(input())
    nums.append(m)
target=int(input("Enter target Value: "))
twoSum(nums,target)
