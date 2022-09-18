#import matplotlib.pyplot as plt
import unittest

#exo 1-----------------------------------------------------------------------------------------------------------------------------
#1

LIST_ENTIER = [1,67,29,98,18,73]

#additionne les valeur d'une liste est retourne la somme
def somme_for(L) -> int:
    somme = 0
    for e in L:
        somme += e
    return somme

#même chose mais avec une boucle i in range
def somme_range(L) -> int:
    somme = 0
    for i in range(len(L)):
        somme += L[i]
    return somme

#même fonction avec boucle while
#crash si vide avec <= comme condition ou i = len car index non existant
def somme_while(L):
    somme = 0
    i = 0
    while i < len(L):
        somme += L[i]
        i+=1
    return somme

#2 ----------------------------------------------------------------------------------------------------------------------------------

#test les différente fonction de l'exercice 1
def test_exercice1():

    print(somme_for(LIST_ENTIER) , "test base")
    print(somme_range(LIST_ENTIER) , "test base")
    print(somme_while(LIST_ENTIER) , "test base")

    #test liste vide
    LIST = []
    print(somme_for(LIST) , "vide")
    print(somme_range(LIST) , "vide")
    print(somme_while(LIST) , "vide")

    #test somme 11111
    S=[1,10,100, 1000,10000]
    print(somme_for(S) , ", 01")
    print(somme_range(S) , ", 01")
    print(somme_while(S) , ", 01")

    #test somme negatif
    NEGATIF_LIST = [-2,-8,698, -54, 76, -89]
    print(somme_for(NEGATIF_LIST) , ", negatif")
    print(somme_range(NEGATIF_LIST) , ", negatif")
    print(somme_while(NEGATIF_LIST) , ", negatif")
    
    #test avec puissance
    PUISSANCE_LIST = [4**2, 8**1, 9**2]
    print(somme_for(PUISSANCE_LIST) , ", puissance")
    print(somme_range(PUISSANCE_LIST) , ", puissance")
    print(somme_while(PUISSANCE_LIST) , ", puissance")

test_exercice1()

#3-----------------------------------------------------------------------------------------------
#prend en paramètres une liste est retourne la moyenne de ses valeurs
def moyenne(L) -> float:
    somme = 0
    if len(L) != 0:
        for e in L:
            somme += e
        return  round(somme / len(L), 2) 

print(moyenne(LIST_ENTIER), "exo 3")
print(moyenne([]), "exo 3")

#4-------------------------------------------------------------------------------------------------

#prend en paramètres une liste est une variable et retourne le nombre de fois ou la variable est supérieur à un élement de la liste
def nb_supp_in(L, e) -> int:
    nb_supp = 0
    for a in L:
        if a > e:
            nb_supp +=1
    return nb_supp

#meme fonction en utilisant in range
def nb_supp_range(L, e) ->int:
    nb_supp = 0
    for a in range(len(L)):
        if L[a] > e:
            nb_supp +=1
    return nb_supp

print(nb_supp_in(LIST_ENTIER, 50), "exo4")
print(nb_supp_range(LIST_ENTIER, 50), "exo4")

#5----------------------------------------------------------------------------------------------------------------------------------
# meme chose mais retourne uniquement la moyenne des nombre superieur à e ((la variable))
def moy_supp(L, e) ->float:
    somme_supp = 0 
    nb_supp = 0
    for a in L:
        if a > e:
            somme_supp += a
            nb_supp +=1
    return round(somme_supp / nb_supp, 2)

print(moy_supp(LIST_ENTIER, 50), "exo 5")

#6----------------------------------------------------------------------------------------------------------------------------------

# prend une liste en entrer est retourne le plus grand element de la liste
def val_max(L) -> int:
    max = 0
    for e in L:
        if e > max:
            max = e
    return max

print(val_max(LIST_ENTIER),"exo 6")

#7----------------------------------------------------------------------------------------------------------------------------------

