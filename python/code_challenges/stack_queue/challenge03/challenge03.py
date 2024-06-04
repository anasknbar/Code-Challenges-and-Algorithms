# Write here the code challenge solution
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    
class Stack:
  def __init__(self):
    self.top = None
    self.stack_size =  0
    
    
  def push(self,value): 
    
    self.stack_size += 1
    
    new_node = Node(value)
    
    if self.top is None:
      self.top = new_node
      
    
    else:
      new_node.next = self.top
      self.top = new_node
      
   
    
      
      
      
   
  def pop(self):
    ''' Removes and return the top element from the stack. '''
    self.stack_size -= 1
    if self.top is None:
      raise IndexError("stack is empty, can not do pop operation")
    poped_value = self.top.value
    self.top = self.top.next
    return poped_value
  
  def peek(self):
    ''' Returns the top element without removing it. '''
    if self.top is None:
      raise IndexError("stack is empty, can not do Peek operation")
    return self.top.value
  
  def size(self):
    return self.stack_size 
  
  def IsEmpty(self):
    ''' Checks if the stack is empty. '''  
    if self.top is None:
      return True
    else:
      return False 
  
  def DeleteMiddleNode(self):
    if self.top is None:
      raise IndexError("stack is empty, can not do DeleteMiddleNode operation")
    
    elif self.top.next is None:
      deleted_value = self.top.value
      self.top = None
      return deleted_value
  
    else:
      s_size = self.size()
      middle_index = s_size//2
      counter = 0
        
      previous_node = None
      current_node = self.top

      while counter != middle_index:
        previous_node = current_node
        current_node = current_node.next
        counter += 1
       
      previous_node.next = current_node.next
      self.stack_size -= 1
      return current_node.value
    
    
    
  
  def __str__(self):
    values = []
    
    current_node = self.top
    while current_node:
      values.append(str(current_node.value))
      current_node = current_node.next
    
    stack_string = "\nTOP ===> |  "+ values[0] +"  |\n"
    
    for value in values[1:]:
      stack_string +="         |  "+value+"  |\n"
    return stack_string
    # return f"TOP ===> { ' -> '.join(values) }"
  



