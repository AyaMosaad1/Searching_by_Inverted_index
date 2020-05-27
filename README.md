# Searching_by_Inverted_index
---
## Project description
 inverted index was through building a trie that would take all words found in all documents and save them all in the same trie. At the end node of each word, we save the ids of all the documents that this word occurred in it. So now when we search for a word, we display this list of ids easily, as we only need to traverse one trie structure with the length of given word. 

While implementing this algorithm, we stumbled across some corner cases that required a solution. For example, since we build the trie children to include the 26 letters of the alphabet, any word that’s not in English (Japanese... Arabic …etc ) was difficult to input to our trie and so unfortunately we couldn’t support it. If a word had (‘s) or any other time of abbreviation would be stored in its original form, ex: master’s is saved as master. When we input our files, we separate the string inside using not only space but also “ . ”  and “@” so that we can handle as many corner cases as we can. Just for safety, we also remove any punctuation from our word before inserting it to our trie in case our conditions didn’t satisfy a particular word. 

---

## TO run it 
  1- clone https://github.com/AyaMosaad1/Searching_by_Inverted_index
      
  2- cd to repo directory
  
  3- install <pip install pyqt5>
  
  4- Run Gui.py
  
 ---

## Contributors 

  - Alaa Mohamed Abd El Rahman
  - Aya Mosaad Mohamed
  - Baraa Magdy El Sayed
  - Toka Abd El Hamid
  - Panse Yasser Mohamed
  
