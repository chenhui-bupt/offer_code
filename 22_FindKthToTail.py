# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        p1List = head
        for i in range(k-1):
            if p1List.next:
                p1List = p1List.next
            else:
                return None
        p2List = head
        while p1List.next:
            p1List = p1List.next
            p2List = p2List.next
        return p2List
    