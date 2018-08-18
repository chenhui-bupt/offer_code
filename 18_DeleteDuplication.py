# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        if pHead.val == pHead.next.val:
            pNext = pHead.next
            while pNext and pNext.val == pHead.val:
                pNext = pNext.next
            pHead = self.deleteDuplication(pNext)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
        return pHead

    def deleteDuplication2(self, pHead):
        # write code here
        if not pHead:
            return
        pNode = pHead
        pPre = None
        while pNode:
            pNext = pNode.next
            if pNext and pNode.val == pNext.val:
                while pNext and pNode.val == pNext.val:
                    pNext = pNext.next
                if pPre:
                    pPre.next = pNext
                else:
                    pHead = pNext
            else:
                pPre = pNode
            pNode = pNext
        return pHead