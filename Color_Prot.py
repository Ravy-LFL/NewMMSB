#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import webbrowser
                        #Creation et ouverture des fichiers
if len(sys.argv) != 2 :
	sys.exit("VEUILLEZ SAISIR LE PATH DE LA SEQUENCE A COLORIER A LA SUITE DE LA COMMANDE DE LANCEMENT DU RPOGRAMME")
else :
	sequence = sys.argv[1]
s=open(sequence,"r")
nouveau_nom=sequence.split('/')
new_name=nouveau_nom[len(nouveau_nom)-1].split('.')
nuevo_nombre=new_name[0]
sC=open(nuevo_nombre+".html","w")
compteur=1


                        #Création des différentes listes et des différents dictionnaire
Basique=['K','R']
Acide=['E','D']
Hydrophobes=['A','I','L','M','F','V','G','P']
Spe=['W','H',]
Cys=['C']
Polaire=['N','Q','S','T','Y']
aa=['A','R','D','N','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
couleur={'red':'E61212','blue':'122FE6','grey':'555658','green':'00CB09','yellow':'E0EC1A','orange':'EC961A','pink':'DF1AEC','purple':'9C3CA2','brown':'A26D3C','grey_clear':'9BA9AB','cyan':'0CF3F0'}

'''
lysine,arginine = acides aminés basique
acide glutamique et acide aspartique = acides aminés acides
alanine, isoleucine, leucine, méthionine, phénylalanine, valine, tyrosine, cystéine = acide aminé hydrophobes
tryptophane et hystidine
asparagine,glutamine,glycine,proline,serine,thréonine= acide aminés polaire
'''
print("voici le code couleur par défaut : gris = acides aminés hydrophobe","\n","rouge = acide ", "\n", " bleu = basique","\n","jaune = tryptophane et hystidine","\n","vert = Polaire","\n","marron = indice des isoleucines","\n","orange = indice des leucines")
change_col=input("si vous voulez modifier ces couleurs appuyez sur y sinon appuyez sur n ( surtout ne pas taper la lettre 'o' ! ): ")

                    #Interface utilisateur pour saisir des nouvelles couleurs ou non
if change_col == 'n' :
    hydrophobe=couleur['grey_clear']
    acide=couleur['red']
    basique=couleur['blue']
    spe=couleur['cyan']
    polaire=couleur['green']
    leucine=couleur['pink']
    isoleucine=couleur['pink']
    cysteine=couleur['yellow']
if change_col == 'y' :
    HYDROPHOBE=input("saisissez le nom de la couleur associer aux acides aminés hydrophobes : ")
    ACIDE=input("saisissez le nom de la couleur associer aux acides aminés acide : ")
    BASIQUE=input("saisissez le nom de la couleur associer aux acides aminés basique : ")
    SPE=input("saisissez le nom de la couleur associer aux tryptophane et à l'hystidine : ")
    POLAIRE=input("saisissez le nom de la couleur associer aux acides aminés polaire : ")
    LEUCINE=input("saisissez le nom de la couleur associer aux leucines : ")
    ISOLEUCINE=input("saisissez le nom de la couleur associer aux isoleucines : ")
    CYSTEINE=input("saisissez le nom de la couleur associer aux cysteine :")
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

def recupere_zipper(seq_aa,aa_choisis):
	a=0
	list_a_renvoyer=[]
	while a!=len(seq_aa)-5:
		list_possible_zipper=[] #On va couper la chaine de caractere et si il s'avere que c'est un zipper alors on la rangera dans chaine a renvoyer, puis si la chaine qui la suis s'avere suivre le meme pattern alors on concatenera les deux chaines, et si la chaine qui suis la precedente ne suis pas le meme pattern on rangera alors notre chaine dans la liste à retourner
		chaine_intermediaire=""
		chaine_a_renvoyer=""
		for i in range(a,a+6):
			chaine_intermediaire+=seq_aa[i]
		if chaine_intermediaire[0]==aa_choisis:
			if chaine_intermediaire[1] in aa and chaine_intermediaire[2] in aa:
				if chaine_intermediaire[3]==aa_choisis:
					if chaine_intermediaire[1] in aa and chaine_intermediaire[2] in aa and chaine_intermediaire[3] :
						chaine_a_renvoyer+=chaine_intermediaire
					else :
						list_a_renvoyer.append(chaine_a_renvoyer)
				else :
					list_a_renvoyer.append(chaine_a_renvoyer)
			else :
				list_a_renvoyer.append(chaine_a_renvoyer)
		else:
			list_a_renvoyer.append(chaine_a_renvoyer)
		a+=1
	return(list_a_renvoyer)

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
		else :
			print('0')
		a+=1
	return(list_a_renvoyer)

def domaine_html(domain_list,sC) :
	sC.write("<table> \n")
	sC.write("<tr> \n")
	sC.write("<th> Hypothetic Transmembrane Domain </th> \n")
	sC.write("</tr> \n")
	for i in domain_list :
		sC.write("\t <tr>")
		sC.write("\t \t <td>")
		domaine=("\t"+"\t"+i)
		sC.write(domaine)
		sC.write("\t \t </td> \n")
		sC.write("\t </tr> \n")
	sC.write("</table> \n \n")

def print_aa(list_line,saut_de_ligne):
	#if saut_de_ligne==100 :
	#	sC.write("<br>")
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
		if saut_de_ligne==nb_aa_sur_ligne:
			sC.write("<br>")
			saut_de_ligne=1
	return(saut_de_ligne)

#main
ligne=s.readlines()
mep_tab(sC)
createur_debut_html(sC)
couleur_background(sC)
saut_de_ligne=1
for i in range(1,len(ligne)) :	#On commence a 1 car la premiere ligne du fichier est le nom du fichier fasta, donc ne nous interesse pas
	list_line=list(ligne[i])
	sdl=print_aa(list_line,saut_de_ligne)
	saut_de_ligne=sdl
#main 2 : transmembrane domains
sC.write("<br>")
domain_list=(recupere_domaine(creer_seq(ligne)))
domaine_html(domain_list,sC)

#main 3 zipper leucine
print(recupere_zipper(creer_seq(ligne),aa_choisis))



















sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("<br>")
sC.write("Legende : ")
sC.write("<br>")
col_hydrophobe="<FONT COLOR="+hydrophobe+"> acides amines hydrophobes </FONT>"
sC.write(col_hydrophobe)
sC.write('<br>')
col_acide="<FONT COLOR="+acide+"> acides amines acide </FONT>"
sC.write(col_acide)
sC.write("<br>")
col_basique="<FONT COLOR="+basique+"> acides amines basique </FONT>"
sC.write(col_basique)
sC.write("<br>")
col_spe="<FONT COLOR="+spe+"> acides amines trypthophane et hystidines </FONT>"
sC.write(col_spe)
sC.write("<br>")
col_polaire="<FONT COLOR="+polaire+"> acides amines polaire </FONT>"
sC.write(col_polaire)
sC.write("<br>")
col_leucine="<FONT COLOR="+leucine+"> indices leucines </FONT>"
sC.write(col_leucine)
sC.write("<br>")
col_isoleucine="<FONT COLOR="+isoleucine+"> indices isoleucines </FONT>"
sC.write(col_isoleucine)
sC.write("<br>")
createur_fin_html(sC)
sC.close()
s.close()
