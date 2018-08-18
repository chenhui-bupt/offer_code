# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s is None or pattern is None:
            return False
        return self.matchCore(s, 0, pattern, 0)

    def matchCore(self, s, strIndex, pattern, patternIndex):
        if strIndex == len(s) and patternIndex == len(pattern):  # 匹配
            return True
        if strIndex != len(s) and patternIndex == len(pattern):  # 如果正则结束了而字符串没结束，返回False
            return False
        if patternIndex < len(pattern) - 1 and pattern[patternIndex + 1] == '*':  # 第二个是'*'
            if (strIndex != len(s) and s[strIndex] == pattern[patternIndex]) or \
                    (strIndex != len(s) and pattern[patternIndex] == '.'):
                return self.matchCore(s, strIndex, pattern, patternIndex + 2) or \
                       self.matchCore(s, strIndex + 1, pattern, patternIndex)  # 匹配0个或多个
            else:
                return self.matchCore(s, strIndex, pattern, patternIndex + 2)  # 匹配0个
        if (strIndex != len(s) and s[strIndex] == pattern[patternIndex]) or \
                (strIndex != len(s) and pattern[patternIndex] == '.'):
            return self.matchCore(s, strIndex + 1, pattern, patternIndex + 1)  # 匹配一个
        return False
