"""
出现次数大于N/k的数
https://blog.csdn.net/u013309870/article/details/69788342
"""

def MoreThanN_K(arr, k):
    res = list()
    hashMap = dict()
    for i in range(len(arr)):
        if arr[i] in hashMap:
            hashMap[arr[i]] += 1
        else:
            if len(hashMap) == k-1:
                for key in list(hashMap.keys()):
                    val = hashMap[key]
                    if val == 1:
                        hashMap.pop(key)
                    else:
                        hashMap[key] = val - 1
            else:
                hashMap[arr[i]] = 1  # 相当于"超过一半的数"中count=0
    for key, val in hashMap.items():
        hashMap[key] = 0
    for i in range(len(arr)):
        if arr[i] in hashMap:
            hashMap[arr[i]] += 1
    for key, val in hashMap.items():
        if val > len(arr) // k:
            res.append(key)
    return res

arr = [1 ,2 ,3 ,3 ,5 ,2 ,2 ,3 ,3 ,3 ,5 ,6 ,2 ,2 ,2 ,3 , 3]
k = 3
res = MoreThanN_K(arr, k)
print(res)
