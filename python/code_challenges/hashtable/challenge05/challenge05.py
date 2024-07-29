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
    
  def hashing_alg(self,key):
    
    hash_value  = 5999
    for char in str(key):
      hash_value = (hash_value*99) + ord(char)
    
    return hash_value%self.size
    
  def insert(self,key,value):
    '''insert method to inser a key and value pair into the HashTable'''
    index = self.hashing_alg(key)
    if self.table[index] is None:
      self.table[index] = LinkedList(key,value)
    else:
      current = self.table[index]
      while current:
        if current.key == key:
          current.value = value
          return
        if current.next is None:
          break
        current = current.next
      current.next = LinkedList(key,value)
      
  def update(self,key,new_value):
    index = self.hashing_alg(key)
    current = self.table[index]
    while current:
      if current.key == key:
        current.value = new_value
        return
      current = current.next
    
    return None
  
  def search(self,key):
    ''' search for particular value using the assoicated key'''
    index = self.hashing_alg(key)
    current = self.table[index]
    
    while current:
      if current.key == key:
        return current.value
      current = current.next
    
    return None


def helper_function(list_1,list_2):
  '''helper function to get the intersection number between two list'''
  intersection_list = []
  hash_table = HashTable()
  
  for item in max(list_1,list_2,key=len):
    hash_table.insert(item,item)
  
  for item in min(list_1,list_2,key=len):
    if hash_table.search(item):
      intersection_list.append(hash_table.search(item)) 
  
  intersection_list = sorted(list(set((intersection_list))))
  return(intersection_list)
    