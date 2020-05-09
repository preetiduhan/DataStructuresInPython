'''
invert binary tree
'''
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
  
# Helper function that allocates  
# a new node with the given data  
# and None left and right pointers 
def createNode(val): 
    newNode = Node(val) 
    newNode.left = None
    newNode.right = None
    return newNode 

def invert_binary_tree(root):
    if root is None:
        return
    q=[]
    q.append(root)
    print(q)
    while (len(q)):
        item=q.pop(0)
        if item is not None:
            item.left,item.right=item.right,item.left
            q.append(item.left)
            q.append(item.right)
        else:
            continue
    print_tree(root)
    
def print_tree(root):
    if root is None:
        return
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)

if __name__=='__main__':  
  
    tree = createNode(5) 
    tree.left = createNode(3) 
    tree.right = createNode(6) 
    tree.left.left = createNode(2) 
    tree.left.right = createNode(4) 
    invert_binary_tree(tree)  
