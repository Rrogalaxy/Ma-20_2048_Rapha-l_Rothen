#fonction de pack pour le 2048
#auteur : Raphaël rothen


#cette fonction permet de décaler tout les nombre le plus à gauche possible
#si 2 mêmes nombres se touchent après le décalage, ceux-ci fusionnent ensemble

def pack4 (a,b,c,d):
    #cette valeur permet de compter le nombre de mouvement, elle est réinitialisée au début de la fonction
    move = 0

    #cette partie sert à décaler tout les nombre le plus à gauche
    if c == 0 and d != 0:
        c,d = d,0
        move += 1
    if b == 0 and c != 0 :
        b,c,d = c,d,0
        move += 1
    if a == 0 and b != 0 :
        a,b,c,d = b,c,d,0
        move += 1

    #celle-ci sert à la fusion des nombres si les 2 mêmes se rencontrent
    if a == b and a != 0 :
        a,b,c,d = a*2,c,d,0
        move += 1

    if b == c and b != 0 :
        b,c,d = b*2,d,0
        move += 1

    if c == d and c != 0 :
        c,d = c*2,0
        move += 1

    return (a,b,c,d,move)

#print(pack4(0,0,0,2))
#print(pack4(0,0,2,2))
#print(pack4(2,0,2,2))
#print(pack4(2,2,2,2))
#print(pack4(2,2,4,0))

################################################