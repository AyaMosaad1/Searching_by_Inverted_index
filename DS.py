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
# clean = open('E:\DS Project\dsdoc.txt').read().replace('\n', '')
'''string_without_line_breaks = ""
for line in file:
    stripped_line = line.rstrip()
    string_without_line_breaks += stripped_line
    #string_without_line_breaks = string_without_line_breaks.replace(',' , "  ")
'''

def get_sentences(word ):
 #word="roses"

 result={}
#hnbdel asm l file b variable 3chan a7ot ay file

 result=(re.findall(r"[^\n]*?"+(word.lower())+r"[^\n]*\n", data))
 final = []
 for i in result:
     final.append((i.strip()))
 return (final)
# for testing bs

'''for i in result:
    print(i)
'''
print(get_sentences("roses"))