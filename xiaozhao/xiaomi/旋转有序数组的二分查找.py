def searchInRotateArray(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[left]:  # 左侧有序
            if nums[left] < target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # target < nums[left]  # 右侧有序
            if nums[mid] < target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

nums = [15,16,19,20,25,1,3,4,5,7,10,14]
target = 5
res = searchInRotateArray(nums, target)
print(res)

