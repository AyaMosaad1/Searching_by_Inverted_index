#from nltk import tokenize
#import  nltk

#nltk.download('punkt')
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
import re
import string
import os


#for line in file


with open("E:\DS Project\dsdoc.txt","r") as file:

   data=file.read()
   file.close()


def get_sentences(word):
   result={}

  # word = "roses"


 #  result=re.findall(r'(?:\d[,.]+(word)+[^,.])*(?:[,.]|$)', data)
   #result = (re.findall(r"[^.]*?" + (word.lower()) + r"[^.]*\.?", data))
   result = (re.findall(r"[^A,.?]*?" +(word.lower()) + r"[^.?,]*\.?", data))
   print (result)
final={}
final=get_sentences("coffe")
#print(final)
'''for i in final:

     final.append((i.strip()))

     print(final)
'''

# clean = open('E:\DS Project\dsdoc.txt').read().replace('\n', '')




#hnbdel asm l file b variable 3chan a7ot ay file



