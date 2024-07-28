# Write your test here
from challenge04 import helper_function

def test_helper_function_multiply_items():
  
  expected_order = ['Bob', 'Alice', 'Bob']
  actual_order = helper_function(["Alice","Bob","Bob"],[155,185,150])
  assert expected_order == actual_order
  

def test_helper_function_signle_item():
  
  expected_order = ['Alice']
  actual_order = helper_function(["Alice"],[155])
  assert expected_order == actual_order 
  
  
def test_helper_function_no_items():
  
  expected_order = []
  actual_order = helper_function([],[])
  assert expected_order == actual_order 
  