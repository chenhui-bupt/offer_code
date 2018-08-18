# -*- coding:utf-8 -*-
#  面试题15： 二进制中1的个数
class Solution:
    def NumberOf1_chenhui(self, n):
        # write code here
        count=0
        flag=1
        if n<0:
            n=n&0xffffffff # 只取32位
        while(flag&0xffffffff):#最多移动flag 32次
            if(flag&n):
                count+=1
            flag=flag<<1
        return count

    def NumberOf1(self, n):
# write code here
        count=0
        flag=1
        if n<0:
            n=n&0xffffffff # 只取32位
        while(n):#n!=0,就说明n有1
            count+=1
            n=(n-1)&n #把最右边的1变为0
        return count
        
    def NumberOf1_bin2string(self,n):
        if n<0:
            n=n&0xffffffff
        string=bin(n)#返回二进制表示的字符串
        return string.count('1')# 计数
