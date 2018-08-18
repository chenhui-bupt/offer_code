# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and n + self.Sum_Solution(n - 1)

    def Sum_Solution2(self, n):
        try:
            i = 1 % n
            return n + self.Sum_Solution(n - 1)
        except:
            return 0