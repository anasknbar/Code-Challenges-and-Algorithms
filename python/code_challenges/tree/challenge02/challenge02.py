# Write here the code challenge solution

class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
    
def breadth_first_values_iterative(root):
  results = []
  queue = [root]
  if queue is None:
    return []
  while len(queue):
    current_node = queue.pop(0)
    try:
      results.append(current_node.value)
    except AttributeError:
      results.append(None)
      continue
    
    if current_node.left:
      queue.append(current_node.left)
    else:
      queue.append(None)
    if current_node.right:
      queue.append(current_node.right)
    else:
      queue.append(None)
    
      
      
  return results


def compare(root_1,root_2):
  if breadth_first_values_iterative(root_1) == breadth_first_values_iterative(root_2):
    return True
  else:
    return False  
  




