# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        map_dict = dict()
        for ch in s:
            map_dict[ch] = map_dict.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if map_dict[ch] == 1:
                return i
        return -1
