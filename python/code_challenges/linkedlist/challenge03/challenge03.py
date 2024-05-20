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
  
  def remove(self, position):
        """ Remove an item from the linked list at the given position. """
        if self.head is None:
            raise IndexError("list is empty")
        
        if position < 1:
            raise IndexError("position must be 1 or greater")

        current = self.head
        if position == 1:
            self.head = current.next
            return

        counter = 1
        previous_node = None
        while current is not None and counter < position:
            previous_node = current
            current = current.next
            counter += 1

        if current is None:
            raise IndexError("position out of range")

        previous_node.next = current.next
     
    
      
  def __str__(self):
      """ return string representation of the list items """
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return "["+','.join(elements) + "]"
    









