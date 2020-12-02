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
        


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None