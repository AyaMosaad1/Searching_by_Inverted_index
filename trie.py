


import os
import re
import pathlib


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        # at the End Of Word is set which represent the name of docs that have this word
        # self.end = set()
        self.end = list()


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
                return "Not Found"
            node = node.child[index]
        if len(node.end) == 0:
            return "Not Found"
        else:
            return node.end




