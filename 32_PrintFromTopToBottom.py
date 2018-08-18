# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [] # 用一个队列保存树的遍历关系
        queue.append(root)
        printTree = []
        while(queue): # 每弹出一个节点，就把该节点的左右子树追加的队列末尾，就能保证按层遍历
        # 因为节点1在节点2的前面，那么节点1的左右子树节点也在节点2的左右子树前面，因此用队列维持树的队列关系
            pNode = queue.pop(0) # 弹出队列头节点
            printTree.append(pNode.val)
            # print(pNode.val)
            if pNode.left: # 追加左子树
                queue.append(pNode.left)
            if pNode.right: # 追加右子树
                queue.append(pNode.right)
        return printTree
    