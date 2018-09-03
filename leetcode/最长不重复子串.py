class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        start = 0
        used = dict()
        maxLen = 0
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            used[s[i]] = i
        return maxLen

s = Solution()
ss = "abcabcbb"
res = s.lengthOfLongestSubstring(ss)
print(res)
ss = "bbbbb"
res = s.lengthOfLongestSubstring(ss)
print(res)

ss = "pwwkew"
res = s.lengthOfLongestSubstring(ss)
print(res)
