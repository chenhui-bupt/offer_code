nums = [10, 9, 7, 8, 6, 5, 3, 4, 2, 1]

nums = list(range(1, 7))
killed = True
night = 0
while killed and len(nums) > 1:
    killed = False
    tmp = []
    tmp.append(nums[0])
    i = 0
    while i < len(nums):
        while i < len(nums) - 1 and nums[i] > nums[i + 1]:
            i += 1
            killed = True
        i += 1
        if i < len(nums):
            tmp.append(nums[i])
        while i < len(nums) - 1 and nums[i] < nums[i + 1]:
            i += 1
            tmp.append(nums[i])
    nums = tmp[::]
    if killed:
        night += 1
    print(tmp, killed)
print(night)