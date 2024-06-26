# Write here the code challenge solution

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    
class Linkedlist:
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
     
  def middle(self):
    ''' return the middel node in agive list, if the list is even , it will return me the second of the two middle node'''
    if self.head == None:
      raise AttributeError('empty list')
    def len():
      counter = 1
      current_node = self.head
      while current_node.next:
        counter += 1
        current_node = current_node.next
      return counter 
    def get_item(index):
      target_index = index
      counter = 0
      target_node = self.head
      previous_node = None
      while counter != target_index:
        previous_node = target_node
        target_node = target_node.next
        
        counter+=1
      return(previous_node.value)
    
    
    def find_middle_index():
      mid_index = len() // 2
      return mid_index+1
    
  
    
    return(get_item(find_middle_index()))
    
    
    
   
   
  
    
    
  
      
    
   
    
    
    
    
    
    
    
    
    
    
  def __str__(self):
      """ return string representation of the list items"""
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return "["+','.join(elements) + "]"
  


# try the following code :
# my_list = Linkedlist()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)

# print(my_list.middle())
  