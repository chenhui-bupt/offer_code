# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here 
        if not sequence:
            return False
        root = sequence.pop()
        i = 0
        for node in sequence: # 找到大于根节点的第一个节点，划分左右子树
            i += 1
            if node > root:
                break
        leftTree = sequence[:i] # 左子树
        rightTree = sequence[i:] # 右子树
        for node in rightTree: # 右子树不能出现节点小于根节点
            if node < root:
                return False
        # 判断左子树是不是BST
        left = True
        if leftTree:
            left = self.VerifySquenceOfBST(leftTree)
        right = True
        if rightTree:
            right = self.VerifySquenceOfBST(rightTree)
        return left and right
    