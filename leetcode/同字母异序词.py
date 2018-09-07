"""
Group Anagram
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        hashMap = dict()
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            tmp = tuple(count)
            if tmp not in hashMap:
                hashMap[tmp] = []
            hashMap[tmp] = hashMap[tmp] + [s]
        return hashMap.values()
