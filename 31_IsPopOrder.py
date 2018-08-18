# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return False
        if len(pushV) != len(popV):
            return False
        stack = [] # 辅助栈
        j = 0 # 外层压入，内层弹出
        for i in range(len(pushV)):
            stack.append(pushV[i]) # 压入栈一个元素
            i += 1
            while(j < len(popV) and stack[-1] == popV[j]): # 如果栈顶元素就是要弹出的，逐一弹出
                stack.pop()
                j += 1
        return len(stack) == 0

    def IsPopOrder2(self, pushV, popV):
        # write code here
        if  not pushV and popV:
            return False
        stack = [] # 辅助栈
        stack.append(pushV.pop(0))
        while(popV):
            if stack[-1] == popV[0]: # 如果弹出元素就是栈顶元素，直接弹出
                stack.pop()
                popV = popV[1:]
            else: # 否则，现压入栈直到栈顶元素与弹出元素相同
                while(pushV and stack[-1] != popV[0]): #
                    stack.append(pushV.pop(0))
                if stack[-1] != popV[0]: # 如果压完pushV后，栈顶元素跟弹出元素仍不相同，返回False
                    return False
        if not pushV and not popV: # 当压入，弹出序列都执行完之后，返回True
            return True
    
s = Solution()
res = s.IsPopOrder([1,2,3], [3,2, 1,4])
a = list('abcdefg')
b = list('bagcefd')
print(s.IsPopOrder2(a,b))

