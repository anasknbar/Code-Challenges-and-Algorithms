# Write your test here
from challenge02 import Hashtable


def test_repeted_word_function():
  hashtable = Hashtable(10)
  repeted_word = hashtable.repeted_word(" ASAC is a department at LTUC. ASAC teaches programming in LTUC")
  assert repeted_word == 'ASAC'
  
def test_no_repeted_word_function():
  hashtable = Hashtable(10)
  repeted_word = hashtable.repeted_word(" ASAC is a department at LTUC.")
  assert repeted_word == 'No Repetition'
  


