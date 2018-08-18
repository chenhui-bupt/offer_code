# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        meetingNode = self.MeetingNode(pHead)
        if not meetingNode:
            return None
        nodesInLoop = 1 # 起始为1
        pNode = meetingNode.next
        while(pNode != meetingNode): # 利用环中相遇节点，当再次经过该节点时，就知道环中节点的个数
            pNode = pNode.next
            nodesInLoop += 1
        pNode1 = pHead
        pNode2 = pHead
        for i in range(nodesInLoop): # 知道环中节点个数，用两个指针一快一慢，一个先走n步，他们会在环入口节点处相遇
            pNode1 = pNode1.next
        while pNode1 != pNode2: # 他们会在环入口节点处相遇
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode2
    
    def MeetingNode(self, pHead):
        if pHead is None:
            return None
        pSlow = pHead
        pFast = pSlow.next
        while(pSlow and pFast):
            if pSlow == pFast:
                return pFast # 找到环中相遇节点
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next # 走两步
        return None
    