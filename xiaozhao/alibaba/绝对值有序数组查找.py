"""
绝对值有序的数组查找给定值，有则返回True，无则返回False
[1,2,4,-4,4,5]
"""

def find(nums, target):
    if not nums or target is None:
        return False
    return helper(nums, target, 0, len(nums) - 1)

def helper(nums, target, left, right):
    while left < right:
        mid = (left + right) //2
        if nums[mid] == target:
            return True
        elif abs(target) < abs(nums[mid]):
            right = mid - 1
        elif abs(target) > abs(nums[mid]):
            left = mid + 1
        else:
            return helper(nums, target, left, right-1) or helper(nums, target, left+1, right)
    return False

nums = [1,2,4,-4,4,5]
target = -4
res = find(nums, target)
print(res)
