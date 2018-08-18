# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        node = pre[0]
        root = TreeNode(node)
        index = tin.index(node)
        root.left = self.reConstructBinaryTree(pre[1: index + 1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index + 1:], tin[index + 1:])
        return root


s = Solution()
pre = [1, 2, 3, 4, 5, 6, 7]
tin = [3,2,4,1,6,5,7]
root = s.reConstructBinaryTree(pre, tin)
print(root.val)

