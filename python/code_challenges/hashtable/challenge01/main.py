from challenge01 import TreeNode,findTarget

# construct a tree example
root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right.right = TreeNode(14)

# try this 
print(findTarget(root, 3))  
print(findTarget(root, 56))  
print(findTarget(root, 19))  
print(findTarget(root, 4))  