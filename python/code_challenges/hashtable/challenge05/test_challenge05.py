# Write your test here
from challenge05 import helper_function

def test_helper_function_1():
  
  list_1 = [300,456,783,563]
  list_2 = [300,456,783,563]
  
  expected_intersection_list = sorted([300,456,783,563])
  actual_intersection_list = helper_function(list_1,list_2)
  
  assert expected_intersection_list == actual_intersection_list



def test_helper_function_2():
  list_1 = [15,30,45,60]
  list_2 = [10,20,30,40,50,60,70,80,90,100]
  
  expected_intersection_list = sorted([60,30])
  actual_intersection_list = helper_function(list_1,list_2)
  
  assert expected_intersection_list == actual_intersection_list