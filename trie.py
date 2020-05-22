import os
import re
import pathlib


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        # at the End Of Word is set which represent the name of docs that have this word
        self.end = set()


class Trie:
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

    def insert(self, word, doc):
        # to covert all capital char to small
        word = word.casefold()

        length = len(word)
        node = self.root

        for i in range(length):
            index = ord(word[i]) - ord('a')
            if 0 <= index <= 26:
                if not node.child[index]:
                    node.child[index] = TrieNode()
                node = node.child[index]
        node.end.add(doc)

    #
    #     @brief search:
    #       1.covert all capital letters to small
    #       2.take the len of word than search about it in trie
    #       @param word which need to find
    #       @return  return set of docs' name on success, or false if there don't find the word
    #

    def search(self, word):
        word = word.casefold()

        node = self.root
        length = len(word)

        for i in range(length):
            index = ord(word[i]) - ord('a')
            if not node.child[index]:
                return False
            node = node.child[index]
        if len(node.end) == 0:
            return False
        else:
            return node.end
    def remove_dup(mylist):
     fial_list = []
     [fial_list.append(x) for x in mylist if x not in fial_list]
     return  fial_list
'''for debug
listy=[1,2,3,2,4]
print(Trie.remove_dup(listy))
'''
#
#     @brief fileToList:
#       1.take the first line in file
#       2.convert string to list
#       @param name of string
#       @return  list of words
#
#

def readallfiles(p, hello):
    for path in pathlib.Path(p).iterdir():
        if path.is_file():
            current_file = open(path, "r", encoding='UTF-8')
            s = current_file.read()
            import re
            # D, file, anotherfile, name = path.split('/')
            keys = list(map(str, re.split('[@. ]', s)))[:len(s)]
            for key in keys:
                if key.find("’") != -1:
                    x = key.find("’")  # ’ mo5tlfa 3an '
                    key = key[:x]
                else:
                    key = ''.join([i for i in key if i.isalpha()])
                hello.insert(key, path.name)
            current_file.close()



#"D:/DATA STRUCTURE/questions"

T = Trie()
readallfiles("D:/DATA STRUCTURE/textfiles", T)

#words = filesread()
#print(words)
#for word in words:
#    T.insert(word, "First")

# T.insert("toka", "second")
# T.insert("abdo", "first")
# T.insert("sara", "Second")
# T.insert("Sara", "first")
# T.insert("sara", "first")
# T.insert("Sara", "second")

L = T.search("this")
#D = T.search("this")
print(L)
