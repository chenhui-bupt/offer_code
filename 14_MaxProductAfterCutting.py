#  -*- coding: utf-8 -*-
# 面试题14：剪绳子

class Solution:
    # 动态规划
    def maxProductAfterCutting(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        products = [0] * 4
        products[0] = 0
        products[1] = 1
        products[2] = 2 # 长度为2时不要剪，不剪比剪乘积大, 2 > 1*1
        products[3] = 3 # 长度为3时不要剪，不剪比剪乘积大, 3 > 1*2 > 1*1*1

        for i in range(4, length+1):
            maxProduct = 0
            for j in range(1, i//2 +1):
                product = products[j] * products[i-j]
                if maxProduct < product:
                    maxProduct = product
            products.append(maxProduct)
        return products[-1]

    # 贪婪算法
    def maxProductAfterCutting2(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        timesOf3 = length // 3 # 地板除
        if length - timesOf3 * 3 ==1: # 当剩下一段长为4的绳子时不要再剪成长为3的，因为2*2 > 3*1
        	timesOf3 -= 1
        timesOf2 = (length - timesOf3 * 3) // 2
        return pow(3, timesOf3) * pow(2, timesOf2)

s = Solution()
res = s.maxProductAfterCutting(5)
print(res)
for i in range(4, 20):
	print(i, s.maxProductAfterCutting(i))
	print(i, s.maxProductAfterCutting2(i))
