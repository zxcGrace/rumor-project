#get text_vectors.txt
#get the entire corpus of the text
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import csv
'''
tokenize = TweetTokenizer()
count = dict()
with open('textwithout.txt','r') as input:
    for row in csv.reader(input):
        string = str(row)
        newstr1 = string.replace('[','')
        newstr2 = newstr1.replace(']','')
        newstr3 = newstr2.replace("'",'')
        list = tokenize.tokenize(newstr3)
        for word in list:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
for key in count:
    print(key,count[key])
'''
f = open('final_text.txt','r')
reasons = f.read()
tokenize = word_tokenize(reasons)

count = dict()

for word in tokenize:
    #if word == 'anti-vaxxers':
    #    print('#')
    if word in count:
        count[word] +=1
    else:
        count[word] =1

for key in count:
    print(key,count[key])
