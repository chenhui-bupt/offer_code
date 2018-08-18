# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root or not expectNumber:
            return []
        path = []
        paths = []
        def helper(root, expectNumber):
            path.append(root.val)
            if root.left is None and root.right is None and expectNumber == root.val:
                paths.append(path[::])
            if root.left:
                helper(root.left, expectNumber - root.val)
            if root.right:
                helper(root.right, expectNumber - root.val)
            path.pop()
        helper(root, expectNumber)
        return paths
        

    


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))
