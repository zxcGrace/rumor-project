#generate a csv file with only misinformation (1) and specific columns 1,2,3,4,6,13,14
import pandas as pd
import csv

with open('tw+ca+ne+np.csv','r') as input, open('1_2_3.csv', 'w') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if (row[1] == '1') or (row[1] == '2') or (row[1] == '3'):
            writer.writerow(row)
        
