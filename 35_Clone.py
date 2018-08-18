# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pNode = pHead
        while pNode:
            label = pNode.label # 先复制出来一个节点
            pCloned = RandomListNode(label)
            pCloned.next = pNode.next
            pCloned.random = None
            
            pNode.next = pCloned # 放到pNode节点的后面
            pNode = pCloned.next # pNode节点移到下一个节点
        
        # 连接random指针
        pNode = pHead
        while(pNode):
            pCloned = pNode.next
            if pNode.random: # 如果有随机指针
                pCloned.random = pNode.random.next
            pNode = pCloned.next # pNode 移向下一节点
        
        # 断开新旧两个链表
        pNode = pHead
        pClonedHead = None
        pClonedNode = None
        if(pNode):
            pClonedHead = pNode.next
            pClonedNode = pClonedHead
            pNode.next = pClonedNode.next
            pNode = pNode.next
        while(pNode):
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead
    