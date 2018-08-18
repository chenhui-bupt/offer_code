# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def FindTheLayerWithMostNodesNearstToBottom(self, root): # 类似于宽度优先，按行打印
        if not root:
            return
        queue = []  # 宽度优先，用队列维持（最重要）
        queue.append(root)
        printTree = []
        maxOfNodes = 0
        maxOfLayer = 0
        layer = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                printTree.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(printTree)
            layer += 1
            if maxOfNodes <= len(printTree):
                maxOfNodes = len(printTree)
                maxOfLayer = layer
            printTree = []
        print("第%s层有最多的节点数%s个" % (maxOfLayer, maxOfNodes))


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
s.FindTheLayerWithMostNodesNearstToBottom(pNode1)
