class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dct = {'2': "abc", '3': 'def', '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = list(dct[digits[0]])
        for i in range(1, len(digits)):
            tmp = []
            for ch in dct[digits[i]]:
                for s in res:
                    tmp.append(s+ch)
            res = tmp[::]
        return res
    