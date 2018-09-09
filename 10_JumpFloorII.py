# -*- coding:utf-8 -*-
# 找到递推关系式，fn = Σ_{i = 1}^{n-1} fi + 1
# 所以fn = 2 * fn-1

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 1:
            return 0
        results = []
        results.append(1)
        if number < 2:
            return results[number - 1]
        for i in range(2, number + 1):
            results.append(sum(results) + 1)
        return results[-1]

    def jumpFloorII(self, number):
        if number < 1:
            return 0
        temp = 1
        if number < 2:
            return temp
        return pow(2, number - 1) * 1
s = Solution()
res = s.jumpFloorII(9)
print(res)