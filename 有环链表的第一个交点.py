# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        enter1 = self.getEnterNode(headA)
        enter2 = self.getEnterNode(headB)
        if not enter1 and not enter2:
            return self.getIntersection(headA, headB)
        elif not enter1 or not enter2:
            return None
        else:
            if enter1 == enter2:
                return self.getIntersection(headA, headB, tail=enter1)
            else:
                p1 = enter1
                while p1 != enter2 and p1.next != enter1:  # 走一圈看p1能否找到enter2
                    p1 = p1.next
                if p1 == enter2:  # 找到
                    return p1
                else:  # 未找到，即没有交点
                    return None

    def getEnterNode(self, head):
        p1 = head
        p2 = head.next
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
        if p1 != p2:
            return None
        p1 = head
        p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def getIntersection(self, headA, headB, tail=None):
        a = headA
        b = headB
        while a != b:
            a = a.next if a != tail else headB
            b = b.next if b != tail else headA
        return a

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

"""
1. 均无环
2. 一个有环一个无环，没有交点
3. 均有环
    3.1 交点在环内，则环的入口节点即是第一个交点
    3.2 交点不在环内，此时enter1=enter2，则将入口节点作为链表尾部
    3.3 没有交点
"""

# 均无环
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node6.next = node7
node7.next = node2
s = Solution()
res = s.getIntersectionNode(node1, node6)
print(res.val)

# 两个均有环，交点在环上
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3
node7.next = node5
res = s.getIntersectionNode(node1, node7)
print(res.val)

# 两个均有环，交点在环外
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3
node7.next = node2
res = s.getIntersectionNode(node1, node7)
print(res.val)

# 两个均有环，但没有交点
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

node5.next = node6
node6.next = node7
node7.next = node6

res = s.getIntersectionNode(node1, node5)
if res:
    print(res.val)
else:
    print(res)
