# Write here the code challenge solution
def isValid(s):
  stack = []
  symbols = {')': '(', '}': '{', ']': '['}
  
  for char in s:
    if char in symbols.values():
      stack.append(char)
    elif char in symbols:
      if len(stack) > 0:
        stack.pop()
      else:
        return False
    else:
      if len(stack) == 0:
        return False
      
        
        
        
  return not stack



