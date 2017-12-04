
from __future__ import print_function

def is_isogram(word):
    if len(word) == 0:
   	 word_tuple = (word, False)
   	 print (word_tuple)
    elif not isinstance(word, str):
   	 word_tuple = (word, False)
   	 raise TypeError("Argument should be a string")
    else:
   	 if len(word) == len(set(word)):
   		 word_tuple = (word, True)
   		 print (word_tuple)
   	 else:
   		 word_tuple = (word, False)
   		 print (word_tuple)

is_isogram("abolishment")