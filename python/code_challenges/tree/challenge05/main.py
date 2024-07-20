from challenge05 import TreeNode,max_height


# we construct a tree same as the assignment example: 
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(28)

root.right.left = TreeNode(27)
root.right.right = TreeNode(50)

root.right.left.right = TreeNode(29)


print(max_height(root)-1)