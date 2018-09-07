
import random
def sample(nums, k):
    res = []
    for i in range(len(nums)):
        if i < k:
            res.append(nums[i])
        else:
            j = random.randint(0, i)
            if j < k:
                res[j] = nums[i]
    return res

nums = list(range(100))
k = 5
res = sample(nums, k)
print(res)


def sample0(nums):
    res = nums[0]
    for m in range(1, len(nums)):
        p = random.random()
        if p < 1/(m + 1):
            res = nums[m]
    return res
