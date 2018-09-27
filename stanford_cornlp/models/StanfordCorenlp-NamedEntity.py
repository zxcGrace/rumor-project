#get named_entity using StanfordCoreNLP
from stanfordcorenlp import StanfordCoreNLP
import re
import csv
nlp = StanfordCoreNLP('http://localhost',9000)

total_entity = []
with open('text.csv','r') as input:
    for row in csv.reader(input):
        p = []
        string = str(row)
        newstr1 = string.replace('[','')
        newstr2 = newstr1.replace(']','')
        newstr3 = newstr2.replace("'",'')
        sentence = newstr3.replace('#','')
        sentence = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",sentence).split())
        #print(sentence)
        #print('Named Entities:', nlp.ner(sentence))

        named_entity = nlp.ner(sentence)
        for i in named_entity:
            if i[1] == 'NUMBER' or i[1] == 'CAUSE_OF_DEATH' or i[1] == 'DATE' or i[1] == 'ORGANIZATION' or i[1] == 'PERCENT' or i[1] == 'LOCATION' or i[1] == 'MONEY' or i[1] == 'TIME' or i[1] == 'IDEOLOGY' or i[1] == 'NATIONALITY' or i[1] == 'RELIGION' or i[1] == 'STATE_OR_PROVINCE' or i[1] == 'TITLE' or i[1] == 'DURATION':
                if (p) and (p[-1][1] == i[1]):
                    temp = list(p[-1])
                    temp.insert(-1,i[0])
                    p[-1] = tuple(temp)
                else:
                    p.append(i)
        total_entity.append(p)

    with open('named_entity.csv','w') as output:
        for i in total_entity:
            print(i)



'''
sentence = "RT @HealthRanger: Dementia now striking people in their 40s as mercury from vaccines causes slow, degenerative brain damage. https://t.co/i蘝錩"
#print( 'Tokenize:', nlp.word_tokenize(sentence))
#print( 'Part of Speech:', nlp.pos_tag(sentence))
print( 'Named Entities:', nlp.ner(sentence))
np = nlp.parse(sentence)
print( 'Constituency Parsing:', np)
print("Type :",type(np))
print("Lentn: ",len(np))

#print( 'Dependency Parsing:', nlp.dependency_parse(sentence))
'''
nlp.close() # Do not forget to close! The backend server will consume a lot memery.
