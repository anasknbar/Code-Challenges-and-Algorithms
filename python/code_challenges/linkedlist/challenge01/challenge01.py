# Write here the code challenge solution

class Node:
  def __init__(self,value):
    self.value = value
    self.next  = None
    
  
class Linkedlist():
  def __init__(self):
    self.head = None
  
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
  def delete(self,value):
    if self.head is None:
      raise ValueError("list is empty") # check if the list is empty
    
    if self.head.value == value:
      self.head = self.head.next # check if the first node is the one to be deleted
      
    current_node = self.head 
    while current_node.next:
      if current_node.next.value == value:
        current_node.next = current_node.next.next
        return 'deleted succefully'
     
      current_node = current_node.next
      
  def __str__(self):
      """ return string representation of the list items"""
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return ' -> '.join(elements) + " -> None"
    
my_list = Linkedlist()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


print(my_list)

    