# Write your test here
import pytest
from challenge03 import Node,Linkedlist



def test_remove():
  my_list = Linkedlist()
  my_list.append(10)
  my_list.append(20)
  my_list.append(30)
  my_list.append(40)
  my_list.append(50)
  
  list_befor_deleting = len(my_list) 
  my_list.remove(5)
  list_after_deleting = len(my_list)
  
  
  assert list_befor_deleting == 5
  assert list_after_deleting == 4
  
