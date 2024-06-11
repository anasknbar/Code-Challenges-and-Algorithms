# Write your test here

from challenge04 import LinkedList,Node
import pytest



def test_one_single_node_in_the_list():
  my_list = LinkedList()

  my_list.append(1)
  
  assert my_list.reverse() == 1

def test_linked_list_with_multiple_node():
  my_list = LinkedList()

  my_list.append(1)
  my_list.append(2)
  my_list.append(3)
  my_list.append(4)
  my_list.append(5)
  
  linked_list_before_reversing = "[1, 2, 3, 4, 5]"
  linked_list_after_reversing =  "[5, 4, 3, 2, 1]"
  
  assert (my_list.reverse()) == linked_list_after_reversing
  
  
def test_empty_list():
  my_list = LinkedList()

  
  
  with pytest.raises(AttributeError):
