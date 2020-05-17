class TrieNode:    
    def __init__(self):
        self.child = [None]*26
      # at the End Of Word is set which represent the name of docs that have this word
        self.end = set()


class Trie :
    def __init__(self):
        self.root = TrieNode()

# 
#     @brief insert:
#       1.to covert all capital letters to small
#       2. convert the words to trie
#       3.the last node after word has set which Contain the name of docs which have this word 
#       @param word to be inserted in trie
#       @param doc the name of current doc
#       @return try have all words of docs 
# 

    def insert (self, word, doc):

# 
#     @brief search:
#       1.covert all capital letters to small
#       2.take the len of word than search about it in trie 
#       @param word which need to find 
#       @return  return set of docs' name on success, or false if there don't find the word 
# 

    def search(self, word): 



# 
#     @brief fileToList:
#       1.take the first line in file 
#       2.convert string to list
#       @param name of string 
#       @return  list of words
# 
#

def fileToList(namefile):



# 
#     @brief NameOfDoc:
#       1.save name of doc in var  
#       @return  this var 
# 
#

def NameOfDoc(namefile):

