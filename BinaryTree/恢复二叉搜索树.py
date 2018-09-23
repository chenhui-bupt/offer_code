""""""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        p1, p2 = None, None
        pre = TreeNode(-0xffff)
        if p1 and p2:
            p1.val, p2.val = p2.val, p1.val

    def inOrder(self, root, p1, p2, pre):
        if not root:
            return
        self.inOrder(root.left, p1, p2, pre)
        if not p1 and pre.val >= root.val:
            p1 = pre
            print("hh")
        if p1 and pre.val >= root.val:
            p2 = root
        pre = root
        self.inOrder(root.right, p1, p2, pre)

