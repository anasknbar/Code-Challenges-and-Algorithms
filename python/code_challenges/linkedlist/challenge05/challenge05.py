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
        print(self.__str__())
        return 
     
      current_node = current_node.next
  def __getitem__(self,index):
    """ get item from the list using [](indexer) operators method."""
    if self.head is None:
      raise IndexError("empty list")
    elif index >= self.__len__() or index < 0: # index 5, length 5 
      raise IndexError("list index out of range")
    counter = 0
    current_node = self.head
    while current_node:
      if counter == index:
        return current_node.value
      current_node = current_node.next
      counter+=1   
  def __str__(self):
      """ return string representation of the list items"""
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return "["+','.join(elements) + "]"
  
  def insert_after(self,before_node,after_node):
    ''' insert node(after node) after a given node(before node): for example if you have a list > [5,6,7,9,10] using 
    insertafter(7,8) will return [5,6,7,8,9,10]'''
    new_node = Node(after_node)
    if self.head == None:
      raise AttributeError('empty list')
    if self.head.next == None:
      self.head.next = new_node 
      return
    
    curr = self.head
    target_node = before_node
    while curr:
      if curr.value == target_node:
        temp = curr.next
        curr.next = new_node
        curr.next.next=temp
        return
      curr = curr.next
    raise ValueError
      
      
      
      
      
    
  



    