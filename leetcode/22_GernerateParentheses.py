class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = set(["()"])
        pattern = ["%s()", "(%s)", "()%s"]
        for i in range(1, n):
            tmp = set()
            for s in res:
                for p in pattern:
                    tmp.add(p % s)
            res = tmp.copy()
        return res

s = Solution()
res = s.generateParenthesis(3)
print(res)
