# -*- coding:utf-8 -*-
# 面试题18：删除链表的节点
class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, val):
        self.value = val
        self.next = None

    def __del__(self):
    	self.value = None
    	self.next = None

class Solution(object):
    """docstring for Solution"""
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return
        if pToBeDeleted.next: # 不是尾节点
            pNext = pToBeDeleted.next
            pToBeDeleted.value = pNext.value
            pToBeDeleted.next = pNext.next
            pNext.__del__()
        elif pToBeDeleted == pListHead: # 既是尾节点又是头节点，直接删除链表
            pListHead.__del__()
            pToBeDeleted.__del__()
        else:  # 是尾节点，遍历到倒数第二个节点，并删除尾节点
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None # 倒数第二个节点尾指针为空，并删除尾节点
            pToBeDeleted.__del__()


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4



s = Solution()
s.DeleteNode(node1, node3)
print(node3.value)
s.DeleteNode(node1, node3)
print(node3.value)
print(node2.value)
print(node2.next.value)
s.DeleteNode(node1, node1)
print(node1.value)
s.DeleteNode(node1, node1)
print(node1.value)





