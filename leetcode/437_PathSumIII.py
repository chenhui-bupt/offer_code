"""
https://leetcode.com/problems/path-sum-iii/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        else:
            return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def helper(self, root, tsum):
        if not root:
            return 0
        else:
            return (root.val == tsum) + self.helper(root.left, tsum - root.val) + self.helper(root.right,
                                                                                              tsum - root.val)
