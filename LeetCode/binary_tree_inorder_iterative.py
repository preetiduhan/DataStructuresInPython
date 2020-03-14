class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack=[]
        current=root
        while(1):
            while(current):
                stack.append(current)
                current=current.left
            if len(stack)==0:
                break
            if len(stack)>0 and (current is None or current.left is None): 
                item=stack.pop()
                output.append(item.val)
                if item.right is not None:
                    current=item.right
        return output
