# challenge test cases 
from challenge01 import Node, Tree, printTree

preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]

root1 = Tree(preorder1, inorder1)
print(printTree(root1))  

preorder2 = [-1]
inorder2 = [-1]
root2 = Tree(preorder2, inorder2)
print(printTree(root2))  