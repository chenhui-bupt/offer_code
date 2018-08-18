class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(': ')', '[': ']', '{': '}'}
        i = 0
        while i < len(s) - 1:
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] in pairs and pairs[s[l]] == s[r]:
                s = s[:l] + s[l +1: r] + s[r+ 1:]
                r = l
                l -= 1
            i = l + 1
        if not s:
            return True
        else:
            return False



s = Solution()
res = s.isValid("{()}")
print(res)
res = s.isValid("[({(())}[()])]")
print(res)
