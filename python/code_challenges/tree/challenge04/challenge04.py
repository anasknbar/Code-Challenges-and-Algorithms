# Write here the code challenge solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_max_value(root):
    '''  Finds the maximum value in a binary tree using iterative inorder traversal. '''
    if not root:
        return float('-inf')
    
    stack = []
    current = root
    max_value = float('-inf')
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        max_value = max(max_value, current.val)
        current = current.right
    
    return max_value


if __name__ == "__main__":
  main()


