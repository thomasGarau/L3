import math

prix = [0,2,5,7,9,10,12,14,15]
meilleurPrix = [0]*len(prix)
solution = [0]*len(prix)
for i in range(0, len(prix)):
    print(i, len(prix))
    meilleurPrix[i] = -math.inf
    for j in range(0, i):
        if  meilleurPrix[i] <= prix[j] + meilleurPrix[i-j]:
            meilleurPrix[i] = prix[j] + meilleurPrix[i-j]
            solution[i]= j
print(solution, "\n" ,meilleurPrix)