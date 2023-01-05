tab = [459,124,321,True,False]

# les quatre premier bits détermine la taille de chaque int en bin les bits deux et trois sont les bool le reste c'est les int
def encodage(tab):
    retour = ""
    #détermine pour le plus grand nombre du tableau le nombre de bits nécessaire l'ajoute au debut du retour
    encodage = bin(len(bin(max(tab))[2:]))[2:]
    retour += encodage
    #ajoute les bool au retour
    for e in tab:
        if type(e) is bool:
            retour += bin(e)[2:]

    #ajoute ensuite les int au retour
    for e in tab:
        if type(e) is int:
            retour += format(e, '011b')[2:]

    return retour

def decodage(str):
    encodage = int(str[:4].encode(), 2)
    if encodage > 9:
        return 
    bool1 = bool(int(str[4:5].encode(), 2))
    bool2 = bool(int(str[5:6].encode(), 2))
    int1 = int(str[6:6+encodage].encode(), 2)
    int2 = int(str[6+encodage: 6 +  2 * encodage].encode(), 2)
    int3 = int(str[6+ 2*encodage: 6+ 3* encodage].encode(), 2)

    return [bool1,bool2,int1,int2,int3]

print(decodage(encodage(tab)))