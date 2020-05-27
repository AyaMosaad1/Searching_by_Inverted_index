import os
import re
import pathlib


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        # at the End Of Word is set which represent the name of docs that have this word
        # self.end = set()
        self.end = []


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
        # node.end.add(doc)
        node.end.append(doc)

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
            node.end = self.remove_dup(node.end)
            return node.end

    #
    #     @briefremove_dup:
    #       1.Remove dupliceted items from list
    #       @param d_list 
    #       @return  return set with unique elements
    #

    def remove_dup(self , d_list):
        final_list = []
        [final_list.append(x) for x in d_list if x not in final_list]
        return  final_list



#     @brief readallfiles:
#       1.takes the chosen directory from gui and the object
#       2.opens each part individually in for loop
#       3.check if chosen part is a file
#       4.convert all words found in it to a string, split it by space, . and @ and add it to a list
#       5.remove all punctuation in the word and if the word has 's, take word till the '
#       6.insert word in trie
#       7.close the file
#       @param directory of folder and object of our class trie
#       @return nothing

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
            keys.clear()

