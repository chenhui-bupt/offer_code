class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestConsecutiveSequence(root):
    if not root:
        return 0
    res = [0]
    dfs(root, root.val, res)
    print(res[0])


def dfs(root, parentVal, res):
    if not root:
        return 0, 0
    leftUp, leftDown = dfs(root.left, root.val, res)
    rightUp, rightDown = dfs(root.right, root.val, res)
    res[0] = max(res[0], leftUp + rightDown + 1, leftDown + rightUp + 1)
    up, down = 0, 0
    if root.val == parentVal + 1:
        down = max(leftDown, rightDown) + 1
    elif root.val == parentVal - 1:
        up += max(leftUp, rightUp) + 1
    return up, down


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
longestConsecutiveSequence(node1)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node1
node2.right = node3
longestConsecutiveSequence(node2)


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
longestConsecutiveSequence(node2)
