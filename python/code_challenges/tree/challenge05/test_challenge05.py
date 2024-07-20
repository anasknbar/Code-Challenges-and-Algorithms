# Write your test here
from challenge05 import TreeNode,max_height

def test_max_height_function_1():
  root_1 = TreeNode(10)
  root_1.left = TreeNode(20)
  root_1.right = TreeNode(30)

  root_1.left.left = TreeNode(40)
  root_1.left.right = TreeNode(28)
  
  root_1.right.left = TreeNode(27)
  root_1.right.right = TreeNode(50)
  
  root_1.right.left.right = TreeNode(29)
  
 
  
  assert (max_height(root_1)-1) == 3
  
def test_max_height_function_2():
  root_2 = TreeNode(10)
  root_2.left = TreeNode(20)
  root_2.right = TreeNode(30)

  root_2.left.left = TreeNode(40)
  root_2.left.right = TreeNode(28)
  
  root_2.right.left = TreeNode(27)
  root_2.right.right = TreeNode(50)
  
  root_2.right.left.right = TreeNode(29)
  root_2.right.left.right.left = TreeNode(60)
  
  assert (max_height(root_2)-1) == 4
  
