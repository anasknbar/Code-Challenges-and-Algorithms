from challenge04 import TreeNode,find_max_value

root = TreeNode(1000)
root.left = TreeNode(500)
root.right = TreeNode(2000)
root.left.left = TreeNode(250)
root.left.right = TreeNode(600)
root.right.left = TreeNode(12000)


print(find_max_value(root))