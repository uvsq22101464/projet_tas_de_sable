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
WIDTH, HEIGHT = 500, 500
N = 3
grille = []

#########################################################
#Fonctions :
def configuration_courante() :
    for i in range(N) :
        grille.append([])
        for j in range(N):
            grille[i].append(random.randint(0,10))
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