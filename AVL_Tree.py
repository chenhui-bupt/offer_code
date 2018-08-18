# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        isBalanced = [True]
        self.getDepth(pRoot, isBalanced)
        return isBalanced[0]

    def getDepth(self, pRoot, isBalanced):
        if not pRoot:
            return 0
        left = self.getDepth(pRoot.left, isBalanced)
        right = self.getDepth(pRoot.right, isBalanced)
        if abs(left - right) > 1:
            isBalanced[0] = False
        if left > right:
            return left + 1
        else:
            return right + 1