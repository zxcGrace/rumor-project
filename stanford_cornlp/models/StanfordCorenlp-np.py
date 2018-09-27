#get noun phrase using StanfordCoreNLP
from stanfordcorenlp import StanfordCoreNLP
import re
import csv
nlp = StanfordCoreNLP('http://localhost',9000)
#get all noun phrase
def get_np(s):
    final_res = []
    for i in range(0,len(s)):
        #print(s[i:i+4])
        if s[i:i+3] == "(NP" and (s[i+4] < 'A' or s[i+4] > 'Z'):
            #print("find")
            res = ""
            count = 0
            for j in range(i+4,len(s)):
                if s[j] == "(":
                    count+=1
                elif s[j] == ")":
                    count-=1
                    if count == -1:
                        break
                    if s[j-1] == ")":
                        continue
                    flag = j-1
                    while s[flag]!=" ":
                        flag-=1
                        #print(res)
                    res+=s[flag+1:j]
                    res+=" "
            final_res.append(res[:-1])
    return final_res

total_np = []
with open('text.csv','r') as input:
    for row in csv.reader(input):
        p = []
        string = str(row)
        newstr1 = string.replace('[','')
        newstr2 = newstr1.replace(']','')
        newstr3 = newstr2.replace("'",'')
        sentence = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newstr3).split())
        parser_result = nlp.parse(sentence)
        total_np.append(get_np(parser_result))


    for i in total_np:
        print(i)

#sentence = "RT @HealthRanger: Dementia now striking people in their 40s as mercury from vaccines causes slow, degenerative brain damage. https://t.co/i蘝錩"
#sentence = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",sentence).split())
#print( 'Constituency Parsing:', np)
#print( 'Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close() # Do not forget to close! The backend server will consume a lot memery.
