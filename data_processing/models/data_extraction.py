#generate a csv file with only misinformation (1) and specific columns 1,2,3,4,6,13,14
import pandas as pd
import csv

reasoning = {
'1':'Vaccines Ingredient: The tweet discusses the ingredients of the vaccines as dangerous or causing negative side effects.',
'2':'Vaccines Safety: The tweet discusses the vaccine is unsafe or the tweet contains claims linking vaccines to harms (e.g., infections, diseases, illnesses) that are beyond known vaccine side effects.  If the tweet mentions autism refers to category 4.',
'3':'Vaccines Effectiveness: The tweet discusses the vaccine’s effectiveness in preventing infections and diseases.',
'4':'Autism: The tweet discusses autism as a potential side effect of vaccines.',
'5':'Vaccine and Shaken Baby Syndrome: The tweet discusses the Shaken Baby Syndrome as a potential side effect of vaccines.',
'6':'Vaccine conspiracy: The tweet contains information arguing government and pharmaceutical companies reap money by promoting vaccinations.',
'7':'Vaccine schedule: The tweet contains information arguing an alternative vaccine schedule (spaced-out schedule) is safer.',
'8':'Vaccine coverage: The tweet contains  information arguing the majority of people do not get vaccinations or the majority of parents do not get their kids vaccinated.',
'9':'Vaccine research and approval: The tweet contains information arguing vaccines are not rigorously evaluated before they get approved.',
'10':'Vaccine and scientific evidence: The tweet contains information arguing most scientists are anti-vaccines and the tweet cites  evidence about vaccine.',
'11':'Vaccine necessity and herd immunity: The tweet contains  information arguing there is no need for getting vaccines because others have been vaccinated (herd immunity).',
'12':'Vaccine necessity and illnesses: The tweet contains information arguing vaccine-preventable diseases are not serious.',
'13':'Vaccine and infant mortality: The tweet contains  information arguing for a link between vaccines and infant mortality.',
'14':'N/A: The tweet does not discuss about potential side effects nor harms associated with the vaccine or does not fit in the above categories.'
}

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
with open('need.csv','r') as input, open('need1.csv', 'w') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        '''
        if row[11] == '1':
            if row[12] == '1':
                a += 1
            elif row[12] == '2':
                b += 1
            elif row[12] == '3':
                c += 1
            elif row[12] == '4':
                d += 1
            elif row[12] == '5':
                e += 1
            elif row[12] == '6':
                f += 1
            elif row[12] == '7':
                g += 1
            elif row[12] == '8':
                h += 1
            elif row[12] == '9':
                i += 1
            elif row[12] == '10':
                j += 1
            elif row[12] == '11':
                k += 1
            elif row[12] == '12':
                l += 1
            elif row[12] == '13':
                m += 1
            elif row[12] == '14':
                n += 1
    print(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
        origional:24 134 12 57 0 14 1 0 1 1 3 0 8 47
        new added:17 162 10 37 0 38 4 0 0 1 1 0 14 11
        #only use 1,2,3,4,6,13,14 as categories

        if (row[1] == '1'):
            writer.writerow(row)
        '''
        if row[1] == '1':
            if row[2] == '1':
                #row[12] = reasoning['1']
                writer.writerow(row)
            elif row[2] == '2':
                #row[12] = reasoning['2']
                writer.writerow(row)
            elif row[2] == '3':
                #row[12] = reasoning['3']
                writer.writerow(row)
            elif row[2] == '4':
                #row[12] = reasoning['4']
                writer.writerow(row)
            elif row[2] == '6':
                #row[12] = reasoning['6']
                writer.writerow(row)
            elif row[2] == '13':
                #row[12] = reasoning['14']
                writer.writerow(row)
            elif row[2] == '14':
                #row[12] = reasoning['14']
                writer.writerow(row)

    #things needed in the final csv file
    #misinformation = 1错误信息
    #reasoning = 1,2,3,4,6,14
    #text, reasoning(only two columns needed for now)
