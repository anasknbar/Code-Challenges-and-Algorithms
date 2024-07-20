# Write here the code challenge solution

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_height(root):
    if not root:
        return 0
    
    return 1 + max(max_height(root.left), max_height(root.right))







