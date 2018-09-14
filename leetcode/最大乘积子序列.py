nums = [2, 3, -2, -2, 4, 5]
def func(nums):
    gmax = tmin = tmax = nums[0]
    print(tmin, tmax)
    for i in range(1, len(nums)):
        tmpmin = min(tmin, tmin * nums[i], tmax * nums[i])
        tmpmax = max(tmax, tmin * nums[i], tmax * nums[i])
        tmin, tmax = tmpmin, tmpmax
        print(tmin, tmax)
        if tmax > gmax:
            gmax = tmax
    return gmax

res = func(nums)
print(res)

nums = [2, 3, -2, 2, 4, 5]
res = func(nums)
print(res)
