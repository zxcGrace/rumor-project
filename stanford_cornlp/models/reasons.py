#accuracy 307/349 correct for 1 2 3 reasoning

import csv
import re

diseases = ['smallpox','B. parapertussis infection', 'heart attack', 'cancer', 'Juvenile diabetes', 'shingles', 'paralysis', 'cervical cancer', 'impairments in behavior and hippocampal neurogenesis', 'infectious disease', 'brains', 'asthma','bowel disease','kidney functions go down','encephalitis','HOMEOPATHY','parapertussis','seizures','allergies','SIDS','placebo','Fatigue','shingles','lizard morphing','behavior change','strains','hippocampal neurogenesis','Hand,Foot and Mouth disease','antibiotics','uillainBarreSyndrome','pneumonia','HPV']

vaccines = ['pertussis', 'hepatitis B', 'polio','Polio','chickenpox', 'measles', 'HPV','rotavirus','flu','Flu','DPT','MMR','Tdap','Hep B','DTap','anti NMDA receptor',' HBV Hepatitis B','Krabbe','Gardisil']

with open('1_2_3.csv','r') as input:
    with open('reasons123.csv','w') as output:
        for row in csv.reader(input):
            writer = csv.writer(output)
            '''
            print(row[3])
            print(type(row[3]))
            print(row[3][0])
            if (i for i in row[3]) in 'Dementia':
                print('yes')
            break
            '''

            if row[1] == '1':
                #ignore it for a moment
                if (re.search('aluminium', row[3], re.IGNORECASE)) or (re.search('aluminum', row[3], re.IGNORECASE)):
                    writer.writerow([row[0],row[1],'Aluminum helps vaccines work better. The average person takes in an estimated 30 to 50 mg of aluminum every day, mainly from foods, drinking water, and medicines. Not all vaccines contain aluminum, but those that do typically contain about .125 mg to .625 mg per dose, or roughly 1% of that daily average.'])

                elif (re.search('mercury', row[3], re.IGNORECASE)) or (re.search('Thimerosal', row[3], re.IGNORECASE)):
                    writer.writerow([row[0],row[1],'Thimerosal contains mercury that is used in vaccine. Thimerosal is added to vials of vaccine that contain more than one dose (multi-dose vials) to prevent growth of germs, like bacteria and fungi. Thimerosal does not stay in the body a long time so it does not build up and reach harmful levels. Thimerosal use in medical products has a record of being very safe.'])
                elif (re.search('dog kidney cells', row[3], re.IGNORECASE)) or (re.search('chicken', row[3], re.IGNORECASE)) or (re.search('fetal', row[3], re.IGNORECASE)) or (re.search('babies', row[3], re.IGNORECASE)) or (re.search('cancer tumor', row[3], re.IGNORECASE)) or (re.search('monkey', row[3], re.IGNORECASE)):
                    writer.writerow([row[0],row[1],'Viruses need cells to grow and tend to grow better in cells from humans than animals (because they infect humans). Some vaccines are made using human embryo cells (chickenpox, rubella, hepatitis A, one version of shingles vaccine, and one version of the rabies vaccine). These vaccines are not likely to cause harm. Because DNA is not stable when exposed to certain chemicals, much of it is destroyed in the process of making the vaccine. Therefore, the amount of human DNA in the final vaccine preparation is minimal (trillionths of a gram) and highly fragmented. Because the DNA is fragmented, it cannot possibly create a whole protein.'])
                else:
                    writer.writerow([row[0],row[1],'Today’s vaccines use only the ingredients they need to be safe and effective. Each ingredient in a vaccine serves a specific purpose. Vaccines include ingredients to help your immune system respond and build immunity to a specific disease. Some ingredients help make sure a vaccine continues to work like it’s supposed to and that it stays free of outside germs and bacteria. Some ingredients that are needed to produce the vaccine are no longer needed for the vaccine to work in a person. These ingredients are taken out after production so only tiny amounts are left in the final product. The very small amounts of these ingredients that remain in the final product aren’t harmful.'])
            elif row[1] == '2':
                #something need to be add into the bracket
                temp_list = row[3].split(' ')
                length = set(temp_list) & set(diseases)
                if (length == 0) and ((re.search('MMR',row[3],re.IGNORECASE)) or (re.search('measles',row[3],re.IGNORECASE)) or (re.search('mumps',row[3],re.IGNORECASE)) or (re.search('rubella',row[3],re.IGNORECASE)) or (re.search('pentavalent',row[3],re.IGNORECASE))):
                    if re.search('measles',row[3],re.IGNORECASE):
                        name = 'measles'
                    elif re.search('mumps',row[3],re.IGNORECASE):
                        name = 'mumps'
                    elif re.search('rubella',row[3],re.IGNORECASE):
                        name = 'rubella'
                    elif re.search('pentavalent',row[3],re.IGNORECASE):
                        name = 'pentavalent'
                    else:
                        name = ''
                    writer.writerow([row[0],row[1],'Before a combination vaccine %s is approved for use, it goes through careful testing to make sure the combination vaccine is as safe and effective as each of the individual vaccines given separately use. Side effects from combination vaccines %s are usually mild. They are similar to those of the individual vaccines given separately.' %(name,name)])
                elif re.search('side effect', row[3], re.IGNORECASE) or (re.search('dangerous', row[0], re.IGNORECASE)) or (re.search('side', row[3], re.IGNORECASE)) or (re.search('health', row[0], re.IGNORECASE)) or (re.search('safe', row[0], re.IGNORECASE)) or (re.search('changed', row[0], re.IGNORECASE)) or (re.search('quality', row[3], re.IGNORECASE)) or (re.search('probiotcs', row[0], re.IGNORECASE)):
                    writer.writerow([row[0],row[1],'There is not a plausible biologic reason to believe vaccines cause any serious long-term health effects. Based on more than 50 years of research on vaccines, we konw the likelihood that a vaccine will cause unanticipated long-term problems is extremely low.'])

                elif re.search('live virus', row[3], re.IGNORECASE) or (re.search('infected', row[0], re.IGNORECASE)) or (re.search('exposure', row[0], re.IGNORECASE)) or (re.search('defective', row[0], re.IGNORECASE)) or (re.search('worse', row[0], re.IGNORECASE)) or (re.search('suppose', row[0], re.IGNORECASE)):
                    writer.writerow([row[0],row[1],'With an inactivited (killed) vaccine, it is not possible to get a disease from the vaccine. Dead virus and bacteria can not causes diseases. With live vaccines, some people get what appears to be a mild case of disease. This is not harmful, and can actually show the vaccine is working.'])
                else:
                    new_row = row[3].split(' ')
                    for i in new_row:
                        i = i.lower()
                    #new_row.remove('')
                    #default
                    disease = 'injury'
                    vaccine = ''
                    if (set(new_row) & set(vaccines)) or (set(new_row) & set(diseases)):
                        length = set(new_row) & set(diseases)
                        if set(new_row) & set(vaccines):
                            vaccine = set(new_row) & set(vaccines)
                            vaccine = str(vaccine)
                            vaccine = vaccine.replace('}','')
                            vaccine = vaccine.replace('{','')
                            vaccine = vaccine.replace("'",'')
                        if set(new_row) & set(diseases):
                            disease = set(new_row) & set(diseases)
                            disease = str(disease)
                            disease = disease.replace('}','')
                            disease = disease.replace('{','')
                            disease = disease.replace("'",'')
                            if disease == 'brain':
                                disease = 'brain damage'

                    writer.writerow([row[0],row[1],'%s vaccine does not cause %s. Results from multiple studies and continued monitoring show that %s vaccine does not cause %s. ' %(vaccine,disease,vaccine,disease)])

            elif row[1] == '3':
                if (re.search('MMR', row[3], re.IGNORECASE)) or (re.search('mumps',row[3],re.IGNORECASE)) or (re.search('rubella',row[3],re.IGNORECASE)) or (re.search('measles',row[3],re.IGNORECASE)):
                    writer.writerow([row[0],row[1],'The MMR vaccine is very safe and effective. Two doses of MMR vaccine are about 97% effective at preventing measles; one dose is about 93% effective. Since the measles vaccination program started in 1963, widespread use of measles vaccine has led to a greater than 99% reduction in measles cases compared with the pre-vaccine era.'])
                elif re.search('flu', row[3], re.IGNORECASE):
                    writer.writerow([row[0],row[1],'While vaccine effectiveness can vary, recent studies show that flu vaccination reduces the risk of flu illness by between 40% and 60% among the overall population during seasons when most circulating flu viruses are well-matched to the flu vaccine.'])
                else:
                    writer.writerow([row[0],row[1],'Vaccines are very effective — and they’re the best protection against many serious diseases. Most people who get vaccinated will have immunity (protection) against the disease. Before a vaccine is recommended for use in the United States, the Food and Drug Administration (FDA) makes sure that it works — and that it’s safe. Since vaccines were invented, the number of babies and adults who get sick or die from vaccine-preventable diseases has gone way down — and some diseases have been wiped out altogether in the United States.'])
            elif row[1] == '4':
                if re.search('hepatitis B',row[3],re.IGNORECASE):
                    name = 'hepatitis B'
                else:
                    name = ''
                writer.writerow([row[0],row[1],'%s vaccine does not cause Autism. Results from multiple studies and continued monitoring show that %s vaccine does not cause Autism. For example, a 2014 meta-analysis in Vaccine examined studies involving a total of almost 1.3 million people. That same year, a paper in the Journal of the American Medical Association reported that no difference existed in autism rates between thousands of vaccinated and unvaccinated children. ' %(name,name)])
            elif row[1] == '6':
                writer.writerow([row[0],row[1],'This is a conspiracy ideation. There is no valid evidence proving the claims. Conspiracy theories present an attempt to explain away overwhelming scientific evidence that vaccines are effective, safe, and necessary.'])
            elif row[1] == '13':
                writer.writerow([row[0],row[1],'Multiple research studies have been conducted to look for possible links between vaccines and Sudden Infant Death Syndrome (SIDS). Results from these studies and continued monitoring show that vaccines do not cause SIDS. A 2003 Institute of Medicine (IOM) report “Immunization Safety Review: Vaccination and Sudden Unexpected Death in Infancy” The committee reviewed scientific evidence focusing on sudden unexpected death in infancy and looked for possible relationships between SIDS and vaccines.  Based on all the research findings they reviewed, the committee concluded that vaccines did not cause SIDS.'])
            elif row[1] == '14':
                writer.writerow([row[0],row[1],'N/A'])
