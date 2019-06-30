class Solution(object):
    def generateTrees(self, n):
        if n==0:
            return []
        nums = [i for i in range(1,n+1)]
        
		#given a list of nodes, gives UBST list for it
        def treeList(L):
            res = []
            if L==[]:
                return [None]
            if len(L)==1:
                l = [TreeNode(L[0])]
                return l
				
			#for each i, taking L[i] as root
            for i in range(len(L)):

                lessThanRoot = L[:i]
                greaterThanRoot = L[i+1:]
                leftNodesList = treeList(lessThanRoot)
                rightNodesList = treeList(greaterThanRoot)

                
                for t1 in leftNodesList:
                    for t2 in rightNodesList:
                        root = TreeNode( L[i] )
                        root.left = t1
                        root.right = t2
                        res.append(root)
            return res
        
        R = treeList(nums)
        return R
