# Write your test here
from challenge02 import isValid

def test_isValid_function():
  assert isValid("()") == True
  assert isValid("()[]{}") == True
  assert isValid("[({}]") == False
  assert isValid("[(hello)()]") == True
  assert isValid("[{(())}]") == True