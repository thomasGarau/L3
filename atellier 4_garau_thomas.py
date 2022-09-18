from msilib.schema import MsiDigitalSignature
import random
import copy
import time
import numpy as np
import matplotlib.pyplot as plt
from atellier2_garau_thomas import est_triee


#retourne une liste generer de x nombre aleatoire compris entre n et n 
def gen_list_random_int(nbr_int:int =10, range_min:int = 0, range_max:int = 10) ->list[int]:
    lst_nbr = []
    for e in range(0, nbr_int):
        lst_nbr.append(random.randint(range_min, range_max))
    return lst_nbr

#retourne une copy mélanger d'une liste passer en param
def mix_list(list_to_mix: list) ->list:
    copy_list = copy.deepcopy(list_to_mix)
    a = len(copy_list)
    i = 0
    lst_nbr = gen_list_random_int(a, 0, a-1)
    for e in range(0, a):
        copy_list.insert(lst_nbr[i], copy_list.pop(0))
        i+=1

    return copy_list
    
#retourne un element aleatoire d'une liste passer en param
def choose_element_list(lst: list) -> int:
    copy_lst = copy.deepcopy(lst)
    a = gen_list_random_int(1, 0, len(copy_lst)-1)
    return copy_lst[a[0]]

#retourne n element d'une liste passer en param 
def extract_element_list(lst: list, nbr_extract: int) -> list:
    copy_lst = copy.deepcopy(lst)
    lst_return = []
    a = gen_list_random_int(nbr_extract, 0, len(copy_lst)-1)
    for i in range(0, nbr_extract):
        lst_return.append(copy_lst[a[i]])
        i+=1
    return lst_return

def sort_list(list)->list :
    list_sorted = []
    maxi = 0
    mini = 0

    for e in list:
        indice_min = 0
        indice_max = len(list_sorted)
        milieu = (indice_max + indice_min) // 2
        if len(list_sorted) == 0:
            mini = e
            maxi = e

        if e >= maxi:
            list_sorted.append(e)
            maxi = e
        elif e <= mini:
            list_sorted.insert(0,e)
            mini = e
        else:
            while e < list_sorted[milieu] or e > list_sorted[milieu +1]:
                milieu = (indice_min + indice_max) //2
                if e > list_sorted[milieu]:
                    indice_min = milieu
                else:
                    indice_max = milieu
            list_sorted.insert(milieu +1, e)

    return list_sorted



#fonction test performance

def test_perf_loop(function: callable, list_to_mix, nb_execution):
    start_pc = time.perf_counter()
    for i in range(0,nb_execution):
        function(list_to_mix)
    end_pc = time.perf_counter()
    return (end_pc - start_pc) / nb_execution

def test_perf(fonction1:callable, fonction2:callable, nb_execution) ->float:
    list_serie_test_perso = []
    list_serie_test_base = []

    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_1k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_5k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_10k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_15k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_20k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_25k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_30k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_35k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_40k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_45k, nb_execution))
    list_serie_test_perso.append(test_perf_loop(fonction1, list_random_50k, nb_execution))

    list_serie_test_base.append(test_perf_loop(fonction2, list_random_1k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_5k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_20k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_25k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_20k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_25k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_30k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_35k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_40k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_45k, nb_execution))
    list_serie_test_base.append(test_perf_loop(fonction2, list_random_50k, nb_execution))
    print(list_serie_test_base, list_serie_test_perso)
    return list_serie_test_perso, list_serie_test_base

def test_perf_extract(fonction1:callable, fonction2:callable, list_to_extract, nb_extract) ->float:
    start_pc = time.perf_counter()
    fonction1(list_to_extract, nb_extract)
    end_pc = time.perf_counter()
    extract_temps = (end_pc - start_pc) / nb_extract

    start_pc = time.perf_counter()
    fonction2(list_to_extract, 10000)
    end_pc = time.perf_counter()
    sample_temps = (end_pc - start_pc) / nb_extract
    
    return extract_temps, sample_temps


#testu
list_random_50k = gen_list_random_int(50000,0,10000)
list_random_45k = gen_list_random_int(45000,0,10000)
list_random_40k = gen_list_random_int(40000,0,10000)
list_random_35k = gen_list_random_int(35000,0,10000)
list_random_30k = gen_list_random_int(30000,0,10000)
list_random_25k = gen_list_random_int(25000,0,10000)
list_random_20k = gen_list_random_int(20000,0,10000)
list_random_15k = gen_list_random_int(15000,0,10000)
list_random_10k = gen_list_random_int(10000,0,10000)
list_random_5k = gen_list_random_int(5000,0,10000)
list_random_1k = gen_list_random_int(1000,0,10000)

