# this is a tutorial file for me, it's not releated to the challenge
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
   
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

#  ----- Depth First Values Algo -----
def depth_first_values_iterative(root):
  if root is None:
    return []
  
  results = []
  stack = [root]
  
  while len(stack):
    current_node = stack.pop()
    results.append(current_node.value)
    
    if current_node.right:
      stack.append(current_node.right)
    if current_node.left:
      stack.append(current_node.left)
    
  return results
def depth_first_values_recursive(root):
  
  if root is None:
    return []
  else:
    left_values  = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)
  return [root.value,*left_values,*right_values]




#  ----- Breadth First Values Algo -----
def breadth_first_values_iterative(root):
  results = []
  queue = [root]
  if queue is None:
    return []
  while len(queue):
    current_node = queue.pop(0)
    results.append(current_node.value)
    
    if current_node.left:
      queue.append(current_node.left)
    if current_node.right:
      queue.append(current_node.right)
      
  return results

def breadth_first_values_recursive(root):
  # we can not use recursion to traverse the tree using the breadth_first_values. 
  # because under the hood recursion use stack and breadth_first_values_ need queus to be implemented. 
  pass
      


