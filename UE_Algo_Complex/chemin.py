import numpy as np
import math

tab=np.loadtxt('chemin.txt')
fp = open('chemin.txt','r')
line = fp.readline()
sommets = line[1:].split()
fp.close()


pcc = []
nkm_min= math.inf
depart = 0
arrivee = 5
chemin=[]
chemin.append(depart)
nkm= 0

def acceptable(chemin, nkm, e, ei):
    global pcc, nkm_min, tab
    if e in chemin or tab[ei, e] == 0 or (nkm + tab[ei,e]) > nkm_min: 
        return False
    else : return True

def chemin_plus_court(chemin, nkm, ei):
    global pcc,nkm_min,tab,arrivee
    if ei == arrivee:
        if nkm< nkm_min : 
            nkm_min = nkm
            pcc = chemin.copy()
            return 
    for e in range(len(tab)):
        if acceptable(chemin, nkm, e, ei):
            chemin.append(e)
            nkm += tab[ei, e]
            chemin_plus_court(chemin, nkm, e)
            del chemin[-1]
            nkm -= tab[ei, e]

chemin_plus_court(chemin, nkm, 0)
print(pcc)
