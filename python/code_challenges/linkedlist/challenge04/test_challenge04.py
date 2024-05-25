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
  
  # before reversing the list  >  head = 1
  # after  reversing the list  >  head = 5
  
  assert my_list.reverse() == 5
  
  
def test_empty_list():
  my_list = LinkedList()

  
  
  with pytest.raises(AttributeError):
    my_list.reverse()