# Write here the code challenge solution

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    
    
  def enqueue(self,value):
    ''' Adds an element to the end of the queue'''
    new_node = Node(value)
    if self.front is None: # empty list edge case
      self.front = new_node
      self.rear = new_node 
    else:
      self.rear.next = new_node
      self.rear = new_node
         
  def dequeue(self):
    '''Removes and returns the element from the front(the first elment) of the queue.'''
    if self.front is None: 
      raise AttributeError('empty queue')
    
    if self.front == self.rear:
      temp = self.front 
      self.front = None 
      return temp.value
    else:
      temp = self.front
      self.front = self.front.next
      temp.next = None
      return temp.value

    
  def peek(self):
    ''' peek/front > Returns the element at the front of the queue without removing it.'''
    return self.front.value 
  
  def IsEmpty(self):
    ''' Checks if the queue is empty'''
    if self.front is None:
      return True
    else:
      return False
    
  def __str__(self):
    '''return a string represention of the queue '''
    values = []
    current = self.front
    while current:
      values.append(str(current.value))
      current = current.next
    return 'front--->  '+' -> '.join(values)+'  <---rear'
  

