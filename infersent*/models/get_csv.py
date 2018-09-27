import csv
import re
file = open('textwithout.txt','r')
with open('textwithout.csv','w') as output:
    for row in file:
        #newstr3 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newstr3).split())
        output.write(row)
        
    #[output.write(" ".join(row)+'\n') for row in csv.reader(input)]
