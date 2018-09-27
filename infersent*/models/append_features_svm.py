#get text_vectors.txt
#get the entire corpus of the text
import nltk
import re
import numpy as np
import csv
from sklearn import preprocessing
from nltk.sentiment.vader import SentimentIntensityAnalyzer

hashtag = ['#vaxwithme','#vaxxed','#vaccines','#vaccineswork','#vaccine','#BigPharma','#autism','#Vaccines','#CDC','#LearnTheRisk','#vaxxed','#VAXXED','#antivax','#vaccines','#Autism','#VaccineSafety']
text_vec = np.loadtxt('final_sen_text.txt')
i = 0
#m = (1,4116)
#m = (1,4112)
m = (1,316)
nparray = np.zeros(m)
hashtags = []
sid = SentimentIntensityAnalyzer()
total_ss = []
p = 0
with open('final_text.csv','r') as input:
    for row in csv.reader(input):
        string = str(row)
        newstr1 = string.replace('[','')
        newstr2 = newstr1.replace(']','')
        newstr3 = newstr2.replace("'",'')
        sstemp = []
        ss = sid.polarity_scores(newstr3)
        for k in ss:
            sstemp.append(ss[k])
        total_ss.append(sstemp)
        temp = []
        for a in hashtag:
            if a in newstr3:
                temp.append(1)

            else:
                temp.append(0)
        hashtags.append(temp)

    '''
    attitude = []
    with open('att.csv','r') as int:
        for row in csv.reader(int):
            new = str(row)
            new = new.replace('[','')
            new = new.replace(']','')
            new = new.replace("'",'')
            if new == '-1':
                attitude.append(-1)
            elif new == '1':
                attitude.append(1)
            else:
                attitude.append(0)
    '''

    #append total_ss to hashtags
    '''
    l = 0
    for o in total_ss:
        for k in o:
            # 6 ->64%
            #10
            hashtags[l].append(float(k))
        l += 1
    '''

    hashtags = preprocessing.normalize(hashtags)

    for a in hashtags:
        l = np.append(text_vec[i],a,axis=0)
        nparray = np.append(nparray,[l],axis=0)
        i += 1
    nparray = np.delete(nparray,0,axis=0)
    np.savetxt('final_sen_text_new.txt',nparray)
    '''
    for a in hashtags:
        nparray = np.append(nparray,[a],axis=0)
    nparray = np.delete(nparray,0,axis=0)
    print(nparray)
    np.savetxt('sen_text_new.txt',nparray)
    '''
