# Write here the code challenge solution
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    
  
class Queue:
  def __init__(self):
    self.front = None 
    self.rear = None
    self.length = 0
    
    
  def enqueue(self,value):
    '''Adds an element to the end of the queue.'''
    new_node = Node(value)
    
    if self.front is None: # check for empty Queue
      self.front = new_node
      self.rear = new_node
      
    
    elif self.front == self.rear:
      self.front.next = new_node
      self.rear = new_node
    
    else:
      current_node = self.front
      while current_node != self.rear:
        current_node = current_node.next
      current_node.next = new_node
      self.rear = new_node
    self.length += 1
  
  def dequeue(self):
    '''Remove and Return the element from the front of the queue.'''   
    if self.front is None:
      raise IndexError('dequeue from empty queue')
    
    
    elif self.front == self.rear:
      
      temp = self.front #
      self.front = None
      self.rear = None
      return temp.value #
    else:
      temp =self.front # 
      self.front = self.front.next
      return temp.value #
    self.length -= 1
  def peek(self):
    '''Returns the element at the front of the queue without removing it.'''
    if self.front is None:
      raise IndexError('peek from empty queue')
    return self.front.value
  def IsEmpty(self):
    '''Checks if the queue is empty.'''
    if self.front is None:
      return True
    else:
      return False 
  
  def size(self):
    '''Returns the number of elements in the queue.'''
    return self.length
  
  def clear(self):
    '''Removes all elements from the queue.'''
    
    self.front = None
    self.rear = None
    self.length = 0
    
  def contains(self,value):
    ''''Checks if a certain element is in the queue.'''
    if self.front is None:
      return False
    current_node = self.front
    is_contain = False
    while current_node:
      if current_node.value != value:
        current_node = current_node.next
      else:
        is_contain = True
        break
    return is_contain
      
  # Challenge04 code     
  def reverse(self):
    '''Reverse the queue and return the new queue.''' 
    reversed_queue = []
    
    if self.front is None:
      raise IndexError("reverse of empty queue")
    elif self.front == self.rear:
      return self.front.value
    current_node = self.front
    
    while current_node:
      reversed_queue.insert(0,str(current_node.value))
      current_node = current_node.next
    return 'front==|[  '+' -> '.join(reversed_queue)+'  ]|==rear'
    
  def __str__(self):
    values = []
    current_node = self.front
    while current_node:
      values.append(str(current_node.value))
      current_node = current_node.next
    
    return 'front==|[  '+' -> '.join(values)+'  ]|==rear'
      
      
