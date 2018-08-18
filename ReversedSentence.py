# -*- coding:utf-8 -*-
# 先整体反转再局部反转
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None:
            return ""
        s = list(s)
        b = 0
        e = len(s) - 1
        while b < e:
            s[b], s[e] = s[e], s[b]
            b += 1
            e -= 1
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            b = e = i
            while i < len(s) and s[i] != ' ':
                e += 1
                i += 1
            e -= 1
            while b < e:
                s[b], s[e] = s[e], s[b]
                b += 1
                e -= 1
        return ''.join(s)


s = Solution()
res = s.ReverseSentence("wonderful")
print(res)

