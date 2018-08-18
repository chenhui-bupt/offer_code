# -*- coding:utf-8 -*-
# 面试题16：数值的整数次方，幂乘运算（考察二分法）


class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent % 2 == 0:
            result = self.Power(base, abs(exponent) // 2) ** 2
        else:
            result = self.Power(base, abs(exponent) // 2) ** 2 * base
        if exponent < 0:
            result = 1.0 / result
        return result

    # def Power2(self, base, exponent):
    #     # write code here
    #     global errorFlag
    #     errorFlag=False
    #     if exponent<0 and base==0:
    #         errorFlag=True
    #         return 0.0
    #     result = self.PowerWithUnsignedExponent(base,abs(exponent))
    #     if exponent<0:
    #         result=1.0/result
    #     return result
    # def PowerWithUnsignedExponent(self,base,exponent):
    # #递归：n为偶数，a^n=a^n/2*a^n/2;n为奇数，a^n=（a^（n-1）/2）*（a^（n-1/2））*a, 时间复杂度O（logn）
    #     if exponent == 0:
    #         return 1
    #     if exponent == 1:
    #         return base
    #     result=self.PowerWithUnsignedExponent(base,exponent>>1)
    #     result*=result
    #     if(exponent&0x01==1):
    #         result*=base
    #     return result

s = Solution()

print(s.Power(3,1))