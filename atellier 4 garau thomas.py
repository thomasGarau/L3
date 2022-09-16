import random
import copy
import time
import matplotlib.pyplot as plt
import numpy as np 

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
def choose_element_list(lst: list) ->any:
    copy_lst = copy.deepcopy(lst)
    a = gen_list_random_int(1, 0, len(copy_lst)-1)
    return copy_lst[a[0]]

#retourne n element d'une liste passer en param 
def extract_element_list(lst: list, nbr_extract: int) ->any:
    copy_lst = copy.deepcopy(lst)
    lst_return = []
    a = gen_list_random_int(nbr_extract, 0, len(copy_lst)-1)
    for e in a:
        lst_return.append(copy_lst[e])
    return lst_return


print(gen_list_random_int(), "gen_list_random_int pas param")
print(gen_list_random_int(15, 8,36), "gen_list_random_int pas param")
lst_test = ["aaa", 1,2,3,8,19,28,89,19902,199033, "bbb", "ccccc", "ddddd", ["aa,", "bbb", "ccc", "ddd", "eeee"]]
print(mix_list(lst_test), "mix_list")
print(choose_element_list(lst_test), "choose_element_list")
print(extract_element_list(lst_test, 3), 3, "extract_element_list 3")


#partie 2.1------------------------------------------------------------------------------
def test_perf(fonction1:callable, fonction2:callable, list_to_mix, nb_execution) ->time:
    start_pc = time.perf_counter()
    for i in range(0, nb_execution):
        fonction1(list_to_mix)
    end_pc = time.perf_counter()
    mix_list_temps = (end_pc - start_pc) / nb_execution

    start_pc = time.perf_counter()
    for i in range(0,nb_execution):
        fonction2(list_to_mix)
    end_pc = time.perf_counter()

    shuffle_temps = (end_pc - start_pc) / nb_execution

    return mix_list_temps, shuffle_temps

list_generated_100k = [item for item in range(0, 100000)]
list_generated_10k = [item for item in range(0, 10000)]
list_generated_1k = [item for item in range(0, 1000)]
list_generated_100 = [item for item in range(0, 100)]

print(test_perf(mix_list, random.shuffle, list_generated_1k, 100), "1k shuffle" )
print(test_perf(mix_list, random.shuffle, list_generated_10k, 100), "10K shuffle")
print(test_perf(mix_list, random.shuffle,list_generated_100k, 100), "100k shuffle ")

print(test_perf(mix_list, random.sample, list_generated_1k, 100), "1k sample" )
print(test_perf(mix_list, random.sample, list_generated_10k, 100), "10K sample")
print(test_perf(mix_list, random.sample,list_generated_100k, 100), "100k sample ")

