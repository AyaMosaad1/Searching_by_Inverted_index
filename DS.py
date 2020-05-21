#from nltk import tokenize
#import  nltk

#nltk.download('punkt')
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
import re
import string

#for line in file

with open("E:\DS Project\dsdoc.txt","r") as file:

 #dh 3chan mytb3sh \n bs
   string_without_line_breaks = ""
   for line in file:
    stripped_line = line.rstrip()
    string_without_line_breaks += stripped_line
    #string_without_line_breaks = string_without_line_breaks.replace(',' , "  ")

file.close()

word="pansea"

result=(re.findall(r"[^.]*?"+(word)+r"[^.]*.", string_without_line_breaks))


#for i in string_without_line_breaks:
# if (string_without_line_breaks[(len(word)+1)]== 'a'):


#result=(re.findall(r"[^.]*?\S"+(word.lower())+r"[^.]*\.S", string_without_line_breaks))



print(result)

