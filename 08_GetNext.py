# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetPreNext(self, pNode):  # 根-左-右
        if pNode.left:  # 有左节点，下一个就是左节点
            pNext = pNode.left
        elif pNode.right:  # 否则有右节点，下一个就是右节点
            pNext = pNode.right
        else:  # 否则就要往上层寻找
            pParent = pNode.next
            while pParent and pParent.left != pNode:  # 往上寻找直到子树是父节点的左子树
                pNode = pParent
                pParent = pParent.next
            if pParent and pParent.right:  # 如果父亲存在，且父节点有右节点，则下一个是右节点
                pNext = pParent.right
            else:  # 否则就是空（因为pNode是前序中最后一个节点）
                pNext = None
        return pNext

    def GetInNext(self, pNode):
        # write code here
        if not pNode:
            return
        if pNode.right:  # 有右子节点
            pNext = pNode.right
            while pNext.left:
                pNext = pNext.left
        else:  # 无右子节点
            pParent = pNode.next
            while pParent and pParent.right == pNode:
                pNode = pParent
                pParent = pParent.next
            pNext = pParent
        return pNext

    def GetPostNext(self, pNode):
        if not pNode:
            return
        pParent = pNode.next
        if not pParent:
            pNext = None
        else:
            if pParent.right:
                if pParent.right == pNode: # 是右节点，下一个是父节点
                    pNext = pParent
                else:  # 是左节点， 下一个是右兄弟节点
                    pNext = pParent.right
                    stack1 = []
                    stack2 = []
                    stack1.append(pNext)
                    while stack1:
                        node = stack1.pop()
                        stack2.append(node)
                        if node.left:
                            stack1.append(node.left)
                        if node.right:
                            stack1.append(node.right)
                    pNext = stack2[-1]
            else:  # 没有右兄弟节点，下一个就是父节点
                pNext = pParent
        return pNext


node1 = TreeLinkNode(8)
node2 = TreeLinkNode(6)
node3 = TreeLinkNode(10)
node4 = TreeLinkNode(5)
node5 = TreeLinkNode(7)
node6 = TreeLinkNode(9)
node7 = TreeLinkNode(11)
node1.left = node2
node1.right = node3
node2.next = node1
node2.left = node4
node2.right = node5
node3.next = node1
node3.left = node6
node3.right = node7
node4.next = node2
node5.next = node2
node6.next = node3
node7.next = node3

s = Solution()
res1 = s.GetPreNext(node1)
res2 = s.GetPreNext(node2)
res3 = s.GetPreNext(node3)
res4 = s.GetPreNext(node4)
res5 = s.GetPreNext(node5)
res6 = s.GetPreNext(node6)
res7 = s.GetPreNext(node7)
print(res1.val if res1 else 'null')
print(res2.val if res2 else 'null')
print(res3.val if res3 else 'null')
print(res4.val if res4 else 'null')
print(res5.val if res5 else 'null')
print(res6.val if res6 else 'null')
print(res7.val if res7 else 'null')

res1 = s.GetPostNext(node1)
res2 = s.GetPostNext(node2)
res3 = s.GetPostNext(node3)
res4 = s.GetPostNext(node4)
res5 = s.GetPostNext(node5)
res6 = s.GetPostNext(node6)
res7 = s.GetPostNext(node7)
print(res1.val if res1 else 'null')
print(res2.val if res2 else 'null')
print(res3.val if res3 else 'null')
print(res4.val if res4 else 'null')
print(res5.val if res5 else 'null')
print(res6.val if res6 else 'null')
print(res7.val if res7 else 'null')
