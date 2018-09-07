"""
76. Minimum Window Substring 包含子串的最小窗口
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        appeared_count = [0] * 256
        expected_count = [0] * 256
        appeared = 0
        for ch in t:
            expected_count[ord(ch)] += 1
        start = 0
        minLen = 0xffffffff
        min_start = 0
        for end in range(len(s)):
            ind = ord(s[end])
            if expected_count[ind] > 0:
                appeared_count[ind] += 1
                if appeared_count[ind] <= expected_count[ind]:
                    appeared += 1
            if appeared == len(t):
                while appeared_count[ord(s[start])] > expected_count[ord(s[start])] or expected_count[ord(s[start])] == 0:
                    appeared_count[ord(s[start])] -= 1
                    start += 1
                if end - start + 1 < minLen:
                    minLen = end - start + 1
                    min_start = start
        if minLen == 0xffffffff:
            return ""
        else:
            return s[min_start: min_start + minLen]

s = Solution()
S = "ADOBECODEBANC"
T = "ABC"
res = s.minWindow(S, T)
print(res)