#prend une liste en entrer est retourne l'index de sont plus grand élement
def ind_max(L) -> int:
    max = 0
    index_max = 0
    i = 0
    for e in L:
        if e > max: 
            max = e
            index_max = i
        i+=1
    return index_max

print(ind_max(LIST_ENTIER), "exo 7")


#exo 2--------------------------------------------------------------------------------------------------------
#1

#prend en paramètres une liste est un entier retourne l'index de la liste correspondant à l'entier, si celui-ci n'est pas présent retourne -1
def position(L,e) ->int:
    i = 0
    position_index = -1
    for a in L:
        if  e == a:
            position_index = i
        i +=1
    return position_index

#même fonction avec boucle while
#le while permet ici d'arreter la boucle si on trouve l'index plutot que de terminer le parcour de la liste
def position_while(L,e) ->int:
    i = 0
    position_index = -1
    while position_index == -1 or i < len(L):
        if  e == L[i]:
            position_index = i
        i +=1
    return position_index


print(position(LIST_ENTIER, 98), "for")
print(position(LIST_ENTIER, 4), "for")
print(position(LIST_ENTIER, 98), "while")
print(position(LIST_ENTIER, 4), "while")       

#2 -------------------------------------------------------------------------------------------------------------------------------------

LIST_ENTIER_REPETITION = [1,67,56,29,56,98,18,73,56,]

#prend en paramètres une liste est un entier est retourne le nombre de fois ou l'entier est présent dans la liste 
def nb_occurrences(L,e) ->int:
    repetition = 0

    for a in L:
        if e == a:
            repetition +=1
    return repetition

print(nb_occurrences(LIST_ENTIER_REPETITION, 56), "exo 2.2")
print(nb_occurrences(LIST_ENTIER_REPETITION, 73), "exo 2.2")


#3------------------------------------------------------------------------------------------------------------------------------------
LIST_CROISSANTE = [1,1,2,5,18,93,192,982]

#prend en paramètres une liste est retourne un bool si celle-ci est trié
def est_triee(L) -> bool:
    est_triee = True
    i = 0 
    while est_triee and i < len(L):
        try:
            if L[i] > L[i+1]:
                est_triee = False
        except Exception:
            pass
        
        i+=1

    return est_triee

#meme fonction avec une boucle while
def est_triee_while(L) ->bool:
    est_triee = True
    i = 0
    while est_triee and i < len(L)-1:
        print(i)
        if L[i] > L[i+1]:
            est_triee = False
        i+=1
    return est_triee

print(est_triee(LIST_ENTIER), "exo 3.3 pas trié for")
print(est_triee(LIST_CROISSANTE), "exo 3.3 trié for")
print(est_triee_while(LIST_ENTIER), "exo 3.3 pas trié while")
print(est_triee_while(LIST_CROISSANTE), "exo 3.3 trié while")


#4----------------------------------------------------------------------------------------------------------------------------------

LIST_GENERATED = [item for item in range(0, 100000)]
LIST_TEST = [6,8,9,10,16,18,19,24,26,29,35,36,37,42,43,47,57,59,68,69,73,78,89,90,98,145,167,189]

#dicothomie, prend une liste est un entier en paramètres est retourne l'index ou ce trouvent l'entier dans la liste
def position_tri(L,e) -> int:
    m = L.copy()
    indice_min = 0
    indice_max = len(m) -1
    #determine l'index milieu
    milieu = (indice_max + indice_min) // 2
    #1 c gauche 2 c droite
    while L[milieu] != e:
        #redetermine l'indice milieu
        milieu = (indice_max + indice_min) // 2
        # si e ce trouvent dans la moitier superieur de la liste on ne garde que celle-ci l'indice min ce retrouve donc changé
        if e > L[milieu]:
            indice_min = milieu +1
        # si non on garde  la premiere moitier inferieur de la liste
        else:
            indice_max = milieu -1
    
    return milieu,
 
print(position_tri(LIST_GENERATED, 37000)) #37K
print(position_tri(LIST_TEST, 37)) #12


