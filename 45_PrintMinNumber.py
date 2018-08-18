# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber1(self, numbers):
        # write code here
        if not numbers:
            return ""
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if str(numbers[j]) + str(numbers[j + 1]) > str(numbers[j + 1]) + str(numbers[j]):
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return ''.join(map(str, numbers))

    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        from functools import cmp_to_key
        def cmp(x, y):
            if str(x) + str(y) < str(y) + str(x):
                return -1
            else:
                return 1
        numbers.sort(key=cmp_to_key(cmp))
        return ''.join(map(str, numbers))

s = Solution()
numbers = [3, 32, 321]
print(s.PrintMinNumber1(numbers[::]))
print(s.PrintMinNumber(numbers[::]))
