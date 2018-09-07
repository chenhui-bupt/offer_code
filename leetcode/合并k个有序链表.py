# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        pNode = pMerged = ListNode(0)
        while q.qsize() > 0:
            pNode.next = q.get()[1]
            pNode = pNode.next
            if pNode.next:
                q.put((pNode.next.val, pNode.next))
        return pMerged.next