#5------------------------------------------------------------------------------------------------------------------------------------

LIST_REPETITION = [1,3,6,8,19,78,78,98,189]
LIST_PAS_REPETITION = [1,3,6,8,19,78,98,189]

#prend une lsite en paramètres est vérifié qu'aucun element n'est présent deux fois 
def a_repetitions(L) -> bool:
    i = 0
    repetition = False
    t = []
    while repetition == False and i < len(L):
        if L[i] not in t:
            t.append(L[i])
        else: 
            repetition = True
        i+=1
    return repetition

print(a_repetitions(LIST_REPETITION), "2.5 repetition")
print(a_repetitions(LIST_PAS_REPETITION), "2.5 pas de repetition")


#exo 3--------------------------------------------------------------------------------------------------------------------------------------

LIST_A_SEPARER = [-1,6,9,0,0,-5,-567,678,-876,789,678,0,-4,-5,432, 0, 876,-543,0,-789,987]

#prend une liste en paramètres est retourne une seconde reprenant les élement de la première en les organisant comme suit :
# tout les négatif suivi de tout les 0 suivi de tout les nombre positif
def list_separation(L) -> list:
    LIST_SEPARER = []
    séparateur = 0
    for e in L:
        if e > 0:
            LIST_SEPARER.append(e)
        elif e < 0:
            LIST_SEPARER.insert(0, e)
            séparateur +=1
        else: 
            LIST_SEPARER.insert(séparateur, 0)

    return LIST_SEPARER

print(list_separation(LIST_A_SEPARER))
    
#exo 4----------------------------------------------------------------------------------------------------------------------------------

LIST_RIEN = [2,6,8,9,1,2,2,8,9,2,2,2]
LIST_TIROIR_INJECTIVE = [0,1,3,6,7,9]
LIST_TIROIR_SURJECTIVE = [0,2,3,1,5,8,4,6,7,9,9,3]
LIST_TIROIR_BIJECTIVE = [0,1,2,3,4,5,6,7,8]

#instancie la liste H rempli de 0 ou chacun des index de h représente un "tiroir" de F ((le tiroir 1 = h[1]))
#puis attribut une valeur à chaque index de 0 représentant le nombre de "boule" contenue dans le "tiroir" qu'il représente
def histo(F) -> list:
    maximum = max(F)
    LIST_HISTORIQUE = [0] * (maximum + 1)
    for e in F:
        LIST_HISTORIQUE[e] +=1

    return LIST_HISTORIQUE

# prend en paramètres une liste retourne un boolen déterminant si celle-ci est injective ou non 
def est_injective(F) -> bool:
    i = 0
    injective = True
    while injective == True and i < len(F):
        if F[i] > 1:
            injective = False
        else: 
            i+=1
    return injective

# prend en paramètres une liste retourne un boolen déterminant si celle-ci est surjective ou non 
def est_surjective(F) -> bool:
    i = 0
    surjective = True
    while surjective == True and i < len(F):
        if F[i] < 1:
            print(F[i], i)
            surjective = False
        else: 
            i+=1
    return surjective

# prend en paramètres une liste retourne un boolen déterminant si celle-ci est bijective ou non 
def est_bijective(F) -> bool:
    i = 0
    bijective = True
    while bijective == True and i < len(F):
        if F[i] != 1:
            bijective = False
        else: 
            i+=1
    return bijective

print(est_injective(histo(LIST_RIEN)), "test injective, liste pas injective")
print(est_injective(histo(LIST_TIROIR_INJECTIVE)), "test injective, liste injective")

print(est_surjective(histo(LIST_RIEN)), "test surjective, liste pas surjective")
print(est_surjective(histo(LIST_TIROIR_SURJECTIVE)), "test surjective, liste surjective")

print(est_bijective(histo(LIST_RIEN)), "test bijective, liste pas bijective")
print(est_bijective(histo(LIST_TIROIR_BIJECTIVE)), "test bijective, liste bijective")

