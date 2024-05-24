# Write your test here
from challenge02 import Node,Linkedlist


def test_odd_list():
  my_list = Linkedlist()
  my_list.append(1)
  my_list.append(2)
  my_list.append(3)
  my_list.append(4)
  my_list.append(5)
  
  actual_middle_node = 3
  expected_middle_node = my_list.middle()
  
  assert actual_middle_node == expected_middle_node

def test_even_list():
  my_list = Linkedlist()
  my_list.append(1)
  my_list.append(2)
  my_list.append(3)
  my_list.append(4)
  my_list.append(5)
  my_list.append(6)
  
  actual_middle_node = 4 # the second node of the two middle node(3,4) is 4 
  expected_middle_node = my_list.middle()
  
  assert actual_middle_node == expected_middle_node