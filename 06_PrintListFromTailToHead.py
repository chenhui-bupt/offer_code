# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 循环
    def printListFromTailToHead(self, listNode):
        # write code here
        value = []
        while listNode:
            value.insert(0, listNode.val)
            listNode = listNode.next
        return value

    # 递归，链表过长时，导致函数调用层级很深，函数调用栈溢出
    def printListFromTailToHead2(self, listNode):
        self.value = []
        if not listNode:
            return []
        self.printListFromTailToHead2(listNode.next) # 先递归尾部节点，再输出头节点
        self.value.append(listNode.val)
        return self.value


s = Solution()
listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next = ListNode(3)
print(s.printListFromTailToHead(listNode))
print(s.printListFromTailToHead2(listNode))
