import numpy as np
lab = np.loadtxt('labyrinthe.txt')
trouve = False

def acceptable(lab, x, y):
    return (x >= 0 and x < len(lab[0]) and y >=0 and y < len(lab[1]) and lab[x, y] != -1 and lab[x,y] != 1 ) 
        

def laby(lab, x, y):
    global trouve
    if x == len(lab[0]) -1 and y == len(lab[1]) -1:
        lab[-1, -1] = 1
        trouve = True
        return
    for e in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if acceptable(lab, e[0], e[1]):
            lab[e[0], e[1]]= 1
            laby(lab, e[0], e[1])
            if trouve:
                return lab
            lab[e[0], e[1]] = 0

print(laby(lab, 0, 0))