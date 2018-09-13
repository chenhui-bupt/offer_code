"""
实现二叉搜索树的搜索，插入，删除
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def search(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    elif value < root.val:
        return search(root.left, value)
    else:
        return search(root.right, value)


def searchNotRecursive(root, value):
    """非递归方式查找"""
    while root:
        if root.val == value:
            return True
        elif value < root.val:
            root = root.left
        else:
            root = root.right
    return False


def insert(root, value):
    if not root:
        return TreeNode(value)
    elif value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def insertNotRecursive(root, value):
    """非递归方式插入"""
    pNode = root
    while pNode:
        if value < pNode.val:
            if not pNode.left:
                pNode.left = TreeNode(value)
            pNode = pNode.left
        else:
            if not pNode.right:
                pNode.right = TreeNode(value)
            pNode = pNode.right


def delete(root, value):  # 先找待删除的节点
    if not root:
        return
    if root.val == value:
        deleteNode(root)
    elif value < root.val:
        delete(root.left, value)
    else:
        delete(root.right, value)


def deleteNode(p):
    """
    1. 待删除的节点是叶子节点
    2. 待删除的节点只有左子节点
    3. 待删除的节点只有右子节点
    4. 待删除的节点有左右子节点
    :param p:
    :return:
    """
    if not p.left and not p.right:
        del p
        p = None
    elif not p.right:
        p = p.left
    elif not p.left:
        p = p.right
    else:
        q, s = p, p.left
        while s.right:
            q = s
            s = s.right
        p.val = s.val
        if q != p:  # 左子节点有右子树，所以s的父亲节点就不会是最初的p节点
            q.right = s.left
        else:
            q.left = s.left
        del s
    return p


node8 = TreeNode(8)
node3 = TreeNode(3)
node10 = TreeNode(10)
node1 = TreeNode(1)
node6 = TreeNode(6)
node14 = TreeNode(14)
node4 = TreeNode(4)
node7 = TreeNode(7)
node13 = TreeNode(13)
node8.left = node3
node8.right = node10
node3.left = node1
node3.right = node6
node10.right = node14
node6.left = node4
node6.right = node7
node14.left = node13


def inOrder(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


print("search...")
print(search(node8, 14))
print(searchNotRecursive(node8, 14))

print("insert...")
insert(node8, 9)
res = inOrder(node8)
print(res)

print("delete...")
delete(node8, 3)
res = inOrder(node8)
print(res)
