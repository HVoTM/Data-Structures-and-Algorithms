nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
temp = nums[n-k:n]
print(temp)

for i in range(len(nums)-k):
    temp.append(nums[i])

nums = temp
print(nums)