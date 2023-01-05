import numpy as np
objets = np.loadtxt('Sac_a_dos.txt', dtype=int)
W = 15
n = len(objets)
c = [0]*W
cnext = [0]*W

for i  in range(n):
    for w in range(W):
        if(w >= objets[i][2]):
            cnext[w] = max(c[w], c[w-objets[i][2]]+ objets[i][1])
        else:
            cnext[w] = c[w]

    c = cnext.copy()

print(c)
