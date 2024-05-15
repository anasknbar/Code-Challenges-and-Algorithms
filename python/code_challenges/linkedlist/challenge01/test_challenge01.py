# Write your test here
import pytest
from challenge01 import Node,Linkedlist

def test_delete_method():
  my_list = Linkedlist()
  my_list.append(10)
  my_list.append(20)
  my_list.append(30)
  my_list.append(40)
  befor_deleting = len(my_list)
  
  my_list.delete(40)
  after_deleting = len(my_list)
  
  assert after_deleting == befor_deleting - 1
