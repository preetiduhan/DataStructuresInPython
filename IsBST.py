# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isValidBST(self, root):
        min=float('-inf')
        max=float('inf')
        def helper(root,min,max):
            if root is None:
                return True
            if root.val<=min or root.val>=max:
                return False
            return helper(root.left,min,root.val) and helper(root.right,root.val,max)
        return helper(root,min,max)
       
    
        
    
