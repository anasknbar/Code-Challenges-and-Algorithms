# Write your test here
from challenge03 import sum_of_unique_elements

def test_sum_of_unique_elements_function():
  
  list_1 = [4,56,75,24,4,5,4]
  sum_of_unique_elements_of_list_1 = 160
  assert sum_of_unique_elements(list_1) == sum_of_unique_elements_of_list_1
  
  list_2 = [100,100,100,100]
  sum_of_unique_elements_of_list_2 = 0
  assert sum_of_unique_elements(list_2) == sum_of_unique_elements_of_list_2
  
  list_3 = [100,200,300,400,500]
  sum_of_unique_elements_of_list_3 = 1500
  assert sum_of_unique_elements(list_3) == sum_of_unique_elements_of_list_3
   