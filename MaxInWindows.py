# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not sum or not size:
            return []
        stack = []
        res = []
        for i in range(len(num)):
            while stack and num[stack[-1]] <= num[i]:
                stack.pop()
            while stack and stack[0] + size - 1 < i:
                stack.pop(0)
            stack.append(i)
            if stack and i + 1 >= size:
                res.append(num[stack[0]])
            print( stack)
        return res

s = Solution()
res = s.maxInWindows([2,3,4,2,6,2,5,1], 3)
print(res)
