import csv
from matplotlib import pyplot as plt
import numpy as np

#On initialise une liste pour chaque secteur d'énergie
fioul=[]
charbon=[]
gaz=[]
nucleaire=[]
eolien=[]
solaire=[]
hydraulique=[]
bioenergie=[]

#On ouvre le fichier
with open('RTE_2020.csv', 'r') as file:
    reader=csv.reader(file)
    lines=list(reader)

#On supprime une ligne sur deux
filtered_lines=[line for index, line in enumerate(lines) if index%2!=0]

#On supprime les deux dernières lignes du fichier
if lines:
    filtered_lines=filtered_lines[:-2]

#On écrit un nouveau fichier sans les deux dernières lignes et les lignes vides
with open('fichier_filtre.csv', 'w', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(filtered_lines)
 
#On ouvre ce fichier
with open('fichier_filtre.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        fioul.append(row)
        charbon.append(row)
        gaz.append(row)
        nucleaire.append(row)
        eolien.append(row)
        solaire.append(row)
        hydraulique.append(row)
        bioenergie.append(row)

#Pour chaque secteur d'energie on va rentrer les données correspondantes
        
fioul=[[fioul[i+1][7]] for i in range(len(fioul)-1)]
# ~ print(fioul)

charbon=[[charbon[i+1][8]] for i in range(len(charbon)-1)]
# ~ print(charbon)

gaz=[[gaz[i+1][9]] for i in range(len(gaz)-1)]
# ~ print(gaz)

nucleaire=[[nucleaire[i+1][10]] for i in range(len(nucleaire)-1)]
# ~ print(nucleaire)

eolien=[[eolien[i+1][11]] for i in range(len(eolien)-1)]
# ~ print(eolien)

solaire=[[solaire[i+1][12]] for i in range(len(solaire)-1)]
# ~ print(solaire)

hydraulique=[[hydraulique[i+1][13]] for i in range(len(hydraulique)-1)]
# ~ print(hydraulique)

bioenergie=[[bioenergie[i+1][15]] for i in range(len(bioenergie)-1)]
# ~ print(bioenergie)

#On calcul la moyenne de chaque secteur d'énergies
moy=[sum([int(item[0]) for item in fioul])/len(fioul) if fioul else 0,
    sum([int(item[0]) for item in charbon])/len(charbon) if charbon else 0,
    sum([int(item[0]) for item in gaz])/len(gaz) if gaz else 0,
    sum([int(item[0]) for item in nucleaire])/len(nucleaire) if nucleaire else 0,
    sum([int(item[0]) for item in eolien])/len(eolien) if eolien else 0,
    sum([int(item[0]) for item in solaire])/len(solaire) if solaire else 0,
    sum([int(item[0]) for item in hydraulique])/len(hydraulique) if hydraulique else 0,
    sum([int(item[0]) for item in bioenergie])/len(bioenergie) if bioenergie else 0]

#On crée le graphique
energies=['Fioul','Charbon','Gaz','Nucléaire','Eolien','Solaire','Hydraulique','Bioénergie']
plt.figure(figsize=(10, 10))
plt.pie(moy, labels=energies,autopct='%1.1f%%')
plt.title('Moyenne de chaque secteur énergétique en 2020')
plt.show()
