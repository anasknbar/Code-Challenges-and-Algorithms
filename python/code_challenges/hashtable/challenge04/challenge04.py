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
        if current.next is None:
          break
        current = current.next
    
      current.next = LinkedList(key,value)
  
  def search(self,key,value):
    ''' search for particular value using the assoicated key'''
    index = self.hashing_alg(key) 
    current = self.table[index]
    while current:
      if current.key == key and current.value == value:
        return (current.key,current.value)
      current = current.next
      
    raise KeyError('key not found')
  
  def update(self,key,new_value):
    index = self.hashing_alg(key)
    
    current = self.table[index]
    while current:
      if current.key == key:
        current.value = new_value
        return
      current = current.next
    raise KeyError('key not found')
  
  
  
def helper_function(list_1,list_2):
  '''helper function to get the sorted names array '''
  if len(list_1) != len(list_2):
    return
  
  list_ = []
  
 
  hashtable = HashTable()
  for key,value in zip(list_1,list_2):
    hashtable.insert(key,value)
  
  for i in range(len(list_1)):
    list_.append(hashtable.search(list_1[i],list_2[i]))
 
  sorted_data = sorted(list_, key=lambda x: x[1])

  sorted_names = [name for name, number in sorted_data]
  return(sorted_names)
    
  
 
  
  
  
      

    
      
    
        


      
      
      
      
    

hashtable = HashTable(10)

# hashtable.insert('name','Anas')
# hashtable.insert('phone','12345')

# print(hashtable.search('name'))
# print(hashtable.search('phone'))

# hashtable.update('name','ali')
# hashtable.update('phone','99999')

# print(hashtable.search('name'))
# print(hashtable.search('phone'))


    
    
    