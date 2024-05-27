# Write your test here
from challenge05 import Node,Linkedlist
import pytest

@pytest.fixture
def instance():
  my_list = Linkedlist()
  my_list.append(10)
  my_list.append(20)
  my_list.append(40)
  my_list.append(50)
 
  
  yield my_list
  
def test_insert_after_empty_list():
    my_list = Linkedlist()
    with pytest.raises(AttributeError, match='empty list'):
        my_list.insert_after(20, 10)

def test_insert_to_list(instance):
  
  # index_2_befor_insertion 
  assert instance[2] == 40 # [10,20,40,50]
  
  # index_2_after_insertion 
  instance.insert_after(20,30) # [10,20,30,40,50]
  assert instance[2] == 30
  
def test_to_insert_not_existed_value(instance):
  with pytest.raises(ValueError):
    instance.insert_after(1,100) # no value with 100 to insert 1 afetr.