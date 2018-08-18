# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return
        pNode = pHead
        pPre = None # 初始为None，因为头节点变尾节点
        while(pNode): # 最后尾节点继续反转，变长pPre，退出while
            pNext = pNode.next # 保存下一个节点
            pNode.next = pPre # 断开pNode和pNext，并将pNode与pPre相连，实现反转
            pPre = pNode # pPre 更新变长（已反转的链表）
            pNode = pNext # pNode 更新为剩余未反转的链表
        return pPre # 全部反转
    