# -*- coding:utf-8 -*-
# 面试题17：打印从1到最大的n位数
class Solution:
    # 用字符串或数组表示大数
    def print1ToMaxNDigits(self, n):
        if n < 0:
            return
        number = ['0'] * n
        while(self.increment(number) == False):
            self.printNumber(number)
        del number
  
    def increment(self, number):
        # 两个标志位进位标志位nTakeOver和溢出标志位isOverFlow（整个程序终止）
        isOverFlow = False
        nTakeOver = 0
        for i in range(len(number)-1, -1, -1): # 降序，要用第三个参数-1，循环进位用
            nSum = ord(number[i]) - ord('0') + nTakeOver
            if i == len(number)-1:
                nSum += 1
            if nSum >= 10:
                if i == 0: # 同时循环也终止，不用再break了
                    isOverFlow = True
                else:
                    nSum -= 10
                    nTakeOver = 1
                    number[i]  = chr(nSum + ord('0'))
            else:
                nTakeOver = 0
                number[i] = chr(nSum + ord('0'))
                break # 有没有break无所谓，increment函数只做一次自增运算（包括循环进位），
                # 有break会节约运算时间，不循环进位就跳出循环
        return isOverFlow

    def printNumber(self, number): # 0不需要打印
        isBeginWithZero = True
        for i in range(0, len(number)):
        	if isBeginWithZero and number[i] != '0': # if number[i] != '0': isBeginWithZero = False即可
        		isBeginWithZero = False
        	if not isBeginWithZero:
        		print(number[i], end='')
        print('\n')
        # print(''.join(number).replace(r'^0', ''))

s = Solution()
s.print1ToMaxNDigits(2)



