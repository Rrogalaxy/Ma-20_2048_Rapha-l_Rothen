#jeu du 2048
#auteur : Raphaël Rothen


import tkinter as tk
from tkinter import *
from tkinter import ttk


#Variables, +listes

#table of the full game
game=[[2,4,8,16],
      [32,64,128,256],
      [512,1024,2048,4096],
      [8192,0,0,0]]

#game=[[None,None,None,None],
#      [None,None,None,None],
#      [None,None,None,None],
#      [None,None,None,None],]

#the table of the tiles
labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

#colors

colors={2:'#ffadad',4:'#f5b494',8:'#dfbe86',16:'#c3c786',32:'#a3cf94',64:'#85d4ae',
        128:'#6ed5cc',256:'#6cd3e7',512:'#84cdfb',1024:'#a9c4ff',2048:'#cebafa',
        4096:'#ebb1e6',8192:'#fcacca',0:'#303030',}


ox = 450
oy = 100

dx = 150
dy = 150

#Fonctions

def display_grid():
    #mettre l'affichage à jour en fonction de la grille
    for row in range(4):
        for col in range(4):
            value = game[line][col] #on prends la valeur de la tuile
            font_color = "#303030" if 0 < value < 4000 else "#000000"
            labels[line][col].configure(text=value,bg=colors[value],fg=font_color)
            #POURQOI LES 0 NNE CHANGENT PAS DE COULEUR ???

# Programme principal
window = Tk()
window.geometry("1200x750")
window.resizable(0,0)
window.configure(background='#303030')
window.title("2048")

sep = tk.Label(bg='#000000')
sep.config(width=1,height=750)
sep.place(x=300, y=0)

back = tk.Label(bg='#000000', height=43, width=93)
back.place(x=400, y=50)

quit = tk.Button(window,bg='#303030',text='Quit',fg='#ffffff',command=quit,font=('arial',20,'bold'),height=1,width=10)
quit.place(x=75, y=250)

Retry = tk.Button(window,bg='#303030',text='Restart',fg='#ffffff',font=('arial',20,'bold'),height=1,width=10)
Retry.place(x=75, y=350)


#création des blocs
for line in range(4):
    for col in range(4):
        labels[line][col] = Label(window, text=game[line][col], font=("Arial", 20),width=6, height=3,bg = colors[game[line][col]])
        labels[line][col].place (x=ox + col*dx, y=oy + line*dy)




display_grid()
mainloop()