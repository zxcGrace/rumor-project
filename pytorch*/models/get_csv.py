import csv
import re
file = open('classified_biclf.txt','r')
with open('classified_biclf.csv','w') as output:
    for row in file:
        #newstr3 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newstr3).split())
        output.write(row)

    #[output.write(" ".join(row)+'\n') for row in csv.reader(input)]
