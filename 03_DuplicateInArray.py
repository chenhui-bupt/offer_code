# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        for i in range(len(numbers)):
            while numbers[i] != i:  # 没有被放到正确位置
                print(numbers)
                if numbers[i] == numbers[numbers[i]]:  # 重复，因为numbers[numbers[i]]可能之前被重新放在正确位置上了
                    duplication[0] = numbers[i]
                    return True
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp  # 把number[i]放到正确的位置上（因为把数字放到本来的位置上，重复的数字就很容易发现了）
            print("...")
        return False

    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            while numbers[i] != numbers[numbers[i]]:
                tmp = numbers[i]
                numbers[i] = numbers[tmp]
                numbers[tmp] = tmp
            if i != numbers[i]:
                duplication[0] = numbers[i]
                return True
        return False

    def duplicate(self, numbers, duplication):  # 核心思想在原来数组上对每个数字进行计数
        # write code here
        for i in range(len(numbers)):
            index = numbers[i]
            if index >= len(numbers):
                index -= len(numbers)
            if numbers[index] >= len(numbers):
                duplication[0] = index
                return True
            numbers[index] += len(numbers)
        return False


s = Solution()
numbers = [2, 3, 1, 2, 5, 3]
duplication = [-1]
res = s.duplicate(numbers, duplication)
print(res, duplication)


print("""不用额外空间对数组元素计数""")
def count(nums):
    for i in range(len(nums)):
        index = nums[i] % len(nums)
        nums[index] += len(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] // len(nums)
nums = [2, 3, 1, 0, 2, 5, 3]
count(nums)
print(nums)