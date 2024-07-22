# Write here the code challenge solution


class Hashtable():
  ''' Initalize the Hashtable class with a size and a table(a list)'''
  def __init__(self,size):
    self.size = size
    self.table = [[] for _ in range(size)]
    
  def hashing_alg(self,key):
    ''' hashing function use unicode function (ord) to return a random index  with the range of the table size '''
    hash_value = 1999
    for char in key:
      hash_value = (hash_value * 99) + ord(char)
    return hash_value % self.size


  def repeted_word(self,string):
    '''function help finding the repeated word in a given index. It takes a string and use hashtable to store each word in specific index in the hashing table'''
    repetition = []
    text = string.split()
    for word in text:
      index = self.hashing_alg(word)
 
      if word in self.table[index]:
        repetition.append(word)
      
      else:
        self.table[index].append(word) 
    
    if len(repetition) :
      return(', '.join(repetition))
    else:
      return("No Repetition")
        
        

    

  