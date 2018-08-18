# -*- coding:utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """docstring for Solution"""
    # 前序遍历
    def preOrder(self, pRoot):
        if not pRoot:
            return 
        print(pRoot.val)
        self.preOrder(pRoot.left)
        self.preOrder(pRoot.right)

    def preOrder2(self, pRoot):
        if not pRoot:
            return []
        stack = []
        stack.append(pRoot)
        while stack:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # 中序遍历
    def inOrder(self, pRoot):
        if not pRoot:
            return
        self.inOrder(pRoot.left)
        print(pRoot.val)
        self.inOrder(pRoot.right)

    def inOrder2(self, pRoot):
        if not pRoot:
            return
        stack = []
        pNode = pRoot
        while pNode or stack:
            if pNode:
                stack.append(pNode)
                pNode = pNode.left
            else:
                pNode = stack.pop()
                print(pNode.val)
                pNode = pNode.right

    def postOrder(self, pRoot):
        if not pRoot:
            return
        self.postOrder(pRoot.left)
        self.postOrder(pRoot.right)
        print(pRoot.val)

    def postOrder2(self, pRoot):
        if not pRoot:
            return
        stack1 = []
        stack2 = []
        stack1.append(pRoot)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().val)
import numpy as np
np.random.randint()
s = Solution()
pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
s.preOrder(pNode1)
print("------")
s.preOrder2(pNode1)
print("------")
s.inOrder(pNode1)
print("------")
s.inOrder2(pNode1)
print("------")
s.postOrder(pNode1)
print("----")
s.postOrder2(pNode1)



