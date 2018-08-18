# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return s
        newStr = []
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == ' ':
                newStr.insert(0, '0')
                newStr.insert(0, '2')
                newStr.insert(0, '%')
            else:
                newStr.insert(0, ch)
        return ''.join(newStr)
