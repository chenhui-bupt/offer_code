"""
1. BST

只保存preorder或者postorder就够了，递归有O(n^2)和O(n)算法。非递归有利用栈的O(n)算法。（前序或后序即可）

2. Complete binary tree

level traversal就行了。 层次遍历存储

3. Full binary tree

用一个bit来保存该结点是internal node还是leaf node. 位标志是否是叶子节点

4. General Binary Tree

用NULL来占位。（这个可以是很小位），如果每个结点很大的话，这种方法相比起直接同时存preorder和inorder好。

见：http://www.geeksforgeeks.org/serialize-deserialize-binary-tree/

个人觉得对叶子结点，直接用另一个占位符更好。然后层次遍历保存起来。比如连续两个NULL用/表示，单个NULL用\表示。

5. k叉树

见：http://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/

就是用多一些标记。

"""