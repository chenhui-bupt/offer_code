"""二叉树最长连续序列II
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].


Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].


Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestConsecutiveSequenceII(root):
    res = [0]
    dfs(root, root.val, res)
    print(res[0])

def dfs(root, parentVal, res):
    if not root:
        return 0, 0
    leftUp, leftDown = dfs(root.left, root.val, res)
    rightUp, rightDown = dfs(root.right, root.val, res)
    res[0] = max(res[0], leftUp + rightDown + 1, leftDown + rightUp + 1)
    upLen = downLen = 0
    if root.val == parentVal + 1:
        upLen = max(leftUp, rightUp) + 1
    elif root.val == parentVal - 1:
        downLen = max(leftDown, rightDown) + 1
    return upLen, downLen


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
longestConsecutiveSequenceII(node1)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node1
node2.right = node3
longestConsecutiveSequenceII(node2)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)


node2.left = node1
node2.right = node3
node1.left = node6
node3.right = node4
node4.left = node5
longestConsecutiveSequenceII(node2)
