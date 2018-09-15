n = int(input())
nums = [int(input()) for i in range(n)]
hashMap = dict()
for num in nums:
    if num not in hashMap:
        hashMap[num] = 0
for num in nums:
    for k in hashMap:
        if num < k:
            hashMap[k] += num
for i in range(len(nums)):
    print(hashMap[nums[i]])
