import matplotlib.pyplot as plt
import numpy as np
import math 
import random as rd

tab = np.loadtxt("ReseauDyxtra.txt")
precedent = [None]*len(tab)
poids = [math.inf]*len(tab)
etat = ['blanc']*len(tab)

poids[0] =0; etat[0] = 'Gris'

def suivant():
    val = math.inf
    sui = math.inf
    for s in range(len(tab)):
        if etat[s] == 'Gris':
            if poids[s]<val:
                sui = s
                val = poids[s]
    return sui

def etape(s):
    s = suivant()
    for x in range(len(tab)):
        if (tab[s,x] >0) and (etat[x] != 'Noir'):
            val = tab[s,x]+ poids[s]
            if val<poids[x]:
                poids[x]=val
                etat[x]='Gris'
                precedent[x]=s
    etat[s] = 'Noir'

def dijsktra():
    s = suivant()
    while(s != math.inf):
        etape(s)
        s = suivant
    print(etat,"\n", poids,"\n", precedent)

dijsktra()


