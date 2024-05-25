# Write here the code challenge solution
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    
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
    if self.head is None:
       raise AttributeError('list is empty')
     
    if self.head.next is None: 
       return self.head.value
     
    curr = self.head
    prev = None
     
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
      
    return prev.value # return the new head of the reversed list.
    
       
     
     
     
  def __str__(self):
      """ return string representation of the list items"""
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return "["+','.join(elements) + "]"
    
### try the following:    
# my_list = LinkedList()

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)

# print(my_list.reverse())

  

    
    
    
      
    
    
    
    
    
  


