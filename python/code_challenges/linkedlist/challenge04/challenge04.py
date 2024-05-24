# Write here the code challenge solution
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    

class LinkedList:
  def __init__(self):
    self.head = None
    
  def __len__(self):
    """return the length of the list"""
    if self.head is None:
      return 0
    
    counter = 1
    current_node = self.head
    while current_node.next:
      counter += 1
      current_node = current_node.next
    return counter
  
  def __str__(self):
      """ return string representation of the list items"""
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return ' -> '.join(elements) + " -> None"
  
  def append(self,value): 
    """Append a new node with the given data to the end of the linked list."""
    
    new_node = Node(value) 
 
    if self.head is None:
      self.head = new_node
      return 
    
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node 
  
  def reverse(self):
    
    if self.head is None:
      raise AttributeError('list is empty!') 
    if self.head.next is None:
      return self.head.value
    
    r_list = []
    while last_node:
      r_list.append(last_node)
      last_node = last_node.next
    
    
    
      
    
    
    
    
    
  

my_list = LinkedList()

my_list.append(1)
my_list.append(2)
# my_list.append(3)

print(my_list)