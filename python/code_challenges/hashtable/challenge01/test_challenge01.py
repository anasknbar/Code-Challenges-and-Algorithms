# Write your test here
from challenge01 import TreeNode,findTarget


def test_findTarget_function_case_1():
  root = TreeNode(7)
  root.left = TreeNode(2)
  root.right = TreeNode(9)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(5)
  root.right.right = TreeNode(14)
  
  assert findTarget(root, 3) == True
  

def test_findTarget_function_case_2():
  root = TreeNode(7)
  root.left = TreeNode(2)
  root.right = TreeNode(9)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(5)
  root.right.right = TreeNode(14)
  
  assert findTarget(root, 99) == False


