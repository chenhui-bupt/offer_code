
def helper(n, nums):
    res = 0
    for i in range(n):
        if nums[i] < 18000:
            num = 0
            temp = nums[i] + 18000
            for j in range(i + 1, n):
                if nums[j] < temp:
                    # print(nums[j])
                    num += 1
            # print("num", num)
            res += (num-1) *num //2
            # print(res)
    for i in range(n):
        if nums[i] >= 18000:
            num = 0
            temp = nums[i] - 18000
            for j in range(i + 1, n):
                if nums[j] > temp:
                    num += 1
            res += (num-1) * num //2
    return res

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()
# print(nums)
res = helper(n, nums)
print(res)