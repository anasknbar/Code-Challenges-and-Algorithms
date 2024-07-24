# Write here the code challenge solution


class LinkedList:
  '''LinkedList class used for chaning proccess'''
  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.next = None
    
class HashTable:
  '''Initailizing the HashTable with a table'''
  def __init__(self,size=10):
    self.size = size
    self.table = [None]*self.size
    
  # standard HashTable Functions:
  def hashing_alg(self,key):
    hash_value = 3999
    for char in str(key):
      hash_value = (hash_value*99) + ord(char)
    return hash_value % self.size
  
  def insert(self,key,value):
    index = self.hashing_alg(key)
    # if the slot is empty
    if self.table[index] is None:
      self.table[index] = LinkedList(key,value)
    # if the slot is not empty
    else:
      current = self.table[index]
      while current:
        # we check if the key is already in the slot update its value, we do not want to have a dublicated keys
        if current.key == key:
          current.value = value
          return
        # if we reach the end of the LinkedList and there is no dublicated key, get out of the loop
        if current.next is None:
          break
        current = current.next
      current.next = LinkedList(key,value)
  
  def search(self,key):
    ''' search for particular value using the assoicated key'''
    index = self.hashing_alg(key)
    current = self.table[index]
    while current:
      if current.key == key:
        return current.value
      current = current.next
    return None
  
  def update(self,key,new_value):
    '''update a value using its key'''
    index = self.hashing_alg(key)
    current = self.table[index]
    while current:
      if current.key == key:
        current.value = new_value
      current = current.next
    return False
              
  # helper Functions:  
  
  # this function used for increment the value by its repeptition 
  def increment(self,key):
    '''The increment method is used to count occurrences of elements in the array.'''
    index = self.hashing_alg(key)
    
    current = self.table[index]
    while current:
      if current.key == key:
        current.value += 1
        return
      current = current.next
      
    self.insert(key,1)
    
  def items(self):
    '''The items method is a generator that iterates over all key-value pairs (element and its count) in the hash table.'''
    for index in range(self.size):
      current = self.table[index]
      while current:
        yield current.key , current.value
        current = current.next
        

def sum_of_unique_elements(nums_list):
  element_counts = HashTable()
  for num in nums_list:
    element_counts.increment(num)
    
  unique_sum = 0
  
  for key,count in element_counts.items():
    if count == 1:
      unique_sum += key
      
  return unique_sum