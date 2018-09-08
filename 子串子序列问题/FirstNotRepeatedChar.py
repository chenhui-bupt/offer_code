"""
第一个只出现一次的字符
"""
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        res = {}
        for i in range(len(s)):
            res[s[i]] = res.get(s[i], 0) + 1
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
        return -1
