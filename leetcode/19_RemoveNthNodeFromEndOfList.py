# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return
        if n == 0:
            return head
        i = 0
        p1 = head
        while i < n:
            if not p1:
                return
            p1 = p1.next
            i += 1
        if not p1:
            return head.next
        p2 = head
        pre = None
        while p1:
            p1 = p1.next
            pre = p2
            p2 = p2.next
        pre.next = p2.next
        return head
