class Node :

    def __init__(self):
        self.child = [None]*26
        self.end = set()

class Trie :
    def __init__(self):
        self.root = Node()

    def inset (self, word, dec):
        word =word.casefold()
        length = len(word)
        node = self.root 

        for i in range(length):
            index = ord(word[i])-ord('a')
            if not node.child[index]:
                node.child[index] = Node()
            node=node.child[index]   
        node.end.add(dec)   

    def search(self, word): 
        word =word.casefold()
        node = self.root 
        length = len(word) 
		    
        for i in range(length): 
            index = ord(word[i])-ord('a') 
            if not node.child[index]: 
                return False
            node = node.child[index] 
        if len(node.end) == 0 :
            return  False
        else:
            return node.end



T = Trie()
T.inset("toka","first")
T.inset("abdo","first")
T.inset("sara","Scond")
T.inset("Sara","first")
T.inset("sara","first")
T.inset("Sara","seond")
# T.inset("a","Scond")
L=T.search("Sara")


print(L)
