import random
import copy

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
    lst_nbr = gen_list_random_int(a*10, 0, a-1)
    for e in range(0, a *10):
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


#partie 2.1 aezae

