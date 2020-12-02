给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

        3
       / \
      9  20
        /  \
       15   7                    

返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4


返回 false 。



解题思路：

 自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回 -1−1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。

```python
# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
         
class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        def treeDepth(root: TreeNode) -> int:
            if root == None:
                return 0
            
            leftDepth = treeDepth(root.left)
            rightDepth = treeDepth(root.right)

            if leftDepth == -1 or rightDepth == -1 or abs(leftDepth-rightDepth) > 1:
                return -1
            else:
                return max(leftDepth,rightDepth) + 1
        return treeDepth(root) >= 0
```

