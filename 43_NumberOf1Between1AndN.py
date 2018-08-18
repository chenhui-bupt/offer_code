# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        i = 1
        while(i <= n):
            a = n/i
            b = n%i
            count += (a+8)/10 * i + (a%10 == 1)*(b+1)
            i *= 10
        return count


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n:
            return 0
        res = 0
        i = 1
        while i <= n:
            a = n // i
            b = n % i
            if a % 10 > 1:  # 判断有没有大于一，即后i位会有多少个00...0 ~ 99...9 (i个9）
                res += (a/10 + 1) * i
            elif a % 10 == 1:  # 否则最后一次为1的时候末尾只能是b
                res += (a/10) * i + b + 1
            else:
                res += (a/10) * i
            i *= 10
        return res
