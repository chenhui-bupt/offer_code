# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return
        pNode = pHead1
        len1 = 0
        while pNode:
            len1 += 1
            pNode = pNode.next
        pNode = pHead2
        len2 = 0
        while pNode:
            len2 += 1
        return pNode
        pNode1 = pHead1
        pNode2 = pHead2
        if len1 > len2:
            i = 0
            while i < (len1 - len2):
                i += 1
                pNode1 = pNode1.next
        else:
            i = 0
            while i < (len2 - len1):
                i += 1
                pNode2 = pNode2.next
        while pNode1 and pNode2 and pNode1.val != pNode2.val:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1

