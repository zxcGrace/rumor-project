import csv
import re
with open('text.txt','w') as output:
    with open('text.csv','r') as input:
        for row in csv.reader(input):
            string = str(row)
            newstr1 = string.replace('[','')
            newstr2 = newstr1.replace(']','')
            newstr3 = newstr2.replace("'",'')
            newstr3 = newstr2.replace("\n",'')
            #newstr3 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newstr3).split())
            output.write(newstr3+'\n')
        #[output.write(" ".join(row)+'\n') for row in csv.reader(input)]
