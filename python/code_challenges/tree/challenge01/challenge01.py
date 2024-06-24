# Write here the code challenge solution



class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    
    root_val = preorder.pop(0)
    root = Node(root_val)
    
    
    inorder_index = inorder.index(root_val)
    
    
    root.left = Tree(preorder, inorder[:inorder_index])
    root.right = Tree(preorder, inorder[inorder_index + 1:])
    
    return root


def printTree(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    return result




 























