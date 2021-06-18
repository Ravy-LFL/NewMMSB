#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
import matplotlib.pyplot as plt
import os
if len(sys.argv) != 3 :
    print("please enter the path of the two folders")
else :
    fichier1=sys.argv[1]
    fichier2=sys.argv[2]

f1=open(fichier1,"r")
f2=open(fichier2,"r")
fresult=open("result_file.tab","w")

# Premiere etape : readline les deux fichiers en entrées
F1=f1.readlines()
F2=f2.readlines()

#Format d'une ligne : "NumeroResidu.Atome Déplacement 0/n"
#Mise en page du premier fichier a fin de le rendre utilisable, on a créer une liste contenant plusieurs liste contenant elle meme en index[0]: residu+Atome et en index[1]:CS+0
print("\n =========== New folder =========== \n")
nouveau_f1=[]
nueva_f1=[]
for i in F1 :
    new_F1=i.split("\n")
    nouveau_f1.append(new_F1[0])
for i in nouveau_f1:
    new_element=i.split("      ")
    nueva_f1.append(new_element)
le_nouveau_f1=[]

for i in nueva_f1 :
    if len(i)==1:
         new_element=i[0].split("     ")
         le_nouveau_f1.append(new_element)
    else :
        le_nouveau_f1.append(i)
#Mise en page du second fichier
nouveau_f2=[]
nueva_f2=[]
for i in F2 :
    new_F2=i.split("\n")
    nouveau_f2.append(new_F2[0])
for i in nouveau_f2:
    new_element=i.split("      ")
    nueva_f2.append(new_element)
le_nouveau_f2=[]

for i in nueva_f2 :
    if len(i)==1:
         new_element=i[0].split("     ")
         le_nouveau_f2.append(new_element)
    else :
        le_nouveau_f2.append(i)
#Ecriture de la premiere ligne du fichier de sortie
fresult.write('Residue')
fresult.write('\t')
fresult.write('Atom')
fresult.write('\t')
fresult.write('Cs1')
fresult.write('\t')
fresult.write('Cs2')
fresult.write('\t')
fresult.write('Diff')
fresult.write('\t')
fresult.write('ratio_gyromagnetic')
fresult.write('\n')

#Comparaison + écriture du fichier de sortie
for i in le_nouveau_f1:
    for j in le_nouveau_f2:
        if i[0]==j[0]:
            pre_residue=i[0].split('.')
            residue=pre_residue[0]          #i[x][y]: i represente l'objet de la 'mega' liste, x represente l'objet contenu dans l'objet de la mega liste, y represente le caractere d'une chaine de caractere
            pre_atom=i[0].split('.')
            atom=pre_atom[1]
            pre_nb1=i[1].split(' ')
            pre_nb2=j[1].split(' ')
            if len(pre_nb1[0])==0 :
                Cs1=float(pre_nb1[1])
            else :
                Cs1=float(pre_nb1[0])
            Cs1_str=str(Cs1)
            if len(pre_nb2[0])==0 :
                Cs2=float(pre_nb2[1])
            else :
                Cs2=float(pre_nb2[0])
            Cs2_str=str(Cs2)
            diff=Cs1-Cs2
            diff_round=round(diff,3)
            diff_str=str(diff_round)
            fresult.write(residue)
            fresult.write('\t')
            fresult.write(atom)
            fresult.write('\t')
            fresult.write(Cs1_str)
            fresult.write('\t')
            fresult.write(Cs2_str)
            fresult.write('\t')
            fresult.write(diff_str)
            fresult.write('\t')
            fresult.write('\t')
            if 'C' in atom :                                        #ECRITURE NOUVEL COLONNE SELON RAPPORT GYROMA
                ratio=diff*0.25144953
                ratio_round=round(ratio,3)
                ratio_str=str(ratio_round)
            elif 'N' in atom :
                ratio=diff*0.101329118
                ratio_round=round(ratio,3)
                ratio_str=str(ratio_round)
            else :
                ratio_str='none'
            fresult.write(ratio_str)
            fresult.write('\n')

#Création de l'histogramme
fig1, ax=plt.subplots(figsize=(10,6))
bar_width = 1.0
plt.title("CSPs for "+fichier1+" "+"and "+fichier2)
plt.xlabel('Residue number', fontsize=12)
plt.ylabel('CSP (ppm)', fontsize=12)
plt.show()





f1.close()
f2.close()
fresult.close()
