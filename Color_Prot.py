#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import termcolor
import webbrowser
                        #Creation and opening of files
if len(sys.argv) != 2 :
	sys.exit("PLEASE ENTER THE PATH OF THE SEQUENCE TO BE COLORED FOLLOWING THE COMMAND TO LAUNCH THE PROGRAM")
else :
	sequence = sys.argv[1]
s=open(sequence,"r")
nouveau_nom=sequence.split('/')
new_name=nouveau_nom[len(nouveau_nom)-1].split('.')
nuevo_nombre=new_name[0]
sC=open(nuevo_nombre+".html","w")
compteur=1

                        #Creation of different lists and dictionaries
Basique=['K','R']
Acide=['E','D']
Hydrophobes=['A','I','L','M','F','V','G','P']
Spe=['W','H',]
Cys=['C']
Polaire=['N','Q','S','T','Y']
aa=['A','R','D','N','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
#IF YOU WANNA ADD A COLOR, JUST ADD IT TO THE DICTIONARY BELOW WITH HIS HEXADECIMAL CODE
couleur={'red':'E61212','blue':'122FE6','grey':'555658','green':'00CB09','yellow':'E0EC1A','orange':'EC961A','pink':'DF1AEC','purple':'9C3CA2','brown':'A26D3C','grey_clear':'9BA9AB','light_blue':'0CF3F0'}

'''
lysine,arginine = acides aminés basique
acide glutamique et acide aspartique = acides aminés acides
alanine, isoleucine, leucine, méthionine, phénylalanine, valine, tyrosine, cystéine = acide aminé hydrophobes
tryptophane et hystidine
asparagine,glutamine,glycine,proline,serine,thréonine= acide aminés polaire
'''
print("here is the default color code : grey = hydrophobic amino acids","\n","red = acid ", "\n", "blue = basic","\n","light_blue = tryptophan and hystidine","\n","gren = Polar","\n","pink = isoleucine index","\n","pink = leucine index","\n", "yellow = cystein")
change_col=input("if you want to change these colors press y otherwise press n (do not type the letter 'o'!): ")

                    #User interface to enter new colors or not
if change_col == 'n' :
    hydrophobe=couleur['grey_clear']
    acide=couleur['red']
    basique=couleur['blue']
    spe=couleur['light_blue']
    polaire=couleur['green']
    leucine=couleur['pink']
    isoleucine=couleur['pink']
    cysteine=couleur['yellow']
if change_col == 'y' :
	print("you choose to change the colors, here the possibilities, if you want to add a color , fund the dictionnary in the script at the line 26 :")
	for i in couleur.keys() :
		print(i, end="\t")
	HYDROPHOBE=input("enter the name of the color associated with hydrophobic amino acids : ")
	ACIDE=input("enter the name of the color associated with the acidic amino acids : ")
	BASIQUE=input("enter the name of the color associated with basic amino acids : ")
	SPE=input("enter the name of the color associated with tryptophan and hystidine : ")
	POLAIRE=input("enter the name of the color associated with polar amino acids : ")
	LEUCINE=input("enter the name of the color associated with leucines : ")
	ISOLEUCINE=input("enter the name of the color associated with isoleucines : ")
	CYSTEINE=input("enter the name of the color associated with cysteine :")
	cysteine=couleur[CYSTEINE]
	hydrophobe=couleur[HYDROPHOBE]
	acide=couleur[ACIDE]
	basique=couleur[BASIQUE]
	spe=couleur[SPE]
	polaire=couleur[POLAIRE]
	leucine=couleur[LEUCINE]
	isoleucine=couleur[ISOLEUCINE]
if change_col=='o':
    webbrowser.open("https://www.youtube.com/watch?v=Lrj2Hq7xqQ8")

nb_aa_sur_Ligne=input("type the number of aa you want on a line : ")
nb_aa_sur_ligne=int(nb_aa_sur_Ligne)
aa_choisis=input("type the aa of the zipper you're searching for : ")

def createur_debut_html(sC):
    sC.write("<HTML>")
    sC.write("\n")
    sC.write("\n")
    sC.write("<HEAD>")
    sC.write("\n")
    titre=("<TITLE>"+str(sequence)+"</TITLE>")
    sC.write("sequence : ")
    sC.write(str(sequence))
    sC.write("<br>")

def couleur_background(sC) :
	sC.write("<style> Iso { background-color:"+isoleucine+";  color: black; } </style>")
	sC.write("<style> Leu { background-color:"+leucine+";  color: black; } </style>")
	sC.write("<style> Hydro { background-color:"+hydrophobe+";  color: black; } </style>")
	sC.write("<style> Aci { background-color:"+acide+";  color: black; } </style>")
	sC.write("<style> Bas { background-color:"+basique+";  color: black; } </style>")
	sC.write("<style> SPe { background-color:"+spe+";  color: black; } </style>")
	sC.write("<style> POlaire { background-color:"+polaire+";  color: black; } </style>")
	sC.write("<style> CYsteine { background-color:"+cysteine+";  color: black; } </style>")

def mep_tab(sC) :
	sC.write("<style> table { border-collapse: collapse; } </style>")
	sC.write("<style> td { border: 1px solid black; } </style>")


def createur_fin_html(sC):
    sC.write("</HEAD>")
    sC.write("/HTML")

'''
def print_compteur(list_line,compteur):
    for i in range(0,(len(list_line))):
        if list_line[i]=='L' :
            termenb="<FONT COLOR="+LeuIso['leucine']+">"+str(compteur)+"&ensp;"+"</FONT>"
            sC.write(termenb)
        elif list_line[i]=='I' :
            termenb="<FONT COLOR="+LeuIso['isoleucine']+">"+str(compteur)+"&ensp;"+"</FONT>"
            sC.write(termenb)
        else :
            termenb="&ensp;&ensp;"
            sC.write(termenb)
        compteur+=1
'''

def creer_seq(ligne):
	seq_aa=""
	for i in ligne :
		b=i.split("\n")
		c=b[0]
		d=list(c)
		for j in d :
			seq_aa+=j
	return(seq_aa)


def recupere_zipper_beta(seq_aa,aa_choisis):									#trouver une solution pour que l'utilisateur puisse choisir de quel longueur il veut ses zipper//Nan bah ducoup quand il en vois un qui est grand il le prend donc c'est bon
	a=0
	list_a_renvoyer=[]
	chaine_test=""
	chaine_a_renvoyer=""
	derniere_chaine=""
	while a<=len(seq_aa)-8:
		for i in range(a,a+7):
			chaine_test+=seq_aa[i]
		if chaine_test[0]==aa_choisis and chaine_test[3]==aa_choisis:
			chaine_a_renvoyer+=chaine_test
			chaine_test=""
			a+=7
		else:
			list_a_renvoyer.append(chaine_a_renvoyer)
			chaine_a_renvoyer=""
			chaine_test=""
			a+=1
	for i in range(len(seq_aa)-7,len(seq_aa)):
		derniere_chaine+=seq_aa[i]
	if derniere_chaine[0]==aa_choisis and derniere_chaine[3]==aa_choisis:
		list_a_renvoyer.append(derniere_chaine)
	return(list_a_renvoyer)
'''
def recupere_domaine(seq_aa):
	a=0
	list_a_renvoyer=[]
	while a!=len(seq_aa)-21:
		list_possible_domaine=[]
		compteur_hydrophobe=0
		compteur_autres=0
		chaine_a_renvoyer=""
		for i in range(a,a+20):
			list_possible_domaine.append(seq_aa[i])
		for j in list_possible_domaine:
			if j in Hydrophobes :
				compteur_hydrophobe+=1
			else :
				compteur_autres+=1
		if compteur_hydrophobe>compteur_autres:
			for k in list_possible_domaine :
						chaine_a_renvoyer+=k
			list_a_renvoyer.append(chaine_a_renvoyer)
		a+=1
	return(list_a_renvoyer)
'''

def recupere_domaine(seq_aa):
	a=0
	list_a_renvoyer=[]
	while a!=len(seq_aa)-22:
		etat = False
		list_possible_domaine=[]
		compteur_hydrophobe=0
		compteur_autres=0
		chaine_a_renvoyer=""
		for i in range(a,a+22):
			list_possible_domaine.append(seq_aa[i])
		for j in list_possible_domaine:
			if j in Hydrophobes :
				compteur_hydrophobe+=1
			else :
				compteur_autres+=1
		if list_possible_domaine[0] in Polaire or list_possible_domaine[len(list_possible_domaine)-1] in Polaire or list_possible_domaine[0] in Polaire and list_possible_domaine[len(list_possible_domaine)-1] in Polaire :
			etat=True
		if compteur_hydrophobe>compteur_autres and etat==True :
			for k in range(1,len(list_possible_domaine)-2) :
						chaine_a_renvoyer+=list_possible_domaine[k]
			list_a_renvoyer.append(chaine_a_renvoyer)
		a+=1
	return(list_a_renvoyer)

def domaine_html(domain_list,sC) :
	print("second step..")
	sC.write("<table> \n")
	sC.write("<tr> \n")
	sC.write("<th> Hypothetic Transmembrane Domain </th> \n")
	sC.write("</tr> \n")
	for i in domain_list :
		sC.write("\t <tr>")
		sC.write("\t \t <td>")
		domaine=("\t"+"\t"+i)
		sC.write(domaine)
		sC.write("*")
		sC.write("\t \t </td> \n")
		sC.write("\t </tr> \n")
	sC.write("</table> \n \n")

def zipper_html(liste_a_zipper,sC):
	print("last step..")
	sC.write("<br>")
	sC.write("<table> \n")
	sC.write("<tr> \n")
	sC.write("<th> Hypothetic Zipper Domain </th> \n")
	sC.write("</tr> \n")
	for i in liste_a_zipper :
		if i!="":
			sC.write("\t <tr>")
			sC.write("\t \t <td>")
			domaine=("\t"+"\t"+i)
			sC.write(domaine)
			sC.write("\t \t </td> \n")
			sC.write("\t </tr> \n")
	sC.write("</table> \n \n")



def print_aa(list_line,saut_de_ligne):
	for k in range(0,len(list_line)-1) :
		if list_line[k] in Basique :
			terme="<Bas> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</Bas>"
			sC.write(terme)
		elif list_line[k] in Acide :
			terme="<Aci> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</Aci>"
			sC.write(terme)
		elif list_line[k] in Hydrophobes and list_line[k]=='L':
			terme="<Leu> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</Leu>"
			sC.write(terme)
		elif list_line[k] in Hydrophobes and list_line[k] == 'I':
			terme="<Iso> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</Iso>"
			sC.write(terme)
		elif list_line[k] in Hydrophobes and list_line[k]!='L' and  list_line[k]!='I':
			terme="<Hydro> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</Hydro>"
			sC.write(terme)
		elif list_line[k] in Spe :
			terme="<SPe> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</SPe>"
			sC.write(terme)
		elif list_line[k] in Polaire :
			terme="<POlaire> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</POlaire>"
			sC.write(terme)
		elif list_line[k] in Cys :
			terme="<CYsteine> <FONT SIZE=3pt face=Courier>"+list_line[k]+"</CYsteine>"
			sC.write(terme)
		elif list_line[k] == "\t" or list_line[k]=="\n" :
			sC.write("")
		else :
			terme="<FONT SIZE=2pt face=Times New Roman>"+list_line[k]+"</FONT>"
			sC.write(terme)
		saut_de_ligne+=1
		if saut_de_ligne==nb_aa_sur_ligne+1:
			sC.write("<br>")
			saut_de_ligne=1
	return(saut_de_ligne)

#main
print("first step...")
ligne=s.readlines()
mep_tab(sC)
createur_debut_html(sC)
couleur_background(sC)
saut_de_ligne=1
for i in range(1,len(ligne)) :	#We start at 1 because the first line of the file is the name of the fasta file, so we are not interested
	list_line=list(ligne[i])
	sdl=print_aa(list_line,saut_de_ligne)
	saut_de_ligne=sdl
nouvelle_ligne=ligne.copy()
new_line=[]
for i in nouvelle_ligne :
	new_element=i.split('\n')
	new_line.append(new_element[0])
del new_line[0]
#print("voici la nouvelle liste appeler new_line : ",end="\t")
#print(new_line)

#main 2 : transmembrane domains
sC.write("<br>")
domain_list=(recupere_domaine(creer_seq(new_line)))
domaine_html(domain_list,sC)
#print(creer_seq(new_line))

#Main 3 : zipper
liste_a_zipper=(recupere_zipper_beta(creer_seq(new_line),aa_choisis))
#print(liste_a_zipper)
zipper_html(liste_a_zipper,sC)

#printing of legends
print("printing legends..")
sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("Legends : ")
sC.write("<br>")
col_hydrophobe="<FONT COLOR="+hydrophobe+"> hydrophobic amino acids </FONT>"
sC.write(col_hydrophobe)
sC.write('<br>')
col_acide="<FONT COLOR="+acide+"> acid amino acids </FONT>"
sC.write(col_acide)
sC.write("<br>")
col_basique="<FONT COLOR="+basique+"> basics amino acids </FONT>"
sC.write(col_basique)
sC.write("<br>")
col_spe="<FONT COLOR="+spe+"> tryptophan and hystidine </FONT>"
sC.write(col_spe)
sC.write("<br>")
col_polaire="<FONT COLOR="+polaire+"> polar amino acids </FONT>"
sC.write(col_polaire)
sC.write("<br>")
col_leucine="<FONT COLOR="+leucine+"> index leucine </FONT>"
sC.write(col_leucine)
sC.write("<br>")
col_isoleucine="<FONT COLOR="+isoleucine+"> index isoleucine </FONT>"
sC.write(col_isoleucine)
sC.write("<br>")
createur_fin_html(sC)



term=input("now maybe the html folder is not complete you can print a terminal version with typing y, else type n : ")
if term == 'y' :
	#printing with termcolor
	print("sequence aligned : ")
	print(nb_aa_sur_ligne)
	b=0
	fin=""
	for i in new_line :
		for j in i :
			b+=1
			if b==nb_aa_sur_ligne:
				fin="\n"
				b=0
			else :
				fin=""
			if j in Hydrophobes :
				termcolor.cprint(j,'white','on_grey',end=fin)
			elif j in Hydrophobes and j=='L':
				termcolor.cprint(j,'white','on_pink',end=fin)
			elif j in Hydrophobes and j=='I' :
				termcolor.cprint(j,'white','on_pink',end=fin)
			elif j in Basique:
				termcolor.cprint(j,'white','on_blue',end=fin)
			elif j in Acide :
				termcolor.cprint(j,'white','on_red',end=fin)
			elif j in Spe :
				termcolor.cprint(j,'white','on_cyan',end=fin)
			elif j in Cys :
				termcolor.cprint(j,'white','on_yellow',end=fin)
			elif j in Polaire :
				termcolor.cprint(j,'white','on_green',end=fin)
	print("\n")
	print("list of hypothetical transmembrane domains : ","\n")
	print(domain_list)
	print("\n")
	print("list of hypothetical zipper : ","\n")
	print(liste_a_zipper)
else :
	print(" you will find you're folder .html at the same place than Color_prot.py")


sC.close()
s.close()
