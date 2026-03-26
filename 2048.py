#jeu du 2048
#auteur : Raphaël Rothen

#les importation
import random
import tkinter as tk
from random import randint
from tkinter import *
import packing as packing
import tkinter.messagebox




#Variables, +listes

#si le jeu à gagné une fois ou pas
won = 0



#un jeu contenant chaque cases
#game=[[2,4,8,16],
#      [32,64,128,256],
#      [512,1024,2048,4096],
#      [8192,0,0,0]]

#le jeu dans toute sa splendeur
game=[[0,0,0,0],
      [0,2,0,0],
      [0,0,2,0],
      [0,0,0,0],]

#la table des cases
labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

#les differentes couleurs des blocs
colors={2:'#ffadad',4:'#f5b494',8:'#dfbe86',16:'#c3c786',32:'#a3cf94',64:'#85d4ae',
        128:'#6ed5cc',256:'#6cd3e7',512:'#84cdfb',1024:'#a9c4ff',2048:'#cebafa',
        4096:'#ebb1e6',8192:'#fcacca',0:'#303030',}

#les positions pour le placement de cases
ox = 450
oy = 100

dx = 150
dy = 150



#Fonctions

#cette fonction permet de créer des nouveau blocks dans des cases vides
def block_spawn():
    found = 0
    while not found:
        #check les cases de manière aléatoire
        line = randint(0,3)
        col = randint(0,3)
        #lorse qu'une case vide est trouvée, fait apparaitre un bloce (80% d'être un 2 et 20% d'être un 4)
        if game[line][col] == 0:
            found = 1
    game[line][col] = random.choice([2,2,2,2,4])




#cette fonction vérifie l'état du jeu si il y a un 2048
def check_win():
    global won
    #check chaque case à la recherche d'un 2048
    for line in range(4):
        for col in range(4):
            #si celui-ci existe, un message apparaît et un flag s'active pour ne plus le remettre
            if game[line][col] == 2048 and won == 0:
                won = 1
                tk.messagebox.showinfo(message="You won!", title="congratulations")


#cette fonction vérifie si le jeu est plein
def check_full_board():
    #verifie toute les cases à la recherche d'un 0, si il y en a pas, retourne false
    for line in range(4):
        for col in range(4):
            if game[line][col] == 0:
                return False
    return True

#cette fonction vérifie si il y a des jumeaux au niveau des ligne
def check_line_twin():
    twin_line = 0
    # verifie si chaque case et son voisin de dessous
    for line in range(3):
        for col in range(4):
            if game[line][col] == game[line+1][col]:
                twin_line += 1
                # retourne le nombre de jumeaux
    return twin_line

#cette fonction vérifie si il y a des jumeaux au niveau des colonnes
def check_col_twin():
    twin_col = 0
    #verifie si chaque case et son voisin de dessous
    for line in range(4):
        for col in range(3):
            if game[line][col] == game[line][col+1]:
                twin_col += 1
                #retourne le nombre de jumeaux
    return twin_col

#cette fonction vérifie si il y a des jumeaux
def check_twin():
    #si le nombre de jumeaux vertical ou horizontal est supérieur à 1 retourne True, sinon False
    if check_col_twin() > 0 or check_line_twin() > 0:
        return True
    return False

#cette fonction vérifie si le jeu peut countinuer ou pas
def check_fail():
    # si il y a pas de jumeaux et pas de place dans le tableau c'est game over
    if check_twin() == False and check_full_board() == True:
        tk.messagebox.showinfo(message="Game Over", title="you lost")



#cette fonction ci-dessous check quand on appuie sur les diférentes touches qui altèrent le jeux
def keypressed(event) :
    touche=event.keysym
    if (touche=="Down" or touche=="s" or touche=="S"):
        down()
    if (touche=="Up" or touche=="w" or touche=="W"):
        up()
    if (touche=="Left" or touche=="a" or touche=="A"):
        left()
    if (touche=="Right" or touche=="d" or touche=="D"):
        right()
    if (touche=="enter" and cheats.get() != None or touche=="ENTER" and cheats.get() == None):
        cheat()

