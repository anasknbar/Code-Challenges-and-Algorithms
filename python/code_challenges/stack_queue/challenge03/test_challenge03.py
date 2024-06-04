# Write your test here
from challenge03 import Stack
import pytest

def test_DeleteMiddleNode_with_odd_stack():
  my_stack = Stack()
  my_stack.push(1)
  my_stack.push(2)
  my_stack.push(3)
  my_stack.push(4)
  my_stack.push(5)
  
  expected_deleted_node = 3
  stack_size_before_deletion = 5
  assert my_stack.DeleteMiddleNode() == expected_deleted_node
  assert my_stack.size() == stack_size_before_deletion - 1 
  
def test_DeleteMiddleNode_with_even_stack():
  my_stack = Stack()
  my_stack.push(1)
  my_stack.push(2)
  my_stack.push(3)
  my_stack.push(4)

  
  expected_deleted_node = 2
  stack_size_before_deletion = 4
  assert my_stack.DeleteMiddleNode() == expected_deleted_node
  assert my_stack.size() == stack_size_before_deletion - 1 
  
  
def test_raising_error_when_deleting_from_empty_stack():
  my_stack = Stack()
  with pytest.raises(IndexError):
    my_stack.DeleteMiddleNode()