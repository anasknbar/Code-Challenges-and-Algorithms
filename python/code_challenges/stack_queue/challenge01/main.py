from challenge01 import Queue

my_queue = Queue()
### adding five elements(A-F) to my_queue
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
my_queue.enqueue('D')
my_queue.enqueue('F')

### Removes and returns the element from the front(the first element) of the queue.
print(my_queue.dequeue()) # >> A

# ### Returns the element at the front of the queue without removing it.
# print(my_queue.peek()) # >> B



print(my_queue)