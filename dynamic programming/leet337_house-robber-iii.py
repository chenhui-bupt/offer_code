# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.robSub(root))
        return self.robHelper(root, {})

    def robHelper(self, root, map_dict):
        """
        最优子问题 + 自顶向下备忘录法（hash map）
        """
        if not root:
            return 0
        if root in map_dict:
            return map_dict[root]
        tsum = 0
        if root.left:
            tsum += self.robHelper(root.left.left, map_dict) + self.robHelper(root.left.right, map_dict)
        if root.right:
            tsum += self.robHelper(root.right.left, map_dict) + self.robHelper(root.right.right, map_dict)
        tsum = max(root.val + tsum, self.robHelper(root.left, map_dict) + self.robHelper(root.right, map_dict))
        map_dict[root] = tsum
        return tsum

    def robSub(self, root):
        if not root:
            return [0, 0]
        left = self.robSub(root.left)
        right = self.robSub(root.right)
        robbed = root.val + left[0] + right[0]
        notrobbed = max(left) + max(right)
        return [notrobbed, robbed]


node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(9)
node6 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

s = Solution()
res = s.rob(node1)
print(res)
