# -*- coding:utf-8 -*-
# 因为队列要先入先出，所以栈1杯底的沙子想要取出来，必须把它倒在栈2里，这样栈2栈顶的沙子就是最早的沙子
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):  # 时间复杂度低
        # return xx
        if not self.stack2:
            while self.stack1:
                node = self.stack1.pop()
                self.stack2.append(node)
        if self.stack2:
            xx = self.stack2.pop()
        else:
            xx = None
        return xx

    # def pop2(self):  # 时间复杂度较高
    #     # return xx
    #     while self.stack1:
    #         node = self.stack1.pop()
    #         self.stack2.append(node)
    #     if self.stack2:
    #         xx = self.stack2.pop()
    #     else:
    #         xx = None
    #     while self.stack2:  # 再给放回stack1, 安全，防止多次压入队列后才有一次弹出操作出现错误
    #         node = self.stack2.pop()
    #         self.stack1.append(node)
    #     return xx
