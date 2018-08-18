# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return 
        buf = []
        self.serializeHelper(root, buf)
        return ','.join(buf)

    def serializeHelper(self, root, buf):
        if not root:
            buf.append('$')
        else:
            buf.append(str(root.val))
            self.serializeHelper(root.left, buf)
            self.serializeHelper(root.right, buf)
    
    def Serialize2(self, root):
        # write code here
        if not root:
            return 
        buf = []
        buf = self.serializeHelper2(root, buf)
        return ','.join(buf)

    def serializeHelper2(self, root, buf):
        if not root:
            buf.append('$')
        else:
            buf.append(str(root.val))
            self.serializeHelper2(root.left, buf)
            self.serializeHelper2(root.right, buf)
        return buf

        
    def Deserialize(self, s):
        # write code here
        if not s:
            return 
        pRoot = self.deserializeHelper(s.split(','))
        return pRoot

    def deserializeHelper(self, buf):
        number = buf.pop(0)
        if number == '$':
            return None
        pRoot = TreeNode(int(number))
        pRoot.left = self.deserializeHelper(buf)
        pRoot.right = self.deserializeHelper(buf)
        return pRoot # 只有栈底的函数才有return，之前的return都被覆盖，即返回的是根节点


# pNode1 = TreeNode(8)
# pNode2 = TreeNode(6)
# pNode3 = TreeNode(10)
# pNode4 = TreeNode(5)
# pNode5 = TreeNode(7)
# pNode6 = TreeNode(9)
# pNode7 = TreeNode(11)

# pNode1.left = pNode2
# pNode1.right = pNode3
# pNode2.left = pNode4
# pNode2.right = pNode5
# pNode3.left = pNode6
# pNode3.right = pNode7
pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode3.left = pNode5
pNode3.right = pNode6

s = Solution()
string = s.Serialize(pNode1)
string = s.Serialize2(pNode1)
print(string)
pRoot = s.Deserialize(string)
print(pRoot.val, pRoot.left.val, pRoot.right.val, pRoot.left.left.val, pRoot.right.left.val, pRoot.right.right.val)

