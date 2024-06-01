# Write your test here
from challenge01 import Queue
import pytest

@pytest.fixture
def instance():
  my_queue = Queue()
  return my_queue

def test_enqueue_method(instance):
  assert instance.IsEmpty() == True
  instance.enqueue(1) # after addition isEmpty() should become False
  assert instance.IsEmpty() == False
  
def test_dequeue_method(instance):
  instance.enqueue(1) # adding an elemnt to the queue, now isEmpty should become False
  assert instance.IsEmpty() == False
  instance.dequeue() # removing the single element in the queue, now isEmpty should become True
  assert instance.IsEmpty() == True
  
def test_peek_method(instance):
  instance.enqueue(1)
  instance.enqueue(2)
  instance.enqueue(3)
  # queue : (front) 1 >> 2 >> 3 (rear)
  assert instance.peek() == 1
  

  
