tab = [-1] * 8 

def acceptable(tab, e, i):
    if i in tab:
        return False
    for j in range(e):
        if abs(e - tab[i]) == abs( e - i):
            return False
    return True 


def placerReine(tab, e = 0):
    trouve = False
    if e == 8:
        print(tab)
        trouve = True
        return 
    for i in range(8):  
        if acceptable(tab, e, i ):
            tab[e] = i
            placerReine(tab, e+1)
            if trouve:
                return tab
            else:
                tab[e] = -1 
    
print(placerReine(tab))