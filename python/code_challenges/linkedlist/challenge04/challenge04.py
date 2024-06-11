# Write here the code challenge solution
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def append(self,value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      return
    current_node = self.head
    
    while current_node.next:
      current_node = current_node.next
    current_node.next = new_node
    
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
      
  def reverse(self):
    '''return reversed linked list. i.e: [1,2,3] >> [3,2,1]'''
    reversed_linked_list =  LinkedList()
    stack = []
    if self.head is None:
       raise AttributeError('list is empty')
     
    if self.head.next is None: 
       return self.head.value
     
    current_node = self.head
     
    while current_node:
      stack.insert(0,current_node.value)
      current_node = current_node.next
    
   
    for value in stack:
      reversed_linked_list.append(value)
    return str(reversed_linked_list)
  
  

      
    
    
       
     
     
     
  def __str__(self):
      """ return string representation of the list items"""
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return "["+', '.join(elements) + "]"
    





  

    
    
    
      
    
    
    
    
    
  


