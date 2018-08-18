# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric1(self, s):
        # write code here
        if not s:
            return False
        import re
        matchObj = re.match(r'[\+-]?[0-9]*(\.[0-9]*)?([eE][\+-]?[0-9]+)?', s)
        if matchObj.group() == s:
            return True
        return False


    def isNumeric(self, s):
        if not s:
            return False
        s = [ch.lower() for ch in s]
        if 'e' in s:
            eIndex = s.index('e')
            front = s[:eIndex]
            behind = s[eIndex + 1:] # 列表的截取操作不会越界
            if '.' in behind or len(behind) == 0: # 指数部分有小数点或者长度为0， 均返回False
                return False
            isFront = self.scanDigit(front)
            isBehind = self.scanDigit(behind)
            if isFront and isBehind:
                return True
        isNum = self.scanDigit(s)
        return isNum
    
    def scanDigit(self, s):
        dotNum = 0
        for i in range(len(s)):
            if not ('0'<= s[i] <= '9' or s[i] in '+-.'): # 不是规定的字符，返回False
                return False
            if s[i] in '+-' and i != 0: # 不在头部出现'+-'正负号， 返回False
                return False
            if s[i] == '.':
                dotNum += 1
        if dotNum > 1: # 小数点个数大于1个，返回False
            return False
        return True # 所有条件均不满足，返回True


s = Solution()
print(s.isNumeric('+123.4e+56'))
print(s.isNumeric('+123.e+56'))
print(s.isNumeric('+.4e+56'))
print(s.isNumeric('.4e+56'))



