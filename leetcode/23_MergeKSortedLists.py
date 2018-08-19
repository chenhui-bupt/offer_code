"""
https://leetcode.com/problems/merge-k-sorted-lists/description/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        p = l = ListNode(0)
        points = lists[::]
        while True:
            minInd = None
            minVal = 0xffffffff
            for i in range(len(points)):
                if points[i] and points[i].val < minVal:
                    minVal = points[i].val
                    minInd = i
            if minInd is None:
                break
            p.next = points[minInd]
            p = p.next
            points[minInd] = points[minInd].next
        return l.next


