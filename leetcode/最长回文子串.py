"""
5. longest palindromic substring
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        maxStr = ""
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > maxLen:
                maxLen = right - left - 1
                maxStr = s[left + 1: right]
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > maxLen:
                maxLen = right - left - 1
                maxStr = s[left + 1: right]
        return maxStr

s = Solution()
ss = "babad"
res = s.longestPalindrome(ss)
print(res)
