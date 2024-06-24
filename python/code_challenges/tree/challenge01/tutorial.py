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
### iterative version:
# def depth_first_values(root):
  
#   if root is None:
#     return []
#   else:
#     results = []
#     stack = [root]
    
#     while len(stack):
#       current_node = stack.pop()
#       results.append(current_node.value)
      
#       if current_node.right:
#         stack.append(current_node.right)
#       if current_node.left:
#         stack.append(current_node.left)
    
#   return results    
# print(depth_first_values(a))

### recursive version:
# def depth_first_values(root):
#   if root is None:
#     return []
#   else:
#     left_values  = depth_first_values(root.left)
#     right_values = depth_first_values(root.right)
#   return [root.value,*left_values,*right_values]
# print(depth_first_values(a))


#  ----- Breadth First Values Algo -----

def breadth_first_values(root):
  results = []
  queue = [root]
  
  if root is None:
    return []
  else:
    while len(queue):
      cuurent_node = queue.pop(0)
      results.append(cuurent_node.value)
      
      if cuurent_node.left:
        queue.append(cuurent_node.left)
      if cuurent_node.right:
        queue.append(cuurent_node.right)
  return results  
print(breadth_first_values(a))
      


