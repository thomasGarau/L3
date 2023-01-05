import math

class Noeud:
    def _init_(self, G, D, num, val=math.inf):
        self.G = G
        self.D = D
        self.val = val
        self.num = num
    
    def isFeuille(self):
        if (self.G==None) and (self.D==None):
            return True
        return False

#valeur de l'exemple 
#on créer les feuilles (les noeuds au dernier niveau de profondeur)
valeurFeuille = [7,9,5,4,11,13,4,17,5,9,4,2,11,1,13,6]
def creer_arbre():
    num = 1
    arbre = []
    for val in valeurFeuille:
        arbre.append(Noeud._init_(None, None, val))
        num+=1
    #on créer des noeud de deux feuille et des noeuds de deux autres noeuds que l'on place dans l'arbre à la place des feuilles seule
    while len(arbre)>1:
        nb = len(arbre)
        for i in range(0, nb, 2):
            ndG = arbre.pop(0)
            #none pour éviter les errreur si les valeur ne sont pas un nombre pair
            ndD = None
            if (i+1)<nb:
                ndD = arbre.pop(0)
            arbre.append(Noeud(ndG, ndD))
            num+=1
        return arbre[0]

def Elagage(noeud, alpha, beta, depth = 0):
    #si le noeud est une feuille (dernier de l'arbre return ca valeur)
    if noeud.isFeuille():
        return noeud.val
    #test si le tour est pair ou impair si il est pair alors on cherche à obtenir le max si non l'adversaire cherche à nous faire obtenir le min 
    if depth%2 == 0:
        for e in noeud:
        #e correspond au branche à e est les branche à l'interieur de la branche e 
        #en gros en retournant e on retourne le noeud ou la feuille inférieur
            value = Elagage(e, depth+1, alpha, beta)
            MaxValue = -math.inf
            MaxValue = max(MaxValue, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return MaxValue   
    else: 
        for e in noeud:
            value = Elagage(e,depth+1, alpha, beta)
            MinValue = math.inf
            MinValue = min(MinValue, value)
            beta = min(alpha, value)
            if beta <= alpha:
                break
        return MinValue

Elagage(creer_arbre(), math.inf, -math.inf)






