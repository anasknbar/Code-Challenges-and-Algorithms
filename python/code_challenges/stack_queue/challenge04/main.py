from challenge04 import Queue

my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(4)
my_queue.enqueue(3)
my_queue.enqueue(2)
my_queue.enqueue(1)
print(f"before reversig >> {my_queue}")

print(f"After reversig  >> {my_queue.reverse()}")

