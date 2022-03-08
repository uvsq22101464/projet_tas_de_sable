#########################################################
# groupe BI 01
# Ethan MACHE
# Neven Martinet--Gauly
# Mathushan MURALY
# https://github.com/uvsq22101464/projet_tas_de_sable.git
#########################################################


#########################################################
#Import des librairies :
import tkinter as tk
import random


#########################################################
#Variables globales :
WIDTH, HEIGHT = 600, 600
N = 10
grille = []
espacementHauteur = HEIGHT / N
espacementLargeur = WIDTH / N
taillePixelLargeur = WIDTH / N
taillePixelHauteur = HEIGHT / N

liste_couleurs = []

#########################################################
#Fonctions :

def configuration_courante() :
    grille, liste_couleurs = [], []
    for i in range(N) :
        grille.append([])
        liste_couleurs.append([])
        for j in range(N):
            grille[i].append(random.randint(1,5))
            if grille[i][j] == 1 :    
                liste_couleurs[i].append("blue")
            elif grille[i][j] == 2 :
                liste_couleurs[i].append("yellow")
            elif grille[i][j] == 3 :
                liste_couleurs[i].append("green")
            else :
                liste_couleurs[i].append("red")
            couleur = liste_couleurs[i][j]
            canvas.create_rectangle(espacementLargeur * i, espacementHauteur * j, \
                espacementLargeur * i + taillePixelLargeur, espacementHauteur * j + taillePixelHauteur, fill=couleur)
    print(grille)

def config_vide() :
    grille, liste_couleurs = [], []
    for i in range(N) :
        grille.append([])
        liste_couleurs.append([])
        for j in range(N):
            grille[i].append(0)
            liste_couleurs[i].append("white")
            couleur = liste_couleurs[i][j]
            canvas.create_rectangle(espacementLargeur * i, espacementHauteur * j, \
                espacementLargeur * i + taillePixelLargeur, espacementHauteur * j + taillePixelHauteur, fill=couleur)
    print(grille)

#def calcul() :


#########################################################
#Widgets :
racine = tk.Tk()
racine.title("tas de sable")
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg='black')
bouton_01 = tk.Button(racine, text="configuration aléatoire", command=configuration_courante)
bouton_02 = tk.Button(racine, text="config vide", command=config_vide)
bouton_03 = tk.Button(racine, text="ajouter 0 à 3 grains de sable")

#canvas.create_text((250,250), text="salut", font=("helvetica", 50))

#########################################################
#Emplacements des widgets :
canvas.grid(row=0, column=0, columnspan=3)
bouton_01.grid(row=1, column=0)
bouton_02.grid(row=1, column=1)
bouton_03.grid(row=1, column=2)

#########################################################
#le reste quoi :

racine.mainloop()