import numpy as np
import math
import copy

bellman=np.loadtxt("dijkstra.txt",dtype=float)

file=open("dijkstra.txt")
ligne=file.readline()
file.close()
nom=ligne.split()

cheminMin = [math.inf] * 6

def testSommet(depart, arrive):
    global cheminMin
    return cheminMin




print(testSommet(1,6))










#global cheminMin
#    global bellman
#    for i in range(depart -1, arrive -1):
#        for j in range(len(bellman)):
#            print(bellman[j][i], cheminMin[i])
#            if(bellman[j][i] < cheminMin[i] and bellman[j][i] != -1):
#                cheminMin[i] = bellman[j][i]
#    return cheminMin