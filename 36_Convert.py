# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert1(self, pRoot):
        # write code here
        if not pRoot:
            return
        pTreeList = []
        self.convertHelper(pRoot, pTreeList)
        for i in range(len(pTreeList) - 1):
            pTreeList[i].right = pTreeList[i + 1]
            pTreeList[i + 1].left = pTreeList[i]
        return pTreeList[0]

    def convertHelper(self, pRoot, pTreeList):
        if pRoot:
            self.convertHelper(pRoot.left, pTreeList)
            pTreeList.append(pRoot)
            self.convertHelper(pRoot.right, pTreeList)

    def Convert(self, pRoot):
        if not pRoot:
            return
        stack = []
        pNode = pRoot
        pTreeList = []
        while pNode or stack:
            if pNode:
                while pNode:
                    stack.append(pNode)
                    pNode = pNode.left
            else:
                pNode = stack.pop()
                pTreeList.append(pNode)
                pNode = pNode.right
        for i in range(len(pTreeList) - 1):
            pTreeList[i].right = pTreeList[i + 1]
            pTreeList[i + 1].left = pTreeList[i]
        return pTreeList[0]


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, root):
        # write code here
        if not root:
            return
        stack = []
        pNode = root
        pre = None
        while pNode or stack:
            if pNode:
                stack.append(pNode)
                pNode = pNode.left
            else:
                pNode = stack.pop()
                pNode.left = pre
                if pre:
                    pre.right = pNode
                pre = pNode
                pNode = pNode.right
        pNode = root
        while pNode.left:
            pNode = pNode.left
        return pNode


class Solution:
    def Convert(self, root):
        # write code here
        if not root:
            return
        pre = None
        self.helper(root, pre)
        pNode = root
        while pNode.left:
            pNode = pNode.left
        return pNode

    def helper(self, root, pre):
        if not root:
            return
        self.helper(root.left, pre)
        root.left = pre
        if pre:
            pre.right = root
        pre = root
        self.helper(root.right, pre)