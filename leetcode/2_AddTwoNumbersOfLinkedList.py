"""
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return
        l = ListNode(0)
        p1, p2, p = l1, l2, l
        carry = 0
        while p1 and p2:
            tsum = p1.val + p2.val + carry
            carry = 1 if tsum >= 10 else 0
            tsum = tsum - 10 if tsum >= 10 else tsum
            p.next = ListNode(tsum)
            p = p.next
            p1 = p1.next
            p2 = p2.next
        while p1:
            tsum = p1.val + carry
            carry = 1 if tsum >= 10 else 0
            tsum = tsum - 10 if tsum >= 10 else tsum
            p.next = ListNode(tsum)
            p = p.next
            p1 = p1.next
        while p2:
            tsum = p2.val + carry
            carry = 1 if tsum >= 10 else 0
            tsum = tsum - 10 if tsum >= 10 else tsum
            p.next = ListNode(tsum)
            p = p.next
            p2 = p2.next
        if carry:
            p.next = ListNode(1)
        return l.next
