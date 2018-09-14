class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        i = 0
        sign = 1
        res = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i < len(str):
            if str[i] == '+':
                i += 1
            elif str[i] == '-':
                sign = -1
                i += 1
        dotNum = 0
        while i < len(str) and ('0' <= str[i] <= '9' or str[i] == '.'):
            if str[i] == '.':
                dotNum += 1
            if dotNum == 0:
                res = res * 10 + int(str[i])
            elif dotNum > 1:
                return 0
            i += 1
        while i < len(str):
            if '0' <= str[i] <= '9':
                print("dot")
                return 0
            i += 1
        res = res * sign
        if res < -0x80000000:
            res = -0x80000000
        elif res > 0x7fffffff - 1:
            res = 0x7fffffff - 1
        return res


s = Solution()
str = "  -0012a42"
res = s.myAtoi(str)
print(res)