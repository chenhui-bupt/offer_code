# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2: # 要考虑树比到最后，递归时树pRoot2为空，此时应该返回True
            return False
        result = False
        if abs(pRoot1.val - pRoot2.val) < 0.0000001:
            result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
        if not result: # 如果根节点比不通， 再用树1的左子树
            result = self.HasSubtree(pRoot1.left, pRoot2) 
        if not result: # 如果根节点比不通， 再用树1的右子树
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    
    # 要考虑树比到最后，递归时树pRoot2为空，此时应该返回True, 所以我们新建了一个函数用于内层递归
    def DoesTree1HaveTree2(self, pRoot1, pRoot2): 
        if not pRoot2: # 树比完了，返回True
            return True
        if not pRoot1: # 树没比完，树1就结束了,返回False
            return False
        result = None
        if abs(pRoot1.val - pRoot2.val) < 0.0000001: # 递归
            return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)
        else:
            return False
    