#envoie les valeur du tableau à la fonction pack4 qui permettra de décaler et fusionner les nombre vers le bas
#récupère également si il y a eu des mouvements
def down():
    tot_move=0
    #change les valeurs des colonnes en les pack4 vers le bas
    for col in range(4):
        (game[3][col], game[2][col], game[1][col], game[0][col],move) = packing.pack4(game[3][col], game[2][col],
                                                                                 game[1][col], game[0][col])
        #si il y a eu du mouvement, fais apparaître un bloc
        tot_move += move
    if tot_move != 0:
        block_spawn()

    display_grid()
    check_win()
    check_fail()


#envoie les valeur du tableau à la fonction pack4 qui permettra de décaler et fusionner les nombre vers le haut
def up():
    tot_move=0
    #change les valeurs des colonnes en les pack4 vers le haut
    for col in range(4):

        (game[0][col], game[1][col], game[2][col], game[3][col],move) = packing.pack4(game[0][col], game[1][col],
                                                                                 game[2][col], game[3][col])
        #si il y a eu du mouvement, fais apparaître un bloc
        tot_move += move
    if tot_move != 0:
        block_spawn()

    display_grid()
    check_win()
    check_fail()


#envoie les valeur du tableau à la fonction pack4 qui permettra de décaler et fusionner les nombre vers la gauche
def left():
    tot_move=0
    #change les valeurs des lignes en les pack4 vers la gauche
    for line in range(4):
        (game[line][0], game[line][1], game[line][2], game[line][3],move) = packing.pack4(game[line][0], game[line][1],
                                                                                 game[line][2], game[line][3])
        #si il y a eu du mouvement, fais apparaître un bloc
        tot_move += move
    if tot_move != 0:
        block_spawn()

    display_grid()
    check_win()
    check_fail()


#envoie les valeur du tableau à la fonction pack4 qui permettra de décaler et fusionner les nombre vers la droite
def right():
    tot_move=0
    #change les valeurs des lignes en les pack4 vers la droite
    for line in range(4):
        (game[line][3], game[line][2], game[line][1], game[line][0],move) = packing.pack4(game[line][3], game[line][2],
                                                                                 game[line][1], game[line][0])
        #si il y a eu du mouvement, fais apparaître un bloc
        tot_move += move
    if tot_move != 0:
        block_spawn()

    display_grid()
    check_win()
    check_fail()


def display_grid():
    #mettre l'affichage à jour en fonction de la grille
    for line in range(4):
        for col in range(4):
            value = game[line][col] #on prends la valeur de la tuile
            font_color = "#303030" if 0 < value < 4000 else "#303030"
            labels[line][col].configure(text=value,bg=colors[value],fg=font_color)


#fonction des cheat codes et easter eggs

def cheat():
    print("yippi")

# Programme principal
window = Tk()
window.geometry("1200x750")
window.resizable(0,0)
window.configure(background='#303030')
window.title("2048")

#les labels
sep = tk.Label(bg='#000000')
sep.config(width=1,height=750)
sep.place(x=300, y=0)

back = tk.Label(bg='#000000', height=43, width=93)
back.place(x=400, y=50)

code = tk.Label(bg='#303030', text="Codes", font=('arial', 20, 'bold'))
code.place(x=75, y=110)

#les bouttons
quit = tk.Button(window,bg='#303030',text='Quit',fg='#ffffff',command=quit,font=('arial',20,'bold'),height=1,width=10)
quit.place(x=75, y=250)

Retry = tk.Button(window,bg='#303030',text='Restart',fg='#ffffff',font=('arial',20,'bold'),height=1,width=10)
Retry.place(x=75, y=350)


#l'entry des cheat codes
cheats = tk.Entry(window,bg='#303030',fg='#ffffff',width=30)
cheats.place(x=75, y=150)

#création des blocs
for line in range(4):
    for col in range(4):
        labels[line][col] = Label(window, text=game[line][col], font=("Arial", 20),width=6, height=3,bg = colors[game[line][col]])
        labels[line][col].place (x=ox + col*dx, y=oy + line*dy)


#les petits details comme le binding du clavier et le refresh du jeu
window.bind('<Key>',keypressed)
display_grid()
mainloop()