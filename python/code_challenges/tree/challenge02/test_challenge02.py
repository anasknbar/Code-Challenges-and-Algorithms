# Write your test here
from challenge02 import Node,breadth_first_values_iterative,compare

def test_compare_case_1():
  # first_tree represented by (f)
  f_one = Node(1)
  f_two = Node(2)
  f_three = Node(3)

  f_one.left = f_two
  f_one.right = f_three

  #    1
  #   / \
  #  2   3

   
  # second_tree represented by (s)
  s_one = Node(1)
  s_two = Node(2)
  s_three = Node(3)

  s_one.left = s_two
  s_one.right = s_three
  
  #    1
  #   / \
  #  2   3
  assert (compare(f_one,s_one))  == True

def test_compare_case_2():
  # first_tree represented by (f)
  f_one = Node(1)
  f_two = Node(2)
  

  f_one.left = f_two
  

  #    1
  #   / \
  #  2   None

   
  # second_tree represented by (s)
  s_one = Node(1)
  s_two = Node(2)
  

  s_one.right = s_two
  
  
  #     1
  #    / \
  # None  2
  
  assert (compare(f_one,s_one))  == False
  
def test_compare_case_3():
  # first_tree represented by (f)
  f_parent_one = Node(1)
  f_child_one = Node(1)
  f_two = Node(2)
  

  f_parent_one.left = f_two
  f_parent_one.right = f_child_one 

  #    1
  #   / \
  #  2   1

   
  # second_tree represented by (s)
  s_parent_one = Node(1)
  s_child_one = Node(1)
  s_two = Node(2)


  s_parent_one.left = s_child_one
  s_parent_one.right = s_two
  
  #    1
  #   / \
  #  1   2
  assert (compare(f_parent_one,s_parent_one))  == False