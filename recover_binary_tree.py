# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.inorder(res, root)
        first = None
        second = None
        for i in range(1, len(res)):
            if res[i].val < res[i - 1].val:
                if first == None:
                    first = res[i - 1]
                    second = res[i]
                else:
                    second = res[i]
                    break
        first.val, second.val = second.val, first.val
    def inorder(self, res, root):
        if root == None:
            return
        self.inorder(res, root.left)
        res.append(root)
        self.inorder(res, root.right)
            
