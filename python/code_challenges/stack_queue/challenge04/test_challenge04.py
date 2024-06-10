# Write your test here
from challenge04 import Queue

def test_reverse_function():
  my_queue = Queue()
  my_queue.enqueue(5)
  my_queue.enqueue(4)
  my_queue.enqueue(3)
  my_queue.enqueue(2)
  my_queue.enqueue(1)
  
  queue_before_reversing = "front==|[  5 -> 4 -> 3 -> 2 -> 1  ]|==rear"
  queue_after_reversing =  "front==|[  1 -> 2 -> 3 -> 4 -> 5  ]|==rear"
  
  
  assert my_queue.reverse() == queue_after_reversing
 