#2-----------------------------------------------------------------------------------------------------------------------------------

#représente de facon graphique la fonction histo()
def affiche_histo(F):
    maximum_hauteur = max(F)
    maximum_longueur = len(F)
    i = 0
    i2 = maximum_hauteur
    a = "--"
    printu = ""
    printu2 = ""
    printu3 = ""

    while i2 > 0:
        while i < maximum_longueur:
            if F[i] >= i2:
                a = "# "
            else:
                a = "  "
            printu2 += f"| {a}|"
            i+=1
        printu2 += "\n"
        i = 0
        i2 -=1

    i = 0
    while i < maximum_longueur:
        printu3 += "| --|"
        printu += f"   {i} "
        i+=1

    return printu2  + printu3 + "\n" + printu

#3-------------------------------------------------------------------------------------------------------------------------------------

#utilise la lire plt pour afficher un diagramme représentant le nombre d'itération de chaque entier dans une liste passer en paramètres
print(affiche_histo(histo(LIST_RIEN)))

def affiche_histo_plt(F):
    plt.hist(F)
    plt.title("HISTOGRAMME")
    plt.show()

#affiche_histo_plt(LIST_RIEN)

#exo 5 ----------------------------------------------------------------------------------------------------------------------------
#1
OBJETS = [1,2,2,3,4,5,5]
OBJETS2 = [0,1,3,4,5,2,2,0]
#prend en paramètres une liste d'entier est la repartie dans deux liste de manière a ce que celle-ci ne comporte deux fois le même entier 
def agencement_vitrine(nbEmplacement, LIST_OBJETS_A_AFFICHER) ->list:
    vitrine = []
    vitrine2 = []
    i = 0
    possible = True
    list = sorted(LIST_OBJETS_A_AFFICHER)
    while possible and i <len(list):
        #si triplons pas possible 
        if list[i] == list[i+1] and list[i] == list[i+2]:
            possible = False
        else: 
            vitrine.append(list[i])
            vitrine2.append(list[i+1])
        i +=2
    return  vitrine, vitrine2

#exo6 ---------------------------------------------------------------------------------------------------------------------------------
#1

LIST_TEST = [0,2,5,7,7,18,39,48,98,76]

def present(L, e) ->bool:
    return e in L

def present1 (L, e) :
    for i in range (0, len(L), 1) : 
        if (L[i] == e) : 
            return(True)
        else : 
            return (False) 

def present2 (L, e) :
    b=True
    for i in range (0, len(L), 1) : 
        if (L[i] == e) : 
            b=True
        else : 
            b=False
    return (b)

def present3 (L, e) :
    b=True
    for i in range (0, len(L), 1) : 
        return (L[i] == e) 

def present4 (L, e) :
    b=False
    i=0
    while (i<len(L) and b) : 
        if (L[i] == e) : 
            b=True
    return (b)


def test_present(present:callable):
    if not present([], 3) :
        print("SUCCES : ", " test list vide doit retourné false")
    else: 
        print("ECHEC : ", " test list vide doit retourné false")
    
    if present(LIST_TEST, 0):
        print("SUCCES:", "test debut ((première élement de la liste)) doit retourné true" )
    else: 
        print ("ECHEC:", "test debut ((première élement de la liste)) doit retourné true")

    if present(LIST_TEST, LIST_TEST[((len(LIST_TEST) -1) // 2)]):
        print("SUCCES: ", "test milieu doit retourné true" )
    else: 
        print("ECHEC", "test milieu  doit retourné true")

    if not present(LIST_TEST, 3):
        print("SUCCES: test entier pas présent doit retourné false")
    else: 
        print("ECHEC: test entier pas présent doit retourné false")

print("present")
test_present(present)
print("present1")
test_present(present1)
print("present2")
test_present(present2)
print("preset 3")
test_present(present3)
print("present4")
test_present(present4)

#a corrigé present 1 2 3 4


print(agencement_vitrine(4,OBJETS2), "exo 5")
