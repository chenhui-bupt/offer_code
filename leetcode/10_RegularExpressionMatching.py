class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return False
        return self.helper(s, 0, p, 0)

    def helper(self, s, sInd, p, pInd):
        if len(s) == sInd and len(p) == pInd:
            return True
        if len(p) == pInd:
            return False
        if pInd + 1 < len(p) and p[pInd + 1] == '*':
            if (sInd < len(s) and s[sInd] == p[pInd]) or (sInd < len(s) and p[pInd] == '.'):
                return self.helper(s, sInd, p, pInd + 2) or self.helper(s, sInd + 1, p, pInd)
            else:
                return self.helper(s, sInd, p, pInd + 2)
        if (sInd < len(s) and s[sInd] == p[pInd]) or (sInd < len(s) and p[pInd] == '.'):
            return self.helper(s, sInd + 1, p, pInd + 1)
        return False