#print(gen_list_random_int(), "gen_list_random_int pas param")
#print(gen_list_random_int(15, 8,36), "gen_list_random_int pas param")
lst_test = ["aaa", 1,2,3,8,19,28,89,19902,199033, "bbb", "ccccc", "ddddd", ["aa,", "bbb", "ccc", "ddd", "eeee"]]
#print(mix_list(lst_test), "mix_list")
#print(choose_element_list(lst_test), "choose_element_list")
#print(extract_element_list(lst_test, 3), 3, "extract_element_list 3")
#print((sort_list(gen_list_random_int(10,0,1000))), "a")
list_triee_1k = sorted(gen_list_random_int(1000, 0, 1000))
list_inverse_1k = reversed(sorted(gen_list_random_int(1000, 0, 1000)))

#test perf
#print(test_perf(mix_list, random.shuffle,list_generated_10k, 100), "10k shuffle ")
#print(test_perf_extract(extract_element_list, random.sample, list_generated_10k, 10000), "10k sample")


def graph(perso,base):
    list_ordonnees = [i for i in range(0, 55000, 5000)]
    #Ici on décrit les abscisses
    #Entre 0 et 5 en 10 points
    x_axis_list = np.arange(0,0.0002)
    fig, ax = plt.subplots()
    #Dessin des courbes, le premier paramètre
    #correspond aux point d'abscisse le
    #deuxième correspond aux points d'ordonnées
    ax.plot(perso,list_ordonnees, 'b*-', label='perso')
    ax.plot(base,list_ordonnees,'r*-', label='base')
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',title='test performance')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()

#perso, base = test_perf(sort_list, sorted, 100)
#graph(perso, base)

#7----------------------------------------------------------------------

def stupid_sort(list_to_sort):
    taille = len(list_to_sort)
    list_random = [item for item in range(0, taille)]
    triee = False
    i = 0
    while not triee:
        #si i atteint taille on recommence à 0
        if i >= taille:
            i = 0

        #conserve la valeur avant de le supprimé 
        a = list_to_sort[i]
        list_to_sort.pop(i)
        # la replace à un index aleatoire
        list_to_sort.insert(choose_element_list(list_random), a)
        i+=1
        #verifie si par miracle c'est triee
        triee = est_triee(list_to_sort)
    return list_to_sort
              

def insertion_sort(list_to_sort) -> list:
    list_return = [list_to_sort[0]]
    for i in range(1, len(list_to_sort)):
        #les element de la liste sont triees jusqu'a i (j = i pour parcourir que les indice deja triee)
        j = i
        while j > 0 and list_to_sort[i] < list_return[j -1]:
            j -=1 
        list_return.insert(j, list_to_sort[i])

    return list_return

#en utilisant une seule liste 
#def insertion_sort2(list_to_sort) -> list:
    list_return = copy.deepcopy(list_to_sort)
    for i in range(1, len(list_return)):
        #les element de la liste sont triees jusqu a i (j = i pour parcourir que les indice deja triee)
        j = i
        while j > 0 and list_return[i] < list_return[j -1]:
            j -=1 
        list_return.insert(j, list_return.pop(i))

    return list_return


def selection_sort(list_to_sort: list) ->list:
    list_copy = copy.deepcopy(list_to_sort)
    for i in range(0,len(list_copy) -1):
        min = list_copy[i]
        index_min = i
        for j in range(i, len(list_copy)):
            if list_copy[j] < min:
                min = list_copy[j]
                index_min = j
        #si min = i alors c'étais déjà dans le bonne ordre 
        #faudrait test avec des doublons
        if min != list_copy[i]:
            list_copy.insert(i, list_copy.pop(index_min))
            #i+1 car le insert à décaler de 1
            list_copy.insert(index_min, list_copy.pop(i+1))
    return list_copy


def buble_sort(list_to_sort) -> list: 
    list_copy = copy.deepcopy(list_to_sort)
    #on part de l'inverse pour diminuer la deuxieme loop
    i =len(list_copy)
    trie = False
    while i > 0 and not trie:
        trie = True
        for j in range(0, i-1):
            if list_copy[j] > list_copy[j+1]:
                #inverse les position
                list_copy.insert(j, list_copy.pop(j+1))
                trie = False
    return list_copy


def merge_sort(list_copy) ->list:
    if len(list_copy) > 1:
       return merge(merge_sort(list_copy[:len(list_copy) //2]), merge_sort(list_copy[len(list_copy) //2: len(list_copy)]))
    else:
        return list_copy

def merge(list_a, list_b) -> list:
    if list_a == []:
        valeur_retour = list_b
    elif list_b == []:
        valeur_retour = list_a
    elif list_a[0] < list_b[0]:
        valeur_retour = merge(list_a[1:len(list_a)], list_b)
        valeur_retour.insert(0, list_a[0])
    else:
        valeur_retour = merge(list_a, list_b[1:len(list_b)])
        valeur_retour.insert(0, list_b[0])
    return valeur_retour




list_stupid = [4,8,2, 14, 27,13, 1, 3, 17, 96]
list_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]
list_copy = copy.deepcopy(list_to_sort)
#print(stupid_sort(list_stupid))
#print(to_sort_sort(list_to_sort))
#print(to_sort_sort2(list_to_sort))
#print(selection_sort(list_to_sort))
#print(buble_sort(list_to_sort))
#print(merge_sort(list_copy))

