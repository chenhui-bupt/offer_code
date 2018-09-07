# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):  # bfs
        # write code here
        if not pRoot:
            return 0
        queue = []
        queue.append(pRoot)
        cnt = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            cnt += 1
        return cnt

    def dfs(self, root):  # dfs
        # write code here
        if not root:
            return 0
        return max(self.dfs(root.left), self.dfs(root.right)) + 1
