class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.helper(root,output)
        return output
        
    def helper(self,root, output):
        if not root:
            return []
        else:
            if root.left:
                self.helper(root.left,output)
            output.append(root.val)
            if root.right:
                self.helper(root.right,output)
