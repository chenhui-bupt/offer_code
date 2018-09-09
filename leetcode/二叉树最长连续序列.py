"""二叉树最长连续递增路径序列
Given a binary tree, find the length of the longest consecutive sequence path.



The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestConsecutiveSequence(root):
    if not root:
        return
    res = [0]
    tLen = 0
    dfs(root, root.val, tLen, res)
    print(res)

def dfs(root, parentVal, tLen, res):
    if not root:
        return
    elif root.val == parentVal + 1:
        tLen += 1
    else:
        tLen = 1
    res[0] = max(res[0], tLen)
    dfs(root.left, root.val, tLen, res)
    dfs(root.right, root.val, tLen, res)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.right = node3
node3.left = node2
node3.right = node4
node4.right = node5
longestConsecutiveSequence(node1)

node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(1)
node1.right = node2
node2.left = node3
node3.left = node4
longestConsecutiveSequence(node1)

