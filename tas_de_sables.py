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
centrageLargeur = espacementLargeur / 2
centrageHauteur = espacementHauteur / 2
taillePixelLargeur = WIDTH / N / N * 1.5
taillePixelHauteur = HEIGHT / N / N * 1.5

liste_couleurs = []

#########################################################
#Fonctions :

def configuration_courante() :
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
            canvas.create_rectangle(espacementLargeur * i + centrageLargeur, espacementHauteur * j + centrageHauteur, \
                espacementLargeur * i + centrageLargeur + taillePixelLargeur, espacementHauteur * j + centrageHauteur + taillePixelHauteur, fill=couleur)
    print(grille)
#création de la grille

#########################################################
#Widgets :
racine = tk.Tk()
racine.title("tas de sable")
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg='black')
bouton_01 = tk.Button(racine, text="configuration aléatoire", command=configuration_courante)

#canvas.create_text((250,250), text="salut", font=("helvetica", 50))

#########################################################
#Emplacements des widgets :
canvas.grid()
bouton_01.grid(row=1)


#########################################################
#le reste quoi :

racine.mainloop()