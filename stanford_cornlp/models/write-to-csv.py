import csv
with open('output.txt','r') as input:
    with open('noun-phrase.csv','w') as output:
        for row in csv.reader(input):
            string = str(row)
            newstr1 = string.replace('[','')
            newstr2 = newstr1.replace(']','')
            newstr3 = newstr2.replace("'",'')
            newstr3 = newstr3.replace('"','')
            writer = csv.writer(output)
            writer.writerow([newstr3])
            #[output.write(" ".join(row)+'\n') for row in csv.reader(input)]
