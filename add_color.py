#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import termcolor

if len(sys.argv) != 2 :
	sys.exit("VEUILLEZ SAISIR LE PATH DE LA SEQUENCE A COLORIER A LA SUITE DE LA COMMANDE DE LANCEMENT DU RPOGRAMME")
else :
	sequence = sys.argv[1]
s=open(sequence,"r")
sC=open(sequence+" color","w")
Basique=['K','R']
Acide=['E','D']
Hydrophobes=['A','I','L','M','F','V','Y','C']
Spe=['W','H']
Polaire=['N','Q','G','P','S','T']
aa=['A','R','D','N','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
'''
lysine,arginine = acides aminés basique
acide glutamique et acide aspartique = acides aminés acides
alanine, isoleucine, leucine, méthionine, phénylalanine, valine, tyrosine, cystéine = acide aminé hydrophobes
tryptophane et hystidine
asparagine,glutamine,glycine,proline,serine,thréonine= acide aminés polaire
'''
print("voici le code couleur par défaut : gris = acides aminés hydrophobe","\n","rouge = acide ", "\n", " bleu = basique","\n","jaune=tryptophane et hystidine","\n","vert = Polaire")
change_col=input("si vous voulez modifier ces couleurs appuyez sur y sinon appuyez sur n : ")

#sys.argv[2]=change_col
if change_col == 'n' :
    hydrophobe='grey'
    acide='red'
    basique='blue'
    spe='yellow'
    polaire='green'
if change_col == 'y' :
    hydrophobe=input("saisissez le nom de la couleur associer aux acides aminés hydrophobes")
    acide=input("saisissez le nom de la couleur associer aux acides aminés acide")
    basique=input("saisissez le nom de la couleur associer aux acides aminés basique")
    spe=input("saisissez le nom de la couleur associer aux tryptophane et à l'hystidine")
    polaire=input("saisissez le nom de la couleur associer aux acides aminés polaire")

ligne=s.readlines()
for i in range(1,len(ligne)) :
	list_line=list(ligne[i])
	for j in range(len(list_line)):
		print(j,end='')
		print('\n')
	for k in list_line:
    		if k in Basique :
    			sC.write(termcolor.colored(i,basique))
    			termcolor.cprint(k,basique,end='')
    		elif k in Acide :
    			termcolor.cprint(k,acide,end='')
    			sC.write(termcolor.colored(i,acide))
    		elif k in Hydrophobes and k=='L' or k=='I':
    			termcolor.cprint('\033[1m'+k+'\033[0m',hydrophobe,end='')
    			sC.write(termcolor.colored(i,hydrophobe))
    		elif k in Hydrophobes and k!='L' and  k!='I':
    			termcolor.cprint(k,hydrophobe,end='')
    			sC.write(termcolor.colored(i,hydrophobe))
    		elif k in Spe :
    			termcolor.cprint(k,spe,end='')
    			sC.write(termcolor.colored(i,spe))
    		elif k in Polaire :
    			termcolor.cprint(k,polaire,end='')
    			sC.write(termcolor.colored(i,polaire))
    		else :
    			print(k,end='')
    			sC.write(termcolor.colored(i,'green'))
sC.close()
s.close()
