class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestConsecutiveSequence(root):
    if not root:
        return
    res = [0]
    dfs(root, root.val, 0, res)
    print(res[0])

    res = [0]
    dfs2(root, root.val, res)
    print(res[0])

def dfs(root, parentVal, tLen, res):  # 从根节点到叶子节点计数
    if not root:
        return   # 结束递归
    elif root.val == parentVal + 1:
        tLen += 1
    else:
        tLen = 1  # 重新计数
    res[0] = max(res[0], tLen)
    dfs(root.left, root.val, tLen, res)  # 递归，
    dfs(root.right, root.val, tLen, res)  # 递归，左右节点传入的tLen一样，连续路径不能包含左右节点

def dfs2(root, parentVal, res):  # 从叶子节点到根节点计数
    if not root:
        return 0  # 计数从叶子节点开始
    # 前序遍历，左右子节点先递归
    left = dfs2(root.left, root.val, res)
    right = dfs2(root.right, root.val, res)
    res[0] = max(res[0], left + 1, right + 1)
    down = 0
    if root.val == parentVal + 1:
        down = max(left, right) + 1
    return down

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
