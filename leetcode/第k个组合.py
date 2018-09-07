"""
60. Permutation Sequence
"""
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n < 1 or n > 9:
            return
        if k < 1 or k > math.factorial(n):
            return
        res = []
        unused = list(range(1, n + 1))
        self.helper(n, k, unused, res)
        return ''.join(map(str, res))

    def helper(self, n, k, unused, res):
        k = k - 1
        while len(res) != n:
            cnt = k // math.factorial(n - len(res) - 1)
            k = k % math.factorial(n - len(res) - 1)
            res.append(unused[cnt])
            unused.remove(unused[cnt])

s = Solution()
n = 4
k = 9
res = s.getPermutation(n, k)
print(res)
