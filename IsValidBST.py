# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isValidBST(self, root):
        Min, Max = -(1<<31)-1, (1<<31)
        return self.helper(root, Min, Max)
    
    def helper(self, root, Min, Max):
        if not root: # root is None
            return True
        if not root.left and not root.right: # root has no leaf
            if Min < root.val < Max:
                return True
            else:
                return False
        if not root.left and root.right: # root only has right leaf
            return root.val < root.right.val and self.helper(root.right, root.val, Max)
        elif root.left and not root.right: # root only has left leaf
            return root.val > root.left.val and self.helper(root.left, Min, root.val)
        else: # root has both left and right leaves
            return root.left.val < root.val < root.right.val and self.helper(root.left, Min, root.val) and                 self.helper(root.right, root.val, Max)
        
    
