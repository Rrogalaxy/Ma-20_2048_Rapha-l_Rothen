#Entête

from tkinter import *

#Variables, +listes

#table of the full game
game=[[2,4,8,16],
      [32,64,128,256],
      [512,1024,2048,4096],
      [8192,0,0,0]]

#game=[]

#the table of the tiles
labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

#colors

colors={2:'#FFADAD',4:'#f5b494',8:'#dfbe86',16:'#c3c786',32:'#a3cf94',64:'#85d4ae',
        128:'#6ed5cc',256:'#6cd3e7',512:'#84cdfb',1024:'#a9c4ff',2048:'#cebafa',
        4096:'#ebb1e6',8192:'#fcacca',0:'#ebb1e6',}


ox = 50
oy = 150

dx = 150
dy = 150

#Fonctions

def display():
    quit()


# Programme principal
window = Tk()
window.geometry("800x800")
window.resizable(0,0)


for line in range(4):
    for col in range(4):
        labels[line][col] = Label(window, text=game[line][col], font=("Arial", 20),width=6, height=3,bg = colors[game[line][col]])
        labels[line][col].place (x=ox + col*dx, y=oy + line*dy)





mainloop()