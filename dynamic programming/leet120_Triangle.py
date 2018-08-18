class Solution(object):
    # 路径有两种方式，从上到下和从下到上
    def minimumTotal(self, triangle):  # 从上到下找最优路径
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        dp = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])


    def minimumTotal(self, triangle):  # 从下到上找最优路径
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        dp = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]
        dp[-1] = triangle[-1][::]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
