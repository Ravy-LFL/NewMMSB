#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
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
nouveau_f1=[]
nueva_f1=[]
for i in F1 :
    new_F1=i.split("\n")
    print(new_F1)
    nouveau_f1.append(new_F1[0])
for i in nouveau_f1:
    new_element=i.split("      ")
    print("le new elment")
    print(new_element)
    nueva_f1.append(new_element)
for i in nueva_f1:
    new_element=i.split("      ")
    print('le new element')
    print(new_element)



print("voici F1 :")
print(nueva_f1)
print("\n")
print("voici F2 :")
print(new_F2)


f1.close()
f2.close()
fresult.close()
