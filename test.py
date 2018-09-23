"""
出现次数超过N?K的数
"""

def moreThanN_K(nums, k):
    hashMap = {}
    for i in range(len(nums)):
        if nums[i] in hashMap:
            hashMap[nums[i]] += 1
        else:
            if len(hashMap) == k-1:
                for key in list(hashMap.keys()):
                    hashMap[key] -= 1
                    if hashMap[key] == 0:
                        hashMap.pop(key)
            else:
                hashMap[nums[i]] = 1
    for key in hashMap:
        hashMap[key] = 0
    for num in nums:
        if num in hashMap:
            hashMap[num] += 1
    res = [key for key, val in hashMap.items() if val > len(nums)//k]
    return res

arr = [1 ,2 ,3 ,3 ,5 ,2 ,2 ,3 ,3 ,3 ,5 ,6 ,2 ,2 ,2 ,3 , 3]
k = 3
res = moreThanN_K(arr, k)
print(res)
