# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return
        result = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                result = numbers[i]
                times = 1
            elif result == numbers[i]:
                times += 1
            else:
                times -= 1
        print("hehe", result)
        times = 0
        for num in numbers:
            if num == result:
                times += 1
        if times > len(numbers) >> 1:
            return result
        else:
            return 0
        
s = Solution()
arr = [3,1,3,2,3]
print(s.MoreThanHalfNum_Solution(arr))