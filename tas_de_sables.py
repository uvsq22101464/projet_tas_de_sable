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


#########################################################
#Fonctions :
def configuration_courante() :
    pass


#########################################################
#Widgets :
racine = tk.Tk()
racine.title("tas de sable")
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg='white')
bouton_01 = tk.Button(racine, text="configuration aléatoire")

canvas.create_text((250,250), text="salut", )

#########################################################
#Emplacements des widgets :
canvas.grid()
bouton_01.grid(row=1)


#########################################################
#le reste quoi :
racine.mainloop()