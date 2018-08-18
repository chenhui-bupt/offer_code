# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror1(self, root):
        # write code here
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.Mirror(root.right)
        self.Mirror(root.left)
        return root

    def Mirror(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        root.left, root.right = root.right, root.left
        if root.left: # 递归调用的条件，写清楚比较好
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)