# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return
        if m==n: return head
        p1head = p1tail = ListNode(0)
        p1tail.next = head
        for i in range(1, m):
            p1tail = p1tail.next
        p2head = p1tail.next
        p2tail = None
        p3head = p2head
        for j in range(m, n+1):
            pnext = p3head.next
            p3head.next = p2tail
            p2tail = p3head
            p3head = pnext
        p1tail.next = p2tail
        p2head.next = p3head
        return p1head